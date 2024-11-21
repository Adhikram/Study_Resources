/*
Problem: Classify Tree Nodes in Hierarchical Structure
- Identify Root, Leaf, and Inner nodes
- Handle parent-child relationships
- Maintain hierarchical integrity
*/

-- Input Table Structure:
-- tree
-- id          INT
-- parent_id   INT (nullable)

-- Sample Input:
-- id    parent_id
-- 1     NULL
-- 2     1
-- 3     1
-- 4     2

-- Method 1: Using CTEs for Node Classification
WITH node_types AS (
    SELECT DISTINCT parent_id 
    FROM tree 
    WHERE parent_id IS NOT NULL
)
SELECT 
    t.id,
    CASE 
        WHEN t.parent_id IS NULL THEN 'Root'      -- No parent = Root
        WHEN t.id NOT IN (                        -- No children = Leaf
            SELECT parent_id 
            FROM node_types
        ) THEN 'Leaf'
        ELSE 'Inner'                              -- Has both = Inner
    END AS node_type
FROM tree t
ORDER BY t.id;

-- Method 2: Using Subqueries
SELECT 
    id,
    CASE 
        WHEN parent_id IS NULL THEN 'Root'
        WHEN id NOT IN (
            SELECT DISTINCT parent_id 
            FROM tree 
            WHERE parent_id IS NOT NULL
        ) THEN 'Leaf'
        ELSE 'Inner'
    END AS node_type
FROM tree
ORDER BY id;

-- Expected Output:
-- id    node_type
-- 1     Root
-- 2     Inner
-- 3     Leaf
-- 4     Leaf

/* Performance Optimizations:
1. Efficient CTE for parent identification
2. Smart NULL handling
3. Consider indexes on (id, parent_id)
4. Multiple implementation approaches
5. Optimal sort order
*/
