/*
Problem: Display Employee ID with their Team Count
- Show every employee with the count of members in their team
- Include all employees in the result
*/

-- Input Table Structure:
-- Employee
-- employee_id    INT
-- team_id       INT

-- Approach 1: Using CTE (Common Table Expression)
WITH team_data AS (
    SELECT team_id, COUNT(*) AS team_count 
    FROM employee 
    GROUP BY team_id
)
SELECT 
    em.employee_id, 
    td.team_count 
FROM employee AS em 
JOIN team_data AS td 
    ON em.team_id = td.team_id;

-- Approach 2: Using Correlated Subquery
SELECT 
    e.employee_id,
    (SELECT COUNT(*) 
     FROM employee e2 
     WHERE e2.team_id = e.team_id) AS team_count
FROM employee e;

-- Approach 3: Using Window Function
SELECT 
    employee_id,
    COUNT(*) OVER(PARTITION BY team_id) AS team_count
FROM employee;

-- Approach 4: Using LEFT JOIN with GROUP BY
SELECT 
    e1.employee_id,
    COUNT(e2.employee_id) AS team_count
FROM employee e1
LEFT JOIN employee e2 
    ON e1.team_id = e2.team_id
GROUP BY e1.employee_id, e1.team_id;

/* Performance Notes:
1. Window function approach is most efficient for large datasets
2. CTE approach provides better readability
3. Consider indexing on team_id for better join performance
4. Correlated subquery might be slower for large datasets
*/
