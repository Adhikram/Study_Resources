/*
Problem: Demonstrate DATE_PART Function Usage
- Extract specific date components
- Enable date-based calculations
- Support time interval analysis
*/

-- Input Table Structure:
-- events
-- event_id      INT
-- event_time    TIMESTAMP
-- duration      INTERVAL

-- Basic Date Part Extraction
SELECT 
    event_time,
    DATE_PART('year', event_time) AS year,
    DATE_PART('month', event_time) AS month_num,
    DATE_PART('day', event_time) AS day_num,
    DATE_PART('dow', event_time) AS day_of_week,
    DATE_PART('hour', event_time) AS hour_24
FROM events;

-- Interval Calculations
SELECT 
    duration,
    DATE_PART('hour', duration) AS hours,
    DATE_PART('minute', duration) AS minutes,
    DATE_PART('second', duration) AS seconds
FROM events;

-- Business Analytics
SELECT 
    DATE_PART('hour', event_time) AS business_hour,
    COUNT(*) AS event_count,
    SUM(DATE_PART('minute', duration)) AS total_minutes
FROM events
WHERE DATE_PART('dow', event_time) BETWEEN 1 AND 5  -- Weekdays only
GROUP BY DATE_PART('hour', event_time)
ORDER BY business_hour;

-- Expected Output:
-- business_hour    event_count    total_minutes
-- 9               45             2700
-- 10              60             3600
-- 11              75             4500

/* Performance Optimizations:
1. Efficient for component-based filtering
2. Use for business hour analysis
3. Optimize with appropriate indexes
4. Consider time zone implications
5. Combine with partitioning strategies
*/
