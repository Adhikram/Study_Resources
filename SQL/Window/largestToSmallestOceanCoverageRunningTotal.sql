/*
Problem: Calculate Running Total of Ocean Coverage
- Order from largest to smallest water bodies
- Group by water body type
- Calculate 3-row rolling sum (previous, current, next)
*/

-- Input Table Structure:
-- water
-- name          VARCHAR
-- type          VARCHAR
-- square_km     DECIMAL

-- Sample Input:
-- name        type    square_km
-- Pacific     ocean   165250000
-- Atlantic    ocean   106460000
-- Indian      ocean   73556000

-- Method 1: Using Window Function with Row Frame
SELECT 
    name,
    type,
    square_km,
    SUM(square_km) OVER (
        PARTITION BY type
        ORDER BY square_km DESC 
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS running_total
FROM water
ORDER BY square_km DESC;

-- Method 2: Using Range Frame
SELECT 
    name,
    type,
    square_km,
    SUM(square_km) OVER (
        PARTITION BY type
        ORDER BY square_km DESC
        RANGE BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING
    ) AS cumulative_total
FROM water
ORDER BY square_km DESC;

-- Expected Output:
-- name        type    square_km    running_total
-- Pacific     ocean   165250000    271710000
-- Atlantic    ocean   106460000    345316000
-- Indian      ocean   73556000     200016000

/* Performance Optimizations:
1. Efficient window frame definition
2. Smart partitioning by water body type
3. Consider index on (type, square_km)
4. Multiple implementation approaches
5. Optimal sort order for large datasets
*/
