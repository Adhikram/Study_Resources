/*
Problem: Ungroup Aggregated Travel Items Data
- Convert grouped counts into individual rows
- Maintain item and ID relationships
- Generate sequential records
*/

-- Input Table Structure:
-- travel_items
-- id           INT
-- item_name    VARCHAR
-- total_count  INT

-- Sample Input:
-- id    item_name    total_count
-- 1     Bag          2
-- 2     Shoes        1
-- 3     Bag          1
-- 4     Shoes        2

-- Method 1: Using Recursive CTE
WITH RECURSIVE cte AS (
    -- Base case: First occurrence
    SELECT 
        id,
        item_name,
        total_count,
        1 AS level
    FROM travel_items
    
    UNION ALL
    
    -- Recursive case: Generate additional rows
    SELECT 
        cte.id,
        cte.item_name,
        cte.total_count - 1,
        level + 1
    FROM cte
    JOIN travel_items t 
        ON t.item_name = cte.item_name
        AND t.id = cte.id
    WHERE cte.total_count > 1
)

-- Final result ordered by ID
SELECT 
    id,
    item_name
FROM cte
ORDER BY id;

-- Method 2: Using Generate_Series
SELECT 
    id,
    item_name
FROM travel_items
CROSS JOIN generate_series(1, total_count)
ORDER BY id;

-- Expected Output:
-- id    item_name
-- 1     Bag
-- 1     Bag
-- 2     Shoes
-- 3     Bag
-- 4     Shoes
-- 4     Shoes

/* Performance Optimizations:
1. Efficient recursive CTE implementation
2. Smart join conditions
3. Consider index on (id, item_name)
4. Multiple implementation options
5. Optimal sort order
*/
