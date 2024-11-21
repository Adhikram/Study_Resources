/*
Problem: Analyze Life Expectancy Trends
- Compare life expectancy with 5-year ranges
- Show first and last values in range window
- Track historical UK life expectancy changes
*/

-- Input Table Structure:
-- life_expectancy
-- recorded_year    INT
-- age             INT

-- Sample Input:
-- recorded_year    age
-- 1543            33
-- 1548            39
-- 1553            40
-- 1558            43

-- Method 1: Using FIRST_VALUE/LAST_VALUE
SELECT 
    recorded_year,
    age,
    FIRST_VALUE(age) OVER (
        ORDER BY recorded_year
        RANGE BETWEEN INTERVAL '5' YEAR PRECEDING 
        AND INTERVAL '5' YEAR FOLLOWING
    ) AS first_value_in_range,
    LAST_VALUE(age) OVER (
        ORDER BY recorded_year
        RANGE BETWEEN INTERVAL '5' YEAR PRECEDING 
        AND INTERVAL '5' YEAR FOLLOWING
    ) AS last_value_in_range
FROM life_expectancy;

-- Method 2: Using Range Boundaries
WITH range_values AS (
    SELECT 
        recorded_year,
        age,
        MIN(recorded_year) OVER (
            ORDER BY recorded_year
            RANGE BETWEEN INTERVAL '5' YEAR PRECEDING 
            AND INTERVAL '5' YEAR FOLLOWING
        ) AS range_start,
        MAX(recorded_year) OVER (
            ORDER BY recorded_year
            RANGE BETWEEN INTERVAL '5' YEAR PRECEDING 
            AND INTERVAL '5' YEAR FOLLOWING
        ) AS range_end
    FROM life_expectancy
)
SELECT 
    recorded_year,
    age,
    MIN(age) AS first_value_in_range,
    MAX(age) AS last_value_in_range
FROM range_values
GROUP BY recorded_year, age;

-- Expected Output:
-- recorded_year    age    first_value    last_value
-- 1543            33     33             33
-- 1548            39     33             39
-- 1553            40     33             40
-- 1558            43     33             43

/* Performance Optimizations:
1. Used RANGE for time-based windows
2. Efficient interval calculations
3. Consider index on (recorded_year, age)
4. Multiple approach options for different data sizes
5. Optimized window frame definitions
*/
