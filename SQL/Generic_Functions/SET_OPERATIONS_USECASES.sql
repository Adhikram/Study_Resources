/*
Problem: Advanced Set Operations and Grouping Analysis
*/

-- 1. Sales Analysis with Multiple Dimensions
SELECT 
    GROUPING SETS (
        (region, product_category, year),
        (region, product_category),
        (region),
        ()
    ),
    SUM(sales_amount) AS total_sales
FROM sales_data;

-- 2. Employee Performance Matrix
SELECT 
    CUBE (department, location, quarter),
    COUNT(employee_id) AS employee_count,
    AVG(performance_score) AS avg_performance
FROM employee_metrics;

-- 3. Revenue Hierarchy Analysis
SELECT 
    ROLLUP (year, quarter, month, day),
    SUM(revenue) AS total_revenue,
    COUNT(DISTINCT customer_id) AS customer_count
FROM financial_data;

-- 4. Product Performance Trends
SELECT 
    category,
    subcategory,
    month,
    SUM(amount) OVER (
        PARTITION BY category 
        ORDER BY month
        ROWS BETWEEN 3 PRECEDING AND CURRENT ROW
    ) AS rolling_sum
FROM product_sales;

-- 5. Regional Market Share
SELECT 
    GROUPING(region) AS is_region_total,
    GROUPING(product) AS is_product_total,
    GROUPING_ID(region, product, year) AS grouping_level,
    SUM(market_share) AS total_share
FROM market_data;

-- 6. Customer Segment Analysis
SELECT 
    CUBE (segment, country, product),
    COUNT(*) AS customer_count,
    SUM(purchase_amount) AS total_purchases
FROM customer_data;

-- 7. Time-based Comparisons
SELECT 
    ROLLUP (year, quarter),
    AVG(growth_rate) AS avg_growth,
    STDDEV(growth_rate) AS growth_volatility
FROM growth_metrics;

-- 8. Multi-level Inventory Analysis
SELECT 
    GROUPING SETS (
        (warehouse, product_type),
        (warehouse),
        (product_type),
        ()
    ),
    SUM(stock_level) AS total_stock
FROM inventory;

/* Key Applications:
1. Multi-dimensional Analysis
2. Hierarchical Reporting
3. Time Series Analysis
4. Performance Metrics
5. Market Analysis
6. Customer Analytics
7. Growth Analysis
8. Inventory Management
*/
