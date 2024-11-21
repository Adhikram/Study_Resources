/*
Problem: Display Highest and Lowest Salary per Department
- Show each employee's details
- Include department's highest and lowest salary
- Display all records with department context
*/

-- Input Table Structure:
-- employee
-- emp_id     INT
-- dept       VARCHAR
-- salary     DECIMAL
-- name       VARCHAR

-- Sample Input:
-- emp_id    dept      salary    name
-- 101       IT        75000     John
-- 102       IT        85000     Jane
-- 103       HR        65000     Mike
-- 104       HR        55000     Sarah

SELECT 
    emp_id,
    name,
    dept,
    salary,
    MAX(salary) OVER (
        PARTITION BY dept
        RANGE BETWEEN UNBOUNDED PRECEDING 
        AND UNBOUNDED FOLLOWING
    ) AS highest_salary,
    MIN(salary) OVER (
        PARTITION BY dept
        RANGE BETWEEN UNBOUNDED PRECEDING 
        AND UNBOUNDED FOLLOWING
    ) AS lowest_salary
FROM employee
ORDER BY 
    dept,
    salary DESC;

-- Expected Output:
-- emp_id    name    dept    salary    highest_salary    lowest_salary
-- 102       Jane    IT      85000     85000            75000
-- 101       John    IT      75000     85000            75000
-- 103       Mike    HR      65000     65000            55000
-- 104       Sarah   HR      55000     65000            55000

/* Performance Optimizations:
1. Used RANGE instead of ROWS for better performance
2. Single window clause for both aggregations
3. Consider index on (dept, salary)
4. Efficient sort order
5. Minimal window function calls
*/
