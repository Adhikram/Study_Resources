-- compare daily uber trips in new york city with 2nd lowest/Highest from July to September
select trip_Date,
    trip_count,
    nth_value(trip_count, 2) over(
        order by trip_count rows between unbounded preceding and unbounded following
    ) as second_lowest
    nth_value(trip_count, 2) over(
        order by trip_count desc rows between unbounded preceding and unbounded following
    ) as second_highest
from trips
order by trip_date


-- Output
-- trip_Date  trip_count  second_lowest  second_highest
-- 2019-07-01 100         100            100
-- 2019-07-02 200         100            100
-- 2019-07-03 300         100            100
-- 2019-07-04 400         100            100