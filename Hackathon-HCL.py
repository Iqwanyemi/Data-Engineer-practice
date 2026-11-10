create OR REPLACE EXTERNAL TABLE `test.brz_accounts_ext`
OPTIONS (
 format = 'CSV',
 uris = ['gs://customer-data-project-iqwan/hackathon/src_data/BankEvalDB_Day0_Interleaved.txt'],
 field_delimiter = '|',
 skip_leading_rows = 1,
 allow_jagged_rows = true
);

====================================================================================

CREATE OR REPLACE TABLE `test.branches` AS
SELECT
 SAFE_CAST(string_field_0 AS INT64) AS BranchID,
 string_field_1 AS BranchName,
 string_field_2 AS Town,
 string_field_3 AS County,
 string_field_4 AS Region,
 string_field_5 AS SortCodePrefix,
 SAFE_CAST(LEFT(string_field_6, 10) AS DATE) AS OpenDate
FROM
 `test.brz_accounts_ext`
WHERE
 LOWER(string_field_1) LIKE '%branch%'
 AND LOWER(string_field_1) NOT IN ('branchname', 'branchid')
 AND string_field_0 IS NOT NULL;
 
 ==================================== 
 
 CREATE OR REPLACE TABLE `test.employees` AS
SELECT 
 SAFE_CAST(string_field_0 AS INT64) AS EmployeeID,
 SAFE_CAST(string_field_1 AS INT64) AS BranchID,
 string_field_2 AS FirstName,
 string_field_3 AS LastName,
 string_field_4 AS JobTitle,
 SAFE_CAST(LEFT(string_field_5, 10) AS DATE) AS HireDate,
 SAFE_CAST(string_field_6 AS INT64) AS ManagerID
FROM `test.brz_accounts_ext`
WHERE string_field_0 NOT IN ('HDR', 'FTR', 'EmployeeID')
 AND string_field_4 IN ('Teller', 'Personal Banker', 'Customer Service Rep', 'Loan Officer', 'Branch Manager');
===================================================
CREATE OR REPLACE TABLE `test.account_types` AS
SELECT 
 SAFE_CAST(string_field_0 AS INT64) AS AccountTypeID,
 string_field_1 AS TypeName,
 SAFE_CAST(string_field_2 AS FLOAT64) AS InterestRate,
 SAFE_CAST(string_field_3 AS FLOAT64) AS MinBalance,
 SAFE_CAST(string_field_4 AS FLOAT64) AS OverdraftLimit
FROM `test.brz_accounts_ext`
WHERE string_field_0 NOT IN ('HDR', 'FTR', 'AccountTypeID')
 AND string_field_1 IN ('Checking', 'Savings', 'MoneyMarket', 'CD-12Month', 'BusinessChecking');
 ==================================================
 CREATE OR REPLACE TABLE `test.customers` AS
SELECT 
 SAFE_CAST(string_field_0 AS INT64) AS CustomerID,
 string_field_1 AS FirstName,
 string_field_2 AS LastName,
 SAFE_CAST(LEFT(string_field_3, 10) AS DATE) AS DateOfBirth,
 string_field_4 AS NationalInsuranceNumber,
 string_field_5 AS Email,
 string_field_6 AS Phone,
 string_field_7 AS AddressLine1,
 string_field_8 AS Town,
 string_field_9 AS County,
 string_field_10 AS PostCode,
 -- Handle shifting columns safely
 CASE 
 WHEN string_field_11 IN ('Verified', 'Pending', 'Expired') THEN string_field_12 
 ELSE string_field_11 
 END AS CustomerSegment,
 CASE 
 WHEN string_field_11 IN ('Verified', 'Pending', 'Expired') THEN string_field_11 
 ELSE string_field_12 
 END AS KYCStatus,
 SAFE_CAST(LEFT(string_field_13, 10) AS DATE) AS CreatedDate
FROM `test.brz_accounts_ext`
WHERE string_field_0 NOT IN ('HDR', 'FTR', 'CustomerID')
 AND SAFE_CAST(string_field_0 AS INT64) IS NOT NULL
 AND (string_field_12 IN ('Verified', 'Pending', 'Expired') 
 OR string_field_11 IN ('Verified', 'Pending', 'Expired'));
 
 ======================================================
 
 CREATE OR REPLACE TABLE `test.transactions` AS
SELECT 
 SAFE_CAST(string_field_0 AS INT64) AS TransactionID,
 SAFE_CAST(string_field_1 AS INT64) AS AccountID,
 SAFE_CAST(string_field_2 AS INT64) AS TransactionTypeID,
 SAFE_CAST(string_field_3 AS TIMESTAMP) AS TransactionDateTime,
 SAFE_CAST(string_field_4 AS FLOAT64) AS Amount,
 string_field_5 AS Currency,
 string_field_6 AS Channel,
 string_field_7 AS MerchantCategory,
 string_field_8 AS Description,
 SAFE_CAST(string_field_9 AS FLOAT64) AS BalanceAfter,
 SAFE_CAST(string_field_10 AS INT64) AS EmployeeID
FROM `test.brz_accounts_ext`
WHERE string_field_0 NOT IN ('HDR', 'FTR', 'TransactionID')
 AND SAFE_CAST(string_field_0 AS INT64) IS NOT NULL
 AND (string_field_6 IN ('POS', 'MobileApp', 'ATM', 'Branch', 'Online') OR string_field_6 IS NULL)
 AND string_field_5 IN ('GBP', 'EUR', 'USD', 'CHF', 'AED');
======================================= 
CREATE OR REPLACE TABLE `test.cards` AS
SELECT 
 SAFE_CAST(string_field_0 AS INT64) AS CardID,
 SAFE_CAST(string_field_1 AS INT64) AS AccountID,
 string_field_2 AS CardNumberMasked,
 string_field_3 AS CardType,
 SAFE_CAST(LEFT(string_field_4, 10) AS DATE) AS IssueDate,
 SAFE_CAST(LEFT(string_field_5, 10) AS DATE) AS ExpiryDate,
 string_field_6 AS Status
FROM `otuscrt2-an-prd-615f.test.brz_accounts_ext`
WHERE string_field_0 NOT IN ('HDR', 'FTR', 'CardID')
 AND SAFE_CAST(string_field_0 AS INT64) IS NOT NULL
 AND string_field_3 IN ('Debit', 'Credit');
 ++++++++++++++++++++
 CREATE OR REPLACE TABLE `test.transaction_types` AS
SELECT 
 SAFE_CAST(string_field_0 AS INT64) AS TransactionTypeID,
 string_field_1 AS TypeName,
 string_field_2 AS Category
FROM `test.brz_accounts_ext`
WHERE string_field_0 NOT IN ('HDR', 'FTR', 'TransactionTypeID')
 AND SAFE_CAST(string_field_0 AS INT64) IS NOT NULL
 AND string_field_1 IN (
 'Deposit', 'Withdrawal', 'POS Purchase', 'ATM Withdrawal', 
 'Transfer In', 'Transfer Out', 'Fee', 'Interest Credit', 
 'Direct Deposit', 'Loan Payment'
 );
 
 ==============================
 CREATE OR REPLACE TABLE `test.loans` AS
WITH numbered AS (
 SELECT *, ROW_NUMBER() OVER() as rn
 FROM `test.brz_accounts_ext`
),
start_row AS (
 SELECT MIN(rn) AS start_rn
 FROM numbered
 WHERE string_field_0 = 'HDR' AND string_field_1 = 'LOANS'
),
end_row AS (
 SELECT MIN(rn) AS end_rn
 FROM numbered
 WHERE rn > (SELECT start_rn FROM start_row)
 AND (string_field_0 = 'FTR' OR string_field_0 LIKE 'HDR%')
)
SELECT 
 SAFE_CAST(string_field_0 AS INT64) AS LoanID,
 SAFE_CAST(string_field_1 AS INT64) AS CustomerID,
 SAFE_CAST(string_field_2 AS INT64) AS BranchID,
 string_field_3 AS LoanType,
 SAFE_CAST(string_field_4 AS FLOAT64) AS PrincipalAmount,
 SAFE_CAST(string_field_5 AS FLOAT64) AS InterestRate,
 SAFE_CAST(string_field_6 AS INT64) AS TermMonths,
 SAFE_CAST(LEFT(string_field_7, 10) AS DATE) AS StartDate,
 string_field_8 AS Status
FROM numbered
WHERE rn > (SELECT start_rn FROM start_row) + 1
 AND rn < (SELECT end_rn FROM end_row);
