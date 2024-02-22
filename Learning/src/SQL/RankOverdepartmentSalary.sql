-- Rank Salaries within Departments
SELECT RANK() OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS dept_ranking,
    department,
    employee_id,
    full_name,
    salary
FROM employee;
-- Explain Time Complexity
-- The time complexity of the RANK() function is O(n log n), 
-- where n is the number of rows in the result set. 
-- The function first sorts the result set by the partitioning column and the ordering column, 
-- which takes O(n log n) time. Then, it assigns a rank to each row based on the order of the ordering column within each partition,
-- which also takes O(n log n) time. Therefore, the overall time complexity of the RANK() function is O(n log n).
-- Input
-- employee table
-- employee_id  full_name  department  salary
-- 1            John Doe   Sales       50000
-- 2            Jane Smith Sales       60000
-- 3            Tom Allen  Marketing   70000
-- 4            Sarah BrownMarketing   80000
-- 5            Mike Davis Marketing   90000
-- Output
-- dept_ranking  department  employee_id  full_name  salary
-- 1             Sales       2            Jane Smith 60000
-- 2             Sales       1            John Doe   50000
-- 1             Marketing   5            Mike Davis 90000
-- 2             Marketing   4            Sarah Brown80000
-- 3             Marketing   3            Tom Allen  70000