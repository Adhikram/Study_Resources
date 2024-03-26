--- Q10: Pizza Delivery Status --- 
-- Solution 
select distinct cust_name as customer_name,
    'COMPLETED' as status
from cust_orders D
where D.status = 'DELIVERED'
    and not exists (
        select 1
        from cust_orders d2
        where d2.cust_name = d.cust_name
            and d2.status in ('SUBMITTED', 'CREATED')
    )
union
select distinct cust_name as customer_name,
    'IN PROGRESS' as status
from cust_orders D
where D.status = 'DELIVERED'
    and exists (
        select 1
        from cust_orders d2
        where d2.cust_name = d.cust_name
            and d2.status in ('SUBMITTED', 'CREATED')
    )
union
select distinct cust_name as customer_name,
    'AWAITING PROGRESS' as status
from cust_orders D
where D.status = 'SUBMITTED'
    and not exists (
        select 1
        from cust_orders d2
        where d2.cust_name = d.cust_name
            and d2.status in ('DELIVERED')
    )
union
select distinct cust_name as customer_name,
    'AWAITING SUBMISSION' as status
from cust_orders D
where D.status = 'CREATED'
    and not exists (
        select 1
        from cust_orders d2
        where d2.cust_name = d.cust_name
            and d2.status in ('DELIVERED', 'SUBMITTED')
    );
CREATE OR REPLACE FUNCTION get_orders_by_status(status_list text []) RETURNS TABLE (result integer, cust_name text) AS $$ BEGIN RETURN QUERY
SELECT 1,
    cust_name
FROM cust_orders
WHERE status = ANY(status_list);
END;
$$
select distinct cust_name as customer_name,
    'COMPLETED' as status
from cust_orders D
where D.status = 'DELIVERED'
    and not exists get_orders_by_status(array ['SUBMITTED', 'CREATED'], D.cust_name)
union
select distinct cust_name as customer_name,
    'IN PROGRESS' as status
from cust_orders D
where D.status = 'DELIVERED'
    and exists get_orders_by_status(array ['SUBMITTED', 'CREATED'], D.cust_name)
union
select distinct cust_name as customer_name,
    'AWAITING PROGRESS' as status
from cust_orders D
where D.status = 'SUBMITTED'
    and not exists get_orders_by_status(array ['DELIVERED'], D.cust_name)
union
select distinct cust_name as customer_name,
    'AWAITING SUBMISSION' as status
from cust_orders D
where D.status = 'CREATED'
    and not exists get_orders_by_status(array ['DELIVERED', 'SUBMITTED'], D.cust_name);