-- Solution:
select *,
    max(salary) over(
        partition by dept
        order by salary desc
    ) as highest_sal,
    min(salary) over(
        partition by dept
        order by salary desc range between unbounded preceding and unbounded following
    ) as lowest_sal
from employee;