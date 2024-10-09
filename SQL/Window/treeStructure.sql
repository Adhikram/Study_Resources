SELECT 
    id,
    CASE 
        WHEN parent_id IS NULL THEN 'Root'
        WHEN id NOT IN (SELECT DISTINCT parent_id FROM tree WHERE parent_id IS NOT NULL) THEN 'Leaf'
        ELSE 'Inner'
    END AS node_type
FROM tree;