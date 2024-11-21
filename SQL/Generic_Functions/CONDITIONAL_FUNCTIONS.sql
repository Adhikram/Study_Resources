/*
Problem: Comprehensive Conditional Function Applications
*/

-- 1. Customer Segmentation
SELECT 
    customer_id,
    CASE 
        WHEN total_spend > 10000 THEN 'Platinum'
        WHEN total_spend > 5000 THEN 'Gold'
        WHEN total_spend > 1000 THEN 'Silver'
        ELSE 'Bronze'
    END AS customer_tier,
    COALESCE(preferred_contact, email, phone, 'No Contact') AS contact_method;

-- 2. Employee Performance Rating
SELECT 
    employee_id,
    CASE 
        WHEN sales_target_achieved >= 120 THEN 'Outstanding'
        WHEN sales_target_achieved >= 100 THEN 'Met Target'
        WHEN sales_target_achieved >= 80 THEN 'Near Target'
        ELSE 'Needs Improvement'
    END AS performance_rating;

-- 3. Product Inventory Status
SELECT 
    product_id,
    CASE 
        WHEN stock_level = 0 THEN 'Out of Stock'
        WHEN stock_level < reorder_point THEN 'Reorder Required'
        WHEN stock_level < (reorder_point * 2) THEN 'Adequate'
        ELSE 'Well Stocked'
    END AS stock_status;

-- 4. Order Processing Priority
SELECT 
    order_id,
    CASE 
        WHEN shipping_method = 'Express' AND amount > 1000 THEN 'High Priority'
        WHEN shipping_method = 'Express' THEN 'Medium Priority'
        ELSE 'Standard Priority'
    END AS processing_priority;

-- 5. Financial Transaction Categorization
SELECT 
    transaction_id,
    NULLIF(category_override, default_category) AS final_category,
    COALESCE(description, 'Uncategorized Transaction') AS transaction_description;

-- 6. Student Grade Assignment
SELECT 
    student_id,
    CASE 
        WHEN score >= 90 THEN 'A'
        WHEN score >= 80 THEN 'B'
        WHEN score >= 70 THEN 'C'
        WHEN score >= 60 THEN 'D'
        ELSE 'F'
    END AS grade;

-- 7. Weather Condition Classification
SELECT 
    location_id,
    CASE 
        WHEN temperature > 30 THEN 'Hot'
        WHEN temperature > 20 THEN 'Warm'
        WHEN temperature > 10 THEN 'Mild'
        ELSE 'Cold'
    END AS temperature_category;

-- 8. Account Status Determination
SELECT 
    account_id,
    CASE 
        WHEN days_inactive > 365 THEN 'Dormant'
        WHEN days_inactive > 180 THEN 'Inactive'
        WHEN days_inactive > 90 THEN 'At Risk'
        ELSE 'Active'
    END AS account_status;

-- 9. Price Discount Calculation
SELECT 
    product_id,
    GREATEST(
        regular_discount,
        member_discount,
        seasonal_discount
    ) AS applied_discount;

-- 10. Risk Assessment
SELECT 
    client_id,
    CASE 
        WHEN credit_score > 750 AND income > 100000 THEN 'Low Risk'
        WHEN credit_score > 650 AND income > 50000 THEN 'Medium Risk'
        ELSE 'High Risk'
    END AS risk_category;

/* Key Applications:
1. Customer Management
2. HR Analytics
3. Inventory Management
4. Order Processing
5. Financial Analysis
6. Education Systems
7. Environmental Monitoring
8. Account Management
9. Pricing Strategies
10. Risk Management
*/
