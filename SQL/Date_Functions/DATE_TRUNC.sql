/*
Problem: Demonstrate DATE_TRUNC Function Usage
- Truncate dates to specific precision
- Group time-series data
- Enable time-based aggregations
*/

-- Input Table Structure:
-- sales
-- sale_id       INT
-- sale_time     TIMESTAMP
-- amount        DECIMAL

-- Basic Date Truncation
SELECT 
    sale_time,
    DATE_TRUNC('year', sale_time) AS year_start,
    DATE_TRUNC('quarter', sale_time) AS quarter_start,
    DATE_TRUNC('month', sale_time) AS month_start,
    DATE_TRUNC('week', sale_time) AS week_start,
    DATE_TRUNC('day', sale_time) AS day_start,
    DATE_TRUNC('hour', sale_time) AS hour_start
FROM sales;

-- Time-Series Analysis
SELECT 
    DATE_TRUNC('hour', sale_time) AS hourly_bucket,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_sales
FROM sales
GROUP BY DATE_TRUNC('hour', sale_time)
ORDER BY hourly_bucket;

-- Period Comparisons
SELECT 
    DATE_TRUNC('month', sale_time) AS month,
    SUM(amount) AS monthly_total,
    LAG(SUM(amount)) OVER (ORDER BY DATE_TRUNC('month', sale_time)) AS prev_month_total
FROM sales
GROUP BY DATE_TRUNC('month', sale_time);

-- Expected Output:
-- hourly_bucket           transaction_count    total_sales
-- 2024-01-20 09:00:00    50                   5000.00
-- 2024-01-20 10:00:00    75                   7500.00
-- 2024-01-20 11:00:00    100                  10000.00

/* Performance Optimizations:
1. Efficient for time-series grouping
2. Optimize with appropriate indexes
3. Use for partition boundaries
4. Combine with materialized views
5. Consider time zone handling
*/
