/*
Problem: Calculate AWS Fleet Server Uptime
- Track total running time across server fleet
- Convert to full days
- Handle start/stop session pairs
*/

-- Input Table Structure:
-- server_utilization
-- server_id        INT
-- session_status   VARCHAR ('start', 'stop')
-- status_time      TIMESTAMP

-- Sample Input:
-- server_id    session_status    status_time
-- 1           start             2023-01-01 10:00:00
-- 1           stop              2023-01-02 15:00:00
-- 2           start             2023-01-01 11:00:00

-- Method 1: Using LEAD for Session Pairs
WITH running_time AS (
    SELECT
        server_id,
        session_status,
        status_time AS start_time,
        LEAD(status_time) OVER (
            PARTITION BY server_id
            ORDER BY status_time
        ) AS stop_time
    FROM server_utilization
)

SELECT
    DATE_PART('days', 
        JUSTIFY_HOURS(
            SUM(stop_time - start_time)
        )
    ) AS total_uptime_days
FROM running_time
WHERE 
    session_status = 'start'
    AND stop_time IS NOT NULL;

-- Method 2: Using Self-Join /// will not work
SELECT 
    DATE_PART('days',
        SUM(stop.status_time - start.status_time)
    ) AS total_uptime_days
FROM server_utilization start
JOIN server_utilization stop
    ON start.server_id = stop.server_id
    AND start.session_status = 'start'
    AND stop.session_status = 'stop'
    AND stop.status_time > start.status_time;

-- Expected Output:
-- total_uptime_days
-- 45

/* Performance Optimizations:
1. Used window functions for efficient pairing
2. Optimized date calculations
3. Consider indexes on (server_id, status_time, session_status)
4. Multiple implementation options for different data volumes
5. Efficient filtering of incomplete sessions
*/
