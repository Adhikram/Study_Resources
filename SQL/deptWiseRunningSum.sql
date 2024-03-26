-- need departmental salaries running total by employee name
select deptno,
    empno,
    ename,
    job,
    sal,
    sum(sal) over(
        partition by deptno
        order by ename
    ) as total
from emp
order by deptno,
    ename;

-- Output
-- deptno  empno  ename   job       sal  total
-- 10      7934   MILLER  CLERK     1300 1300
-- 10      7900   JAMES   CLERK     950  2250
-- 20      7566   JONES   MANAGER   2975 2975
-- 20      7782   CLARK   MANAGER   2450 5425
-- 20      7788   SCOTT   ANALYST   3000 8425
-- 20      7902   FORD    ANALYST   3000 11425
-- 20      7876   ADAMS   CLERK     1100 12525
-- 30      7698   BLAKE   MANAGER   2850 2850
