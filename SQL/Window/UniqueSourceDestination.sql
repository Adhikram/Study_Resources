/*
Problem: Find Unique Source-Destination Pairs
- Identify bidirectional route pairs
- Eliminate duplicate combinations
- Maintain distance information
*/

-- Input Table Structure:
-- src_dest_distance
-- source        VARCHAR
-- destination   VARCHAR
-- distance      INT

-- Sample Input:
-- source    destination    distance
-- A         B             100
-- B         A             100
-- B         C             150
-- C         B             150

-- Method 1: Using ROW_NUMBER
WITH cte AS (
    SELECT 
        *,
        ROW_NUMBER() OVER() AS rn
    FROM src_dest_distance
)
SELECT 
    t1.source,
    t1.destination,
    t1.distance
FROM cte t1
JOIN cte t2 
    ON t1.rn < t2.rn
    AND t1.source = t2.destination
    AND t1.destination = t2.source;

-- Method 2: Using Source-Destination Comparison
SELECT DISTINCT
    CASE 
        WHEN source < destination THEN source 
        ELSE destination 
    END AS source,
    CASE 
        WHEN source < destination THEN destination 
        ELSE source 
    END AS destination,
    distance
FROM src_dest_distance;

-- Expected Output:
-- source    destination    distance
-- A         B             100
-- B         C             150

/* Performance Optimizations:
1. Efficient ROW_NUMBER for unique identification
2. Smart join conditions
3. Consider index on (source, destination)
4. Multiple implementation approaches
5. Optimal duplicate elimination
*/
