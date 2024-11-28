/*
Problem: Track Merchant Account Balance
- Calculate daily cumulative balance
- Reset balance at month end
- Handle deposits and withdrawals
*/

-- Input Table Structure:
-- merchant_transactions
-- transaction_id         INT
-- transaction_date      TIMESTAMP
-- type                  VARCHAR ('deposit', 'withdrawal')
-- amount               DECIMAL

-- Sample Input:
-- transaction_id    transaction_date    type        amount
-- 1                2023-01-01          deposit     1000
-- 2                2023-01-02          withdrawal  500
-- 3                2023-01-03          deposit     750

-- Calculate daily balances within months
WITH daily_balances AS (
    SELECT
        DATE(transaction_date) AS transaction_day,
        DATE_FORMAT(transaction_date, '%Y-%m-01') AS transaction_month,
        SUM(CASE 
            WHEN type = 'deposit' THEN amount
            WHEN type = 'withdrawal' THEN -amount
            ELSE 0
        END) AS daily_balance
    FROM merchant_transactions
    GROUP BY
        DATE(transaction_date),
        DATE_FORMAT(transaction_date, '%Y-%m-01')
)

-- Calculate running totals with monthly reset
SELECT
    transaction_day,
    SUM(daily_balance) OVER (
        PARTITION BY transaction_month
        ORDER BY transaction_day
    ) AS cumulative_balance
FROM daily_balances
ORDER BY transaction_day;

-- Expected Output:
-- transaction_day    cumulative_balance
-- 2023-01-01        1000
-- 2023-01-02        500
-- 2023-01-03        1250

/* Performance Optimizations:
1. Used DATE for efficient date grouping
2. Partitioned by month for balance reset
3. Consider index on (transaction_date, type)
4. Efficient CASE statement for balance calculation
5. Optimized window frame clause
*/