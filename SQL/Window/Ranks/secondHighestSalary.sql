/*
Problem: Find Second Highest Salary by Department
- Get department-wise second highest salaries
- Handle departments with single employee
- Include employee details
*/

-- Input Table Structure:
-- employees
-- department      VARCHAR
-- employee_name   VARCHAR
-- salary         DECIMAL

-- Sample Input:
-- department    employee_name    salary
-- IT           John             80000
-- IT           Jane             85000
-- HR           Mike             65000

-- Method 1: Using ROW_NUMBER
WITH ranked_salaries AS (
    SELECT 
        department,
        employee_name,
        salary,
        ROW_NUMBER() OVER (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS rank,
        COUNT(*) OVER (
            PARTITION BY department
        ) AS total_employees
    FROM employees
)
SELECT   
    department,
    employee_name,
    salary
FROM ranked_salaries
WHERE rank = 2 
OR total_employees = 1;


-- Expected Output:
-- department    employee_name    salary
-- IT           John             80000
-- HR           Mike             65000

/* Performance Optimizations:
1. Efficient window functions
2. Smart handling of single-employee departments
3. Consider index on (department, salary)
4. Multiple implementation options
5. Optimal partitioning strategy
*/
