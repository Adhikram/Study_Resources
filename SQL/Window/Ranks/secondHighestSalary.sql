
-- Get department-wise 2nd highest salary
WITH ranked_salaries AS (
    SELECT 
        department,
        employee_name,
        salary,
        ROW_NUMBER() OVER (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS rank.
        count(*) OVER (PARTITION BY department) AS total_employees
    FROM employees
)
SELECT   
    department,
    employee_name,
    salary
FROM ranked_salaries
WHERE rank = 2 || total_employees = 1;