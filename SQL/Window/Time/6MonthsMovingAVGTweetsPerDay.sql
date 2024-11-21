/*
Problem: Calculate 6-Month Moving Average of Daily Tweets
- Track tweet volume trends
- Calculate rolling 6-month average
- Display results in millions
*/

-- Input Table Structure:
-- tweets
-- dte              DATE
-- tweet_millions   DECIMAL

-- Sample Input:
-- dte          tweet_millions
-- 2019-01-01   0.1
-- 2019-02-01   0.2
-- 2019-03-01   0.3
-- 2019-04-01   0.4
-- 2019-05-01   0.5

SELECT 
    dte,
    tweet_millions,
    AVG(tweet_millions) OVER (
        ORDER BY dte 
        RANGE BETWEEN INTERVAL '6' MONTH PRECEDING 
        AND CURRENT ROW
    ) AS moving_average
FROM tweets
ORDER BY dte;

-- Expected Output:
-- dte          tweet_millions    moving_average
-- 2019-01-01   0.1              0.1
-- 2019-02-01   0.2              0.15
-- 2019-03-01   0.3              0.2
-- 2019-04-01   0.4              0.25
-- 2019-05-01   0.5              0.3

/* Performance Optimizations:
1. Used RANGE instead of ROWS for date-based windows
2. Efficient interval-based window frame
3. Consider index on (dte, tweet_millions)
4. Single pass calculation
5. Minimal columns in result set
*/
