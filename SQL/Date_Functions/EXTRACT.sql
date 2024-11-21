/*
Problem: Demonstrate EXTRACT Function Applications
- Extract specific parts from dates
- Handle different time components
- Support time-based analytics
*/

-- Input Table Structure:
-- transactions
-- tx_id        INT
-- tx_timestamp TIMESTAMP
-- amount       DECIMAL

-- Basic Time Component Extraction
SELECT 
    tx_timestamp,
    EXTRACT(YEAR FROM tx_timestamp) AS year,
    EXTRACT(MONTH FROM tx_timestamp) AS month,
    EXTRACT(DAY FROM tx_timestamp) AS day,
    EXTRACT(HOUR FROM tx_timestamp) AS hour,
    EXTRACT(MINUTE FROM tx_timestamp) AS minute,
    EXTRACT(SECOND FROM tx_timestamp) AS second
FROM transactions;

-- Business Analytics
SELECT 
    EXTRACT(HOUR FROM tx_timestamp) AS hour_of_day,
    COUNT(*) AS transaction_count,
    AVG(amount) AS avg_amount
FROM transactions
GROUP BY EXTRACT(HOUR FROM tx_timestamp)
ORDER BY hour_of_day;

-- Time Difference Calculations
SELECT 
    tx_timestamp,
    EXTRACT(EPOCH FROM (tx_timestamp - lag_timestamp)) AS seconds_since_last,
    EXTRACT(DAYS FROM (tx_timestamp - lag_timestamp)) AS days_difference
FROM (
    SELECT 
        tx_timestamp,
        LAG(tx_timestamp) OVER (ORDER BY tx_timestamp) AS lag_timestamp
    FROM transactions
);

-- Expected Output:
-- hour_of_day    transaction_count    avg_amount
-- 9              100                  150.25
-- 10             150                  175.50
-- 11             200                  200.75

/* Performance Optimizations:
1. Use for efficient date part filtering
2. Index-friendly for specific components
3. Optimize for common extractions
4. Consider materialized views for frequent analytics
5. Combine with appropriate partitioning strategy
*/
