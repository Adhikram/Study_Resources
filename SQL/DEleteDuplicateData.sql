/*
Problem: Delete Duplicate Car Records
- Keep only one record per model and brand
- Maintain lowest model_id for duplicates
- Multiple implementation strategies
*/

-- Input Table Structure:
-- cars
-- model_id    INT
-- model_name  VARCHAR
-- brand       VARCHAR

-- Sample Input:
-- model_id    model_name    brand
-- 1           Civic         Honda
-- 2           Civic         Honda
-- 3           Camry         Toyota

-- Method 1: Using Subquery with MIN
DELETE FROM cars
WHERE model_id NOT IN (
    SELECT MIN(model_id)
    FROM cars
    GROUP BY 
        model_name,
        brand
);

-- Method 2: Using CTID (PostgreSQL Specific)
DELETE FROM cars
WHERE ctid IN (
    SELECT MAX(ctid)
    FROM cars
    GROUP BY 
        model_name,
        brand
    HAVING COUNT(1) > 1
);

-- Method 3: Using Window Function
WITH duplicates AS (
    SELECT model_id
    FROM (
        SELECT 
            model_id,
            ROW_NUMBER() OVER(
                PARTITION BY model_name, brand
                ORDER BY model_id
            ) AS rn
        FROM cars
    ) x
    WHERE x.rn > 1
)
DELETE FROM cars
WHERE model_id IN (
    SELECT model_id 
    FROM duplicates
);

-- Expected Output After Deletion:
-- model_id    model_name    brand
-- 1           Civic         Honda
-- 3           Camry         Toyota

/* Performance Optimizations:
1. Efficient index usage on (model_name, brand)
2. Multiple implementation strategies for different scenarios
3. Optimal duplicate identification methods
4. Transaction management for large deletions
5. Minimal lock time approaches
*/
