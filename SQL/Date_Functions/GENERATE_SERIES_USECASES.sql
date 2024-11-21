/*
Problem: Comprehensive Guide to GENERATE_SERIES Applications
*/

-- 1. Date Range Analysis
WITH date_range AS (
    SELECT generate_series(
        '2024-01-01'::date,
        '2024-12-31'::date,
        '1 day'::interval
    ) AS date
)
SELECT 
    date,
    EXTRACT(dow FROM date) AS day_of_week,
    CASE WHEN EXTRACT(dow FROM date) IN (0, 6) THEN 'Weekend' ELSE 'Weekday' END AS day_type;

-- 2. Time Slot Generation for Appointments
SELECT generate_series(
    '2024-01-20 09:00:00'::timestamp,
    '2024-01-20 17:00:00'::timestamp,
    '30 minutes'
) AS appointment_slots;

-- 3. Missing Data Detection
WITH all_dates AS (
    SELECT generate_series(
        (SELECT MIN(transaction_date) FROM sales),
        (SELECT MAX(transaction_date) FROM sales),
        '1 day'::interval
    ) AS date
)
SELECT 
    date
FROM all_dates a
LEFT JOIN sales s ON s.transaction_date = a.date
WHERE s.transaction_date IS NULL;

-- 4. Sales Forecasting Template
SELECT 
    generate_series(
        CURRENT_DATE,
        CURRENT_DATE + interval '12 months',
        '1 month'
    ) AS forecast_month;

-- 5. Hourly Performance Metrics
WITH hours AS (
    SELECT generate_series(
        date_trunc('hour', CURRENT_TIMESTAMP - interval '24 hours'),
        date_trunc('hour', CURRENT_TIMESTAMP),
        '1 hour'
    ) AS hour
)
SELECT 
    hour,
    COUNT(event_id) AS events
FROM hours
LEFT JOIN events ON date_trunc('hour', event_timestamp) = hour
GROUP BY hour;

-- 6. Custom Calendar with Fiscal Periods
SELECT 
    generate_series(
        date_trunc('year', CURRENT_DATE),
        date_trunc('year', CURRENT_DATE) + interval '1 year',
        '3 months'
    ) AS fiscal_quarter;

-- 7. Temperature Reading Simulation
SELECT 
    generate_series(
        NOW(),
        NOW() + interval '1 day',
        '1 hour'
    ) AS reading_time,
    random() * 10 + 20 AS temperature;

-- 8. Server Uptime Slots
SELECT generate_series(
    NOW(),
    NOW() + interval '7 days',
    '1 hour'
) AS health_check_schedule;

-- 9. Recurring Event Schedule
SELECT generate_series(
    '2024-01-01'::timestamp,
    '2024-12-31'::timestamp,
    '2 weeks'
) AS biweekly_meetings;

-- 10. Load Testing Timestamps
SELECT generate_series(
    NOW(),
    NOW() + interval '1 minute',
    '100 milliseconds'
) AS load_test_times;

/* Use Cases Benefits:
1. Gap Analysis in Time Series
2. Schedule Generation
3. Data Quality Checks
4. Forecasting Templates
5. Performance Monitoring
6. Custom Calendar Creation
7. Data Simulation
8. Maintenance Scheduling
9. Event Planning
10. Testing Data Generation
*/
