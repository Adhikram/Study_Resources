/*
Problem: Apple Purchase Pattern Analysis
- Calculate percentage of iPhone buyers who bought AirPods next
- Track sequential product purchases
- Return rounded percentage with no decimals
*/

-- Input Table Structure:
-- transactions
-- transaction_id         INT
-- customer_id           INT
-- product_name          VARCHAR
-- transaction_timestamp TIMESTAMP

-- Sample Input:
-- transaction_id    customer_id    product_name    transaction_timestamp
-- 1                101            iPhone          2022-08-08 00:00:00
-- 2                101            AirPods         2022-08-08 00:00:00
-- 5                301            iPhone          2022-09-05 00:00:00

-- Track sequential purchases
WITH lag_products AS (
    SELECT
        customer_id,
        product_name,
        LAG(product_name) OVER (
            PARTITION BY customer_id
            ORDER BY transaction_timestamp
        ) AS prev_prod
    FROM transactions
    GROUP BY
        customer_id,
        product_name,
        transaction_timestamp
),

-- Identify iPhone-to-AirPods buyers
interested_users AS (
    SELECT 
        customer_id AS airpod_iphone_buyers
    FROM lag_products
    WHERE 
        LOWER(product_name) = 'airpods'
        AND LOWER(prev_prod) = 'iphone'
    GROUP BY customer_id
)

-- Calculate final percentage
SELECT
    ROUND(
        COUNT(DISTINCT iu.airpod_iphone_buyers)::DECIMAL
        / COUNT(DISTINCT transactions.customer_id)::DECIMAL
        * 100, 
        0
    ) AS follow_up_percentage
FROM transactions
LEFT JOIN interested_users AS iu
    ON iu.airpod_iphone_buyers = transactions.customer_id;

-- Expected Output:
-- follow_up_percentage
-- 50

/* Performance Optimizations:
1. Used CTEs for better query organization
2. Efficient window function for sequence analysis
3. Case-insensitive product matching
4. Consider index on (customer_id, transaction_timestamp)
5. DISTINCT counts to prevent duplicates
*/
