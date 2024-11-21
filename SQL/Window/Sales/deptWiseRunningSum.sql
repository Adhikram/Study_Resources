/*
Problem: Calculate Running Total of Salaries by Department
- Group by department number
- Order by employee name within each department
- Show running sum of salaries
*/

-- Input Table Structure:
-- emp
-- deptno    INT
-- empno     INT
-- ename     VARCHAR
-- job       VARCHAR
-- sal       DECIMAL

-- Sample Input:
-- deptno    empno    ename    job        sal
-- 10        7934     MILLER   CLERK      1300
-- 10        7900     JAMES    CLERK      950
-- 20        7566     JONES    MANAGER    2975

-- Calculate department-wise running totals
SELECT 
    deptno,
    empno,
    ename,
    job,
    sal,
    SUM(sal) OVER (
        PARTITION BY deptno
        ORDER BY ename
    ) AS running_total
FROM emp
ORDER BY 
    deptno,
    ename;

-- Expected Output:
-- deptno  empno  ename   job       sal    running_total
-- 10      7934   MILLER  CLERK     1300   1300
-- 10      7900   JAMES   CLERK     950    2250
-- 20      7566   JONES   MANAGER   2975   2975

/* Performance Optimizations:
1. Efficient partitioning by department
2. Single table query - no joins needed
3. Consider index on (deptno, ename)
4. Ordered window function for running totals
5. Minimal columns in result set
*/
