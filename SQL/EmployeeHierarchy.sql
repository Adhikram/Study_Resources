--- Q8 : Find the hierarchy --- 
-- Solution
with recursive cte as (
    select *
    from emp_details
    where name = 'Asha'
    union
    select e.*
    from cte
        join emp_details e on e.manager_id = cte.id
)
select *
from cte;