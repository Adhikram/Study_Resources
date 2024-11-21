/*
Problem: Comprehensive Numeric Function Applications
*/

-- 1. Financial Calculations
SELECT 
    transaction_id,
    ROUND(amount, 2) AS rounded_amount,
    CEIL(tax_rate * amount) AS tax_ceiling,
    FLOOR(discount * amount) AS min_discount,
    ABS(balance_change) AS absolute_change;

-- 2. Statistical Analysis
SELECT 
    department_id,
    AVG(salary) AS average_salary,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) AS median_salary,
    STDDEV(salary) AS salary_deviation,
    VARIANCE(salary) AS salary_variance;

-- 3. Product Pricing
SELECT 
    product_id,
    ROUND(base_price * (1 + markup_rate), 2) AS retail_price,
    FLOOR(base_price * 0.9) AS sale_price,
    CEIL(shipping_weight * shipping_rate) AS shipping_cost;

-- 4. Performance Metrics
SELECT 
    employee_id,
    ROUND(success_rate * 100, 1) AS success_percentage,
    POWER(growth_rate, 4) AS compound_growth,
    SQRT(variance) AS standard_deviation;

-- 5. Distance Calculations
SELECT 
    location_id,
    ROUND(SQRT(POWER(x2 - x1, 2) + POWER(y2 - y1, 2)), 2) AS distance,
    CEIL(distance / speed) AS estimated_hours;

-- 6. Random Sampling
SELECT 
    product_id,
    RANDOM() AS random_value,
    FLOOR(RANDOM() * 100) AS percentage,
    CEIL(RANDOM() * 10) AS scale_rating;

-- 7. Inventory Management
SELECT 
    item_id,
    FLOOR(available_quantity * 0.2) AS reorder_point,
    CEIL(average_daily_sales * lead_time) AS safety_stock,
    ROUND(unit_cost * quantity, 2) AS total_value;

-- 8. Score Calculations
SELECT 
    student_id,
    ROUND(AVG(score), 1) AS average_score,
    GREATEST(score1, score2, score3) AS best_score,
    LEAST(score1, score2, score3) AS lowest_score;

-- 9. Market Analysis
SELECT 
    stock_id,
    ROUND(closing_price, 2) AS rounded_price,
    ABS(price_change) AS price_movement,
    POWER(1 + daily_return, 252) - 1 AS annual_return;

-- 10. Resource Utilization
SELECT 
    server_id,
    ROUND(cpu_usage * 100, 1) AS cpu_percentage,
    CEIL(memory_used / memory_total * 100) AS memory_utilization,
    FLOOR(disk_free / disk_total * 100) AS free_space_percent;

/* Key Applications:
1. Financial Analysis
2. Statistical Computations
3. Pricing Strategies
4. Performance Analysis
5. Geospatial Calculations
6. Data Sampling
7. Inventory Control
8. Academic Scoring
9. Market Analysis
10. System Monitoring
*/
