-- Solution:
select *,
    max(salary) over(
        partition by dept
        range between unbounded preceding and unbounded following
    ) as highest_sal,
    min(salary) over(
        partition by dept
        range between unbounded preceding and unbounded following
    ) as lowest_sal
from employee;