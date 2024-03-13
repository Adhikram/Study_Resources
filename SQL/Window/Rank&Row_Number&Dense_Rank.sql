-- Calculate the rank according to the salary of the employee and order by the salary of the employee in ascending order. Use Empno when sal is the same.
select empno,
    ename,
    job,
    hiredate,
    sal,
    row_number() over(
        order by sal,
            empno
    ) as row_num,
    rank() over(
        order by sal
    ) as rnk,
    dense_rank() over(
        order by sal
    ) as sal_dense_rnk
from emp
order by sal;
-- Input
-- emp table
-- empno  ename   job       hiredate   sal
-- 7839   KING    PRESIDENT 1990-06-09 5000
-- 7566   JONES   MANAGER   1995-10-31 2975
-- 7698   BLAKE   MANAGER   1992-06-11 2850
-- 7782   CLARK   MANAGER   1993-05-14 2450
-- 7788   SCOTT   ANALYST   1996-03-05 3000
-- 7902   FORD    ANALYST   1997-12-05 3000
-- 7844   TURNER  SALESMAN  1995-06-04 1500
-- 7900   JAMES   CLERK     2000-06-23 950
-- 7654   MARTIN  SALESMAN  1998-12-05 1250
-- 7499   ALLEN   SALESMAN  2001-02-11 1600
-- 7521   WARD    SALESMAN  1996-03-26 1250
-- 7934   MILLER  CLERK     2000-01-21 1300
-- Output
-- empno  ename   job       hiredate   sal  row_num  rnk  sal_dense_rnk
-- 7934   MILLER  CLERK     2000-01-21 1300 1        1    1
-- 7654   MARTIN  SALESMAN  1998-12-05 1250 2        2    2
-- 7521   WARD    SALESMAN  1996-03-26 1250 3        2    2
-- 7844   TURNER  SALESMAN  1995-06-04 1500 4        4    3
-- 7499   ALLEN   SALESMAN  2001-02-11 1600 5        5    4
-- 7900   JAMES   CLERK     2000-06-23 950  6        6    5
-- 7782   CLARK   MANAGER   1993-05-14 2450 7        7    6
-- 7698   BLAKE   MANAGER   1992-06-11 2850 8        8    7
-- 7788   SCOTT   ANALYST   1996-03-05 3000 9        9    8
-- 7902   FORD    ANALYST   1997-12-05 3000 10       9    8
-- 7566   JONES   MANAGER   1995-10-31 2975 11       11   9
-- 7839   KING    PRESIDENT 1990-06-09 5000 12       12   10