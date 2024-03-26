-- 1. First, create a CTE to get the latest restocking date for each product
WITH latest_restock AS (
    SELECT product_id,
        MAX(restock_date) AS max_restock_date
    FROM restocking
    GROUP BY product_id
),
-- 2. Then, create another CTE to get the sales that occurred after the latest restocking
filtered_sales AS (
    SELECT s.*
    FROM sales s
        JOIN latest_restock lr ON s.product_id = lr.product_id
    WHERE s.date >= lr.max_restock_date
) -- 3. Finally, calculate the cumulative sum of sales since the latest restocking
SELECT p.product_name,
    fs.date,
    SUM(fs.sold_count) OVER (
        PARTITION BY fs.product_id
        ORDER BY fs.date
    ) AS sales_since_last_restock
FROM filtered_sales fs
    JOIN products p ON fs.product_id = p.product_id
ORDER BY fs.product_id,
    fs.date;