-- Approach 1: Using NTH_VALUE (Original)
SELECT 
    trip_date,
    trip_count,
    NTH_VALUE(trip_count, 2) OVER w AS second_lowest,
    NTH_VALUE(trip_count, 2) OVER (
        ORDER BY trip_count DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS second_highest
FROM trips
WINDOW w AS (
    ORDER BY trip_count
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
);

-- Approach 2: Using DENSE_RANK
WITH ranked_trips AS (
    SELECT 
        trip_date,
        trip_count,
        DENSE_RANK() OVER (ORDER BY trip_count) AS low_rank,
        DENSE_RANK() OVER (ORDER BY trip_count DESC) AS high_rank
    FROM trips
)
SELECT 
    trip_date,
    trip_count,
    MAX(CASE WHEN low_rank = 2 THEN trip_count END) OVER () AS second_lowest,
    MAX(CASE WHEN high_rank = 2 THEN trip_count END) OVER () AS second_highest
FROM ranked_trips;

-- Approach 3: Using LAG/LEAD
WITH distinct_counts AS (
    SELECT DISTINCT trip_count
    FROM trips
    ORDER BY trip_count
)
SELECT 
    t.trip_date,
    t.trip_count,
    MIN(dc2.trip_count) AS second_lowest,
    MAX(dc2.trip_count) AS second_highest
FROM trips t
CROSS JOIN (
    SELECT 
        trip_count
    FROM distinct_counts
    OFFSET 1 LIMIT 1
) dc2
GROUP BY t.trip_date, t.trip_count;

/* Each approach has its advantages:
1. NTH_VALUE: Most readable, direct approach
2. DENSE_RANK: Better for finding multiple rankings
3. LAG/LEAD: Efficient for sequential analysis
*/
