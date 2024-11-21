/*
Problem: Calculate Time Between Train Stations
- Track time to next station for each train
- Group by train routes
- Show station arrival times
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
-- 2           A          09:00
-- 2           B          09:15

-- Method 1: Using LEAD Function
SELECT 
    train_id,
    station,
    time AS station_time,
    LEAD(time) OVER (
        PARTITION BY train_id
        ORDER BY time
    ) - time AS time_to_next_station
FROM train_schedule;

-- Method 2: Using Self-Join
SELECT 
    t1.train_id,
    t1.station,
    t1.time AS station_time,
    MIN(t2.time - t1.time) AS time_to_next_station
FROM train_schedule t1
LEFT JOIN train_schedule t2 
    ON t1.train_id = t2.train_id
    AND t1.time < t2.time
GROUP BY 
    t1.train_id,
    t1.station,
    t1.time
ORDER BY 
    t1.train_id,
    t1.time;

-- Expected Output:
-- train_id  station  station_time  time_to_next_station
-- 1         A        09:00         00:15
-- 1         B        09:15         00:30
-- 1         C        09:45         NULL
-- 2         A        09:00         00:15
-- 2         B        09:15         00:30

/* Performance Optimizations:
1. LEAD function for efficient sequential access
2. Optimal partitioning by train_id
3. Consider index on (train_id, time)
4. Multiple implementation approaches
5. Efficient ordering strategy
*/
