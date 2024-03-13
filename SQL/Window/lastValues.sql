-- Fill in the blanks for the null values in DEPTNPO table and count the employees according to departments.
select seq,
    empno,
    ename,
    job,
    mgr,
    hiredate,
    sal,
    deptno,
    last_value(deptno ignore nulls) over(
        order by seq
    ) as dept
from external_emp
