/*
Problem: Track Train Station Arrival Times
- Calculate elapsed time between stations
- Measure time to next station
- Track cumulative journey time
*/

-- Input Table Structure:
-- train_schedule
-- train_id    INT
-- station     VARCHAR
-- time        TIMESTAMP

-- Sample Input:
-- train_id    station    time
-- 1           A          09:00
-- 1           B          09:15
-- 1           C          09:45

-- Method 1: Using LAG and LEAD
SELECT 
    train_id,
    station,
    time AS station_time,
    -- Calculate elapsed time from previous station
    EXTRACT(
        EPOCH FROM (
            time - LAG(time) OVER (
                PARTITION BY train_id
                ORDER BY time
            )
        )
    ) AS elapsed_travel_time,
    -- Calculate time to next station
    EXTRACT(
        EPOCH FROM (
            LEAD(time) OVER (
                PARTITION BY train_id
                ORDER BY time
            ) - time
        )
    ) AS time_to_next_station
FROM train_schedule;

-- Method 2: Using Window Functions with Running Total
SELECT 
    train_id,
    station,
    time AS station_time,
    EXTRACT(
        EPOCH FROM (
            time - MIN(time) OVER (
                PARTITION BY train_id
                ORDER BY time
                ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
            )
        )
    ) AS total_journey_time,
    EXTRACT(
        EPOCH FROM (
            LEAD(time) OVER (
                PARTITION BY train_id
                ORDER BY time
            ) - time
        )
    ) AS next_station_time
FROM train_schedule;

-- Expected Output:
-- train_id  station  station_time  elapsed_time  time_to_next
-- 1         A        09:00         0            900
-- 1         B        09:15         900          1800
-- 1         C        09:45         1800         NULL

/* Performance Optimizations:
1. Efficient window functions for time calculations
2. Single scan per analysis type
3. Consider index on (train_id, time)
4. Optimized EXTRACT usage
5. Multiple implementation options for different needs
*/
