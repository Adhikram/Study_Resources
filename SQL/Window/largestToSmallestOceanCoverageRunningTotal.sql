-- need a running total of total ocean coverage across the world, largest to smallest
select name,
    type,
    square_km,
    sum(square_km) over (
        partition by type
        order by square_km desc rows between 1 preceding and 1 following
    ) as tot
from water
order by square_km desc;
-- Explanation
-- The sum of the square_km column is calculated for each type of water body
-- (ocean, sea, lake, etc) in descending order of square_km.
-- Output
-- name      type  square_km  tot
-- Pacific   ocean 165250000  165250000
-- Atlantic  ocean 106460000  271710000
-- Indian    ocean 73556000   345316000
-- Southern  ocean 20000000   365316000
-- Arctic    ocean 14056000   14056000