--- Q8 : Find the hierarchy --- 
-- Solution
with recursive cte as (
    select *
    from emp_details
    where name = 'Asha'
    union
    select e.*
    from cte
        join emp_details e on e.manager_id = cte.id
)
select *
from cte;
WITH RECURSIVE ManagerHierarchy AS (
  SELECT 
    EmployeeID,
    ManagerID,
    1 AS Level
  FROM 
    Employees
  WHERE 
    EmployeeID = <employee_id>
  UNION ALL

  SELECT
    e.EmployeeID,
    e.ManagerID,
    h.Level + 1
  FROM
    Employees e
  INNER JOIN
    ManagerHierarchy h ON e.ManagerID = h.EmployeeID
)
SELECT
  EmployeeID,
  ManagerID,
  Level
FROM
  ManagerHierarchy
ORDER BY
  Level DESC;
-- Input:
-- emp_details
-- +----+--------+------------+
-- | id | name   | manager_id |
-- +----+--------+------------+
-- | 1  | Asha   | NULL       |
-- | 2  | Bala   | 1          |
-- | 3  | Chitra | 2          |
-- | 4  | Deepa  | 2          |
-- | 5  | Ela    | 3          |
-- | 6  | Fathima| 3          |
-- +----+--------+------------+
-- Output:
-- +----+--------+------------+
-- | id | name   | manager_id |
-- +----+--------+------------+
-- | 1  | Asha   | NULL       |
-- | 2  | Bala   | 1          |
-- | 3  | Chitra | 2          |
-- | 5  | Ela    | 3          |
-- | 6  | Fathima| 3          |
-- +----+--------+------------+