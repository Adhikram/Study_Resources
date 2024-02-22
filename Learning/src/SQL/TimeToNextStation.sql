-- Time To next Station
SELECT train_id,
    station,
    time as "station_time",
    lead(time) OVER (
        PARTITION BY train_id
        ORDER BY time
    ) - time AS time_to_next_station
FROM train_schedule;

-- Input
-- train_schedule table
-- train_id  station  time
-- 1         A        09:00
-- 1         B        09:15
-- 1         C        09:45
-- 2         A        09:00
-- 2         B        09:15
-- 2         C        09:45

-- Output
-- train_id  station  station_time  time_to_next_station
-- 1         A        09:00         00:15
-- 1         B        09:15         00:30
-- 1         C        09:45         00:00
-- 2         A        09:00         00:15
-- 2         B        09:15         00:30