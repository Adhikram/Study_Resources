/*
Problem: DoorDash New User Experience Analysis
- Calculate percentage of bad delivery experiences for new users
- Focus on first 14 days after signup in June 2022
- Round result to 2 decimal places
*/

-- Input Tables Structure:
-- orders
-- order_id              INT
-- customer_id           INT
-- trip_id              INT
-- status               VARCHAR
-- order_timestamp      TIMESTAMP

-- trips
-- dasher_id            INT
-- trip_id              INT
-- estimated_delivery   TIMESTAMP
-- actual_delivery      TIMESTAMP

-- customers
-- customer_id          INT
-- signup_timestamp     TIMESTAMP

-- Sample Input:
-- orders
-- order_id    customer_id    trip_id    status                order_timestamp
-- 727424      8472          100463     completed successfully 2022-06-05 09:12:00
-- 242513      2341          100482     completed incorrectly  2022-06-05 14:40:00

-- Identify June 2022 new customers
WITH june_customers AS (
    SELECT 
        customer_id,
        signup_timestamp,
        signup_timestamp + INTERVAL '14 days' AS first_14_days
    FROM customers
    WHERE DATE_TRUNC('month', signup_timestamp) = '2022-06-01'
),

-- Calculate bad experiences
bad_experiences AS (
    SELECT 
        o.order_id,
        o.customer_id,
        CASE WHEN 
            o.status IN ('completed incorrectly', 'never received')
            OR (t.actual_delivery_timestamp - o.order_timestamp) > INTERVAL '30 minutes'
        THEN 1 ELSE 0 END AS is_bad_experience
    FROM orders o
    LEFT JOIN trips t 
        ON o.trip_id = t.trip_id
    INNER JOIN june_customers jc 
        ON o.customer_id = jc.customer_id
    WHERE 
        o.order_timestamp BETWEEN jc.signup_timestamp AND jc.first_14_days
)

-- Calculate final percentage
SELECT 
    ROUND(
        100.0 * SUM(is_bad_experience)::DECIMAL / COUNT(*)::DECIMAL,
        2
    ) AS bad_experience_pct
FROM bad_experiences;

-- Expected Output:
-- bad_experience_pct
-- 75.00

/* Performance Optimizations:
1. Used CTEs for logical separation
2. Early date filtering
3. Efficient JOIN sequence
4. Consider indexes on:
   - customers(signup_timestamp)
   - orders(customer_id, order_timestamp)
   - trips(trip_id, actual_delivery_timestamp)
5. Type casting for accurate percentage calculation
*/
