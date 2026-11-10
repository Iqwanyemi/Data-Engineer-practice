CREATE TABLE numbers (
    id INT PRIMARY KEY
);

INSERT INTO numbers (id) VALUES 
(1), 
(2), 
(4), 
(5), 
(8), 
(9), 
(10);

select id1+1 as nums from numbers_1 where id1+1 not in (select id1 from numbers_1 ) and id1 < (select max(id1) from numbers_1)

or 

SELECT t1.id + 1 AS missing_num
FROM numbers t1
WHERE NOT EXISTS (
    SELECT 1 
    FROM numbers t2 
    WHERE t2.id = t1.id + 1
)
  AND t1.id < (SELECT MAX(id) FROM numbers);
