/*
Problem: Comprehensive Date Operations Guide
- Demonstrate all major date operations
- Show practical business applications
- Include performance optimizations
*/

-- 1. Date Intervals and Ranges
SELECT 
    current_date AS today,
    current_date + INTERVAL '1 day' AS tomorrow,
    current_date - INTERVAL '1 week' AS last_week,
    current_date + INTERVAL '1 month' AS next_month,
    current_date BETWEEN 
        DATE_TRUNC('month', current_date) 
        AND (DATE_TRUNC('month', current_date) + INTERVAL '1 month' - INTERVAL '1 day') AS is_current_month;

-- 2. Rolling Date Windows
WITH date_series AS (
    SELECT generate_series(
        current_date - INTERVAL '30 days',
        current_date,
        '1 day'::interval
    ) AS date
)
SELECT 
    date,
    COUNT(*) OVER (
        ORDER BY date 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_7_day_count;

-- 3. Business Days Calculation
WITH RECURSIVE business_days AS (
    SELECT current_date AS date
    UNION ALL
    SELECT date + 1
    FROM business_days
    WHERE date + 1 <= current_date + INTERVAL '30 days'
)
SELECT date
FROM business_days
WHERE EXTRACT(DOW FROM date) NOT IN (0, 6);

-- 4. Fiscal Year Calculations
SELECT 
    CASE 
        WHEN EXTRACT(MONTH FROM current_date) >= 7 
        THEN DATE_TRUNC('year', current_date) + INTERVAL '6 months'
        ELSE DATE_TRUNC('year', current_date) - INTERVAL '6 months'
    END AS fiscal_year_start;

-- 5. Time Zone Handling
SELECT 
    current_timestamp AS server_time,
    current_timestamp AT TIME ZONE 'UTC' AS utc_time,
    current_timestamp AT TIME ZONE 'America/New_York' AS est_time,
    current_timestamp AT TIME ZONE 'Asia/Tokyo' AS japan_time;

/* Performance Optimizations:
1. Use appropriate indexes for date columns
2. Leverage partitioning for large date ranges
3. Cache frequently used calculations
4. Consider materialized views for complex date operations
5. Optimize timezone conversions
*/
