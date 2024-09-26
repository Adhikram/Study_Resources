-- SQL Time-Related Hacks Cheat Sheet

-- 1. Get the current date and time
SELECT CURRENT_TIMESTAMP;

-- 2. Extract parts of a date
SELECT 
    EXTRACT(YEAR FROM CURRENT_TIMESTAMP) AS year,
    EXTRACT(MONTH FROM CURRENT_TIMESTAMP) AS month,
    EXTRACT(DAY FROM CURRENT_TIMESTAMP) AS day,
    EXTRACT(HOUR FROM CURRENT_TIMESTAMP) AS hour,
    EXTRACT(MINUTE FROM CURRENT_TIMESTAMP) AS minute,
    EXTRACT(SECOND FROM CURRENT_TIMESTAMP) AS second;

-- 3. Add or subtract intervals from a date
SELECT 
    CURRENT_TIMESTAMP + INTERVAL '1 day' AS tomorrow,
    CURRENT_TIMESTAMP - INTERVAL '1 day' AS yesterday,
    CURRENT_TIMESTAMP + INTERVAL '1 month' AS next_month,
    CURRENT_TIMESTAMP - INTERVAL '1 month' AS last_month;

-- 4. Calculate the difference between two dates
SELECT 
    AGE(TIMESTAMP '2023-12-31', TIMESTAMP '2023-01-01') AS age_difference,
    DATE_PART('day', TIMESTAMP '2023-12-31' - TIMESTAMP '2023-01-01') AS days_difference;

-- 5. Format a date
SELECT 
    TO_CHAR(CURRENT_TIMESTAMP, 'YYYY-MM-DD') AS formatted_date,
    TO_CHAR(CURRENT_TIMESTAMP, 'HH24:MI:SS') AS formatted_time;

-- 6. Find the first and last day of the month
SELECT 
    DATE_TRUNC('month', CURRENT_TIMESTAMP) AS first_day_of_month,
    (DATE_TRUNC('month', CURRENT_TIMESTAMP) + INTERVAL '1 month - 1 day')::DATE AS last_day_of_month;

-- 7. Use window functions for time-based calculations
WITH session_logs AS (
    SELECT 
        id,  
        onboarding_status,  
        is_visible,
        type,
        timestamp,
        LAG(timestamp) OVER (PARTITION BY id, onboarding_status, is_visible, type ORDER BY timestamp) AS session_change_start,
        LAG(timestamp) OVER (PARTITION BY id ORDER BY timestamp) AS prev_start
    FROM logs 
    GROUP BY id, onboarding_status, is_visible, type, timestamp
),
session_start AS (
    SELECT 
        id,  
        onboarding_status,  
        is_visible,
        type,
        CASE 
            WHEN session_change_start IS NULL OR session_change_start != prev_start 
            THEN timestamp 
            ELSE NULL 
        END AS begin_timestamp
    FROM session_logs
)
SELECT 
    id,
    onboarding_status,
    is_visible,
    type,
    begin_timestamp, 
    LEAD(begin_timestamp) OVER (PARTITION BY id ORDER BY begin_timestamp) AS end_timestamp 
FROM session_start
WHERE begin_timestamp IS NOT NULL;

-- 8. Generate a series of dates
SELECT 
    GENERATE_SERIES(
        TIMESTAMP '2023-01-01', 
        TIMESTAMP '2023-12-31', 
        INTERVAL '1 month'
    ) AS month_series;

-- 9. Find overlapping date ranges
WITH date_ranges AS (
    SELECT 
        id, 
        start_date, 
        end_date,
        LEAD(start_date) OVER (PARTITION BY id ORDER BY start_date) AS next_start_date
    FROM date_table
)
SELECT 
    id, 
    start_date, 
    end_date, 
    next_start_date
FROM date_ranges
WHERE end_date > next_start_date;

-- 10. Calculate running totals with dates
SELECT 
    id, 
    date, 
    amount,
    SUM(amount) OVER (PARTITION BY id ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM transactions;
