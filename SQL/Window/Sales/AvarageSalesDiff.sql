--- Q9 : Find difference in average sales --- 
-- Solution
with cte as (
        select year_id,
                month_id,
                to_char(order_date, 'MON') as mon,
                avg(sales) as avg_sales_per_month
        from sales_order s
        where year_id in (2003, 2004)
        group by year_id,
                month_id,
                to_char(order_date, 'MON')
)
select y03.mon,
        round(
                abs(
                        y03.avg_sales_per_month - y04.avg_sales_per_month
                )::decimal,
                2
        ) as diff
from cte y03
        join cte y04 on y03.mon = y04.mon
where y03.year_id = 2003
        and y04.year_id = 2004
order by y03.month_id;