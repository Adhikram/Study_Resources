/*
Problem: Comprehensive LEAD/LAG Function Applications
*/

-- 1. Price Change Analysis
SELECT 
    product_id,
    price_date,
    price,
    LAG(price) OVER (PARTITION BY product_id ORDER BY price_date) AS previous_price,
    LEAD(price) OVER (PARTITION BY product_id ORDER BY price_date) AS next_price,
    price - LAG(price) OVER (PARTITION BY product_id ORDER BY price_date) AS price_change;

-- 2. Employee Salary Progression
SELECT 
    employee_id,
    review_date,
    salary,
    LAG(salary, 1) OVER (PARTITION BY employee_id ORDER BY review_date) AS last_salary,
    LEAD(salary, 1) OVER (PARTITION BY employee_id ORDER BY review_date) AS next_salary,
    (salary - LAG(salary) OVER (PARTITION BY employee_id ORDER BY review_date)) / 
    LAG(salary) OVER (PARTITION BY employee_id ORDER BY review_date) * 100 AS salary_growth_percent;

-- 3. Stock Market Analysis
SELECT 
    stock_symbol,
    trading_date,
    closing_price,
    LAG(closing_price, 1) OVER (PARTITION BY stock_symbol ORDER BY trading_date) AS prev_day_close,
    LEAD(closing_price, 1) OVER (PARTITION BY stock_symbol ORDER BY trading_date) AS next_day_close,
    LAG(closing_price, 5) OVER (PARTITION BY stock_symbol ORDER BY trading_date) AS last_week_close;

-- 4. Customer Purchase Patterns
SELECT 
    customer_id,
    order_date,
    order_amount,
    LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS previous_order_date,
    order_date - LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS days_between_orders;

-- 5. Website Traffic Analysis
SELECT 
    page_id,
    visit_timestamp,
    visitor_count,
    LAG(visitor_count) OVER (PARTITION BY page_id ORDER BY visit_timestamp) AS prev_hour_visitors,
    LEAD(visitor_count) OVER (PARTITION BY page_id ORDER BY visit_timestamp) AS next_hour_visitors;

-- 6. Inventory Level Tracking
SELECT 
    product_id,
    check_date,
    stock_level,
    LAG(stock_level) OVER (PARTITION BY product_id ORDER BY check_date) AS previous_stock,
    stock_level - LAG(stock_level) OVER (PARTITION BY product_id ORDER BY check_date) AS stock_change;

-- 7. Temperature Variation Analysis
SELECT 
    location_id,
    reading_time,
    temperature,
    LAG(temperature, 1) OVER (PARTITION BY location_id ORDER BY reading_time) AS prev_temp,
    LEAD(temperature, 1) OVER (PARTITION BY location_id ORDER BY reading_time) AS next_temp,
    ABS(temperature - LAG(temperature) OVER (PARTITION BY location_id ORDER BY reading_time)) AS temp_change;

-- 8. Sales Performance Comparison
SELECT 
    sales_rep_id,
    month_date,
    sales_amount,
    LAG(sales_amount, 12) OVER (PARTITION BY sales_rep_id ORDER BY month_date) AS last_year_sales,
    sales_amount - LAG(sales_amount, 12) OVER (PARTITION BY sales_rep_id ORDER BY month_date) AS yoy_growth;

/* Key Applications:
1. Price Analytics
2. HR Analytics
3. Financial Markets
4. Customer Behavior
5. Traffic Analysis
6. Inventory Management
7. Environmental Monitoring
8. Sales Analytics
*/
