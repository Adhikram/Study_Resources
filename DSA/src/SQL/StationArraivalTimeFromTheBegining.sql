-- how much time has elapsed from the train’s first stop to the current station
SELECT train_id,
    station,
    time as "station_time",
    EXTRACT(EPOCH FROM (time - min(time) OVER (
        PARTITION BY train_id
        ORDER BY time
    ))) AS elapsed_travel_time,
    EXTRACT(EPOCH FROM (lead(time) OVER (
        PARTITION BY train_id
        ORDER BY time
    ) - time)) AS time_to_next_station
FROM train_schedule;
--  Output
--  train_id  station  station_time  elapsed_travel_time  time_to_next_station
--  1         A        09:00         00:00                00:15
--  1         B        09:15         00:15                00:30
--  1         C        09:45         00:45                00:00
--  2         A        09:00         00:00                00:15
--  2         B        09:15         00:15                00:30
--  2         C        09:45         00:45                00:00
--  3         A        09:00         00:00                00:15
--  3         B        09:15         00:15                00:30
--  3         C        09:45         00:45                00:00
--  4         A        09:00         00:00                00:15