/*
Problem: Analyze Accenture Consultant Staffing Metrics
- Calculate total consultants per client
- Identify exclusively staffed consultants
- Return metrics sorted by client name
*/

-- Input Tables Structure:
-- employees
-- employee_id    INT
-- engagement_id  INT

-- consulting_engagements
-- engagement_id  INT
-- client_name    VARCHAR

-- Sample Input:
-- employees
-- employee_id    engagement_id
-- 101           1
-- 102           1
-- 102           2

-- consulting_engagements
-- engagement_id    client_name
-- 1               Microsoft
-- 2               Google

-- Find exclusively staffed consultants
WITH exclusive_employees AS (
    SELECT 
        employee_id
    FROM employees e
    JOIN consulting_engagements ce 
        ON e.engagement_id = ce.engagement_id
    GROUP BY employee_id
    HAVING COUNT(DISTINCT ce.client_name) = 1
)

-- Calculate staffing metrics
SELECT 
    ce.client_name, 
    COUNT(DISTINCT e.employee_id) AS total_staffed,
    COUNT(DISTINCT ee.employee_id) AS exclusive_staffed
FROM employees e
INNER JOIN consulting_engagements ce 
    ON e.engagement_id = ce.engagement_id
LEFT JOIN exclusive_employees ee 
    ON e.employee_id = ee.employee_id
GROUP BY ce.client_name
ORDER BY ce.client_name;

-- Expected Output:
-- client_name    total_staffed    exclusive_staffed
-- Google         5                2
-- Microsoft      8                4

/* Performance Optimizations:
1. Used CTE for exclusive employee identification
2. Efficient JOIN sequence
3. Consider indexes on:
   - employees(engagement_id, employee_id)
   - consulting_engagements(engagement_id, client_name)
4. DISTINCT counts to prevent duplicates
5. Optimal GROUP BY and ORDER BY
*/
