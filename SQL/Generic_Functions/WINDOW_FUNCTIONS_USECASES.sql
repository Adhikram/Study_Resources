/*
Problem: Advanced Window Function Applications
*/

-- 1. Sales Rankings and Analysis
SELECT 
    sales_id,
    product_name,
    amount,
    ROW_NUMBER() OVER (PARTITION BY category ORDER BY amount DESC) AS category_rank,
    DENSE_RANK() OVER (PARTITION BY category ORDER BY amount DESC) AS dense_rank,
    RANK() OVER (PARTITION BY category ORDER BY amount DESC) AS standard_rank;

-- 2. Running Totals and Moving Averages
SELECT 
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) AS running_total,
    AVG(amount) OVER (
        ORDER BY date 
        ROWS BETWEEN 3 PRECEDING AND CURRENT ROW
    ) AS moving_average;

-- 3. Employee Salary Analysis
SELECT 
    employee_id,
    department,
    salary,
    LAG(salary) OVER (PARTITION BY department ORDER BY hire_date) AS previous_salary,
    LEAD(salary) OVER (PARTITION BY department ORDER BY hire_date) AS next_salary,
    salary - LAG(salary) OVER (PARTITION BY department ORDER BY hire_date) AS salary_increase;

-- 4. Market Share Calculation
SELECT 
    product_id,
    sales_amount,
    sales_amount / SUM(sales_amount) OVER (PARTITION BY category) * 100 AS market_share,
    sales_amount / SUM(sales_amount) OVER () * 100 AS total_share;

-- 5. First/Last Values in Groups
SELECT 
    department,
    employee_name,
    hire_date,
    FIRST_VALUE(salary) OVER (PARTITION BY department ORDER BY hire_date) AS starting_salary,
    LAST_VALUE(salary) OVER (
        PARTITION BY department 
        ORDER BY hire_date
        RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS current_salary;

-- 6. Percentile and Distribution Analysis
SELECT 
    product_id,
    price,
    NTILE(4) OVER (ORDER BY price) AS price_quartile,
    PERCENT_RANK() OVER (ORDER BY price) AS price_percentile,
    CUME_DIST() OVER (ORDER BY price) AS cumulative_distribution;

-- 7. Time-Based Analysis
SELECT 
    transaction_date,
    amount,
    LAG(amount, 7) OVER (ORDER BY transaction_date) AS amount_last_week,
    LEAD(amount, 7) OVER (ORDER BY transaction_date) AS amount_next_week;

-- 8. Growth and Change Analysis
SELECT 
    year,
    revenue,
    revenue - LAG(revenue) OVER (ORDER BY year) AS absolute_change,
    (revenue - LAG(revenue) OVER (ORDER BY year)) / LAG(revenue) OVER (ORDER BY year) * 100 AS percentage_growth;

/* Key Applications:
1. Performance Rankings
2. Financial Analysis
3. Employee Analytics
4. Market Analysis
5. Historical Trending
6. Statistical Analysis
7. Time Series Analysis
8. Growth Metrics
*/
