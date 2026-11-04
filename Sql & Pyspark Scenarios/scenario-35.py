with cte as (
    select customer_id,
           trunc(order_date,'MM') as month_dt,
           row_number() over(
               partition by customer_id
               order by trunc(order_date,'MM')
           ) as rn
    from kholi
),
cte2 as (
    select *,
           add_months(month_dt,-rn) as grp
    from cte
)
select customer_id
from cte2
group by customer_id, grp
having count(*) >= 3;
