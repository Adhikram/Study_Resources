/*
Problem: Fill NULL Values in Department Data
- Replace NULL department values with last known value
- Maintain sequential order
- Track employee details with department assignments
*/

-- Input Table Structure:
-- external_emp
-- seq           INT
-- empno         INT
-- ename         VARCHAR
-- job           VARCHAR
-- mgr           INT
-- hiredate      DATE
-- sal           DECIMAL
-- deptno        INT (nullable)

-- Sample Input:
-- seq    empno    ename    deptno
-- 1      7839     KING     10
-- 2      7698     BLAKE    NULL
-- 3      7782     CLARK    NULL
-- 4      7566     JONES    20

SELECT 
    seq,
    empno,
    ename,
    job,
    mgr,
    hiredate,
    sal,
    deptno,
    LAST_VALUE(deptno IGNORE NULLS) OVER (
        ORDER BY seq
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS filled_dept
FROM external_emp;

-- Method 2: Using COALESCE with LAG
SELECT 
    seq,
    empno,
    ename,
    job,
    mgr,
    hiredate,
    sal,
    deptno,
    COALESCE(
        deptno,
        LAG(deptno IGNORE NULLS) OVER (ORDER BY seq)
    ) AS filled_dept
FROM external_emp;

-- Expected Output:
-- seq    empno    ename    deptno    filled_dept
-- 1      7839     KING     10        10
-- 2      7698     BLAKE    NULL      10
-- 3      7782     CLARK    NULL      10
-- 4      7566     JONES    20        20

/* Performance Optimizations:
1. Efficient LAST_VALUE with IGNORE NULLS
2. Optimal window frame definition
3. Consider index on (seq)
4. Multiple implementation options
5. Smart NULL handling strategies
*/
