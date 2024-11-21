/*
Problem: Track User Session Changes
- Monitor changes in user onboarding status
- Track visibility and type changes
- Identify session start and end times
*/

-- Input Table Structure:
-- logs
-- id                INT
-- onboarding_status VARCHAR
-- is_visible        BOOLEAN
-- type             VARCHAR
-- timestamp        TIMESTAMP

-- Sample Input:
-- id    onboarding_status    is_visible    type    timestamp
-- 1     started             true          web     2023-01-01 10:00:00
-- 1     completed           true          web     2023-01-01 10:30:00
-- 2     started             true          mobile  2023-01-01 11:00:00

-- Track session changes with window functions
WITH session_logs AS (
    SELECT 
        id,  
        onboarding_status,  
        is_visible,
        type,
        timestamp,
        LAG(timestamp) OVER (
            PARTITION BY id, onboarding_status, is_visible, type 
            ORDER BY timestamp
        ) AS session_change_start,
        LAG(timestamp) OVER (
            PARTITION BY id 
            ORDER BY timestamp
        ) AS prev_start
    FROM logs 
    GROUP BY 
        id, onboarding_status, is_visible, type, timestamp
),

-- Identify session start timestamps
session_start AS (
    SELECT 
        id,  
        onboarding_status,  
        is_visible,
        type,
        CASE 
            WHEN session_change_start IS NULL 
            OR session_change_start != prev_start 
            THEN timestamp 
            ELSE NULL 
        END AS begin_timestamp
    FROM session_logs
)

-- Calculate session durations
SELECT 
    id,
    onboarding_status,
    is_visible,
    type,
    begin_timestamp, 
    LEAD(begin_timestamp) OVER (
        PARTITION BY id 
        ORDER BY begin_timestamp
    ) AS end_timestamp 
FROM session_start
WHERE begin_timestamp IS NOT NULL;

/* Performance Optimizations:
1. Efficient window functions for sequence analysis
2. Smart partitioning for accurate session tracking
3. Consider indexes on (id, timestamp)
4. Minimal data scanning with targeted GROUP BY
5. Optimal session boundary detection
*/
