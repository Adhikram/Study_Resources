/*
Problem: Track Cumulative Sales Since Last Product Restocking
- Calculate running total of sales after most recent restock date
- Group by product and order chronologically
- Show product names with their cumulative sales
*/

-- Input Tables Structure:
-- products
-- product_id    INT
-- product_name  VARCHAR

-- restocking
-- product_id    INT  
-- restock_date  DATE

-- sales
-- product_id    INT
-- date         DATE
-- sold_count   INT

-- Sample Input:
-- products
-- product_id    product_name
-- 1            iPhone
-- 2            iPad

-- restocking
-- product_id    restock_date
-- 1            2023-01-01
-- 2            2023-01-15

-- sales
-- product_id    date         sold_count
-- 1            2023-01-02    5
-- 1            2023-01-03    3
-- 2            2023-01-16    2

-- Get latest restock date per product
WITH latest_restock AS (
    SELECT 
        product_id,
        MAX(restock_date) AS max_restock_date
    FROM restocking
    GROUP BY product_id
),

-- Filter sales after last restock
filtered_sales AS (
    SELECT s.*
    FROM sales s
    INNER JOIN latest_restock lr 
        ON s.product_id = lr.product_id
    WHERE s.date >= lr.max_restock_date
)

-- Calculate running sales totals
SELECT 
    p.product_name,
    fs.date,
    SUM(fs.sold_count) OVER (
        PARTITION BY fs.product_id
        ORDER BY fs.date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_sales
FROM filtered_sales fs
INNER JOIN products p 
    ON fs.product_id = p.product_id
ORDER BY 
    fs.product_id,
    fs.date;

-- Expected Output:
-- product_name    date         cumulative_sales
-- iPhone         2023-01-02    5
-- iPhone         2023-01-03    8
-- iPad          2023-01-16    2

/* Performance Optimizations:
1. Used CTEs for logical separation
2. Efficient JOIN order
3. Consider indexes on:
   - restocking(product_id, restock_date)
   - sales(product_id, date)
4. Partitioned window function by product
5. Optimized sort order
*/
