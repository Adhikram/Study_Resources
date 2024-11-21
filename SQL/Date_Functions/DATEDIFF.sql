/*
Problem: Comprehensive DATEDIFF Applications
*/

-- 1. Employee Tenure Calculation
SELECT 
    employee_id,
    hire_date,
    DATEDIFF('year', hire_date, CURRENT_DATE) AS years_employed,
    DATEDIFF('month', hire_date, CURRENT_DATE) AS months_employed,
    DATEDIFF('day', hire_date, CURRENT_DATE) AS days_employed;

-- 2. Project Timeline Analysis
SELECT 
    project_id,
    start_date,
    end_date,
    DATEDIFF('day', start_date, end_date) AS project_duration,
    DATEDIFF('week', start_date, end_date) AS project_weeks;

-- 3. Age Calculation
SELECT 
    customer_id,
    birth_date,
    DATEDIFF('year', birth_date, CURRENT_DATE) AS age;

-- 4. Order Processing Time
SELECT 
    order_id,
    order_date,
    delivery_date,
    DATEDIFF('hour', order_date, delivery_date) AS processing_hours,
    DATEDIFF('minute', order_date, delivery_date) AS processing_minutes;

-- 5. Subscription Duration
SELECT 
    subscription_id,
    start_date,
    end_date,
    DATEDIFF('month', start_date, end_date) AS subscription_length;

-- 6. Late Payment Analysis
SELECT 
    payment_id,
    due_date,
    payment_date,
    DATEDIFF('day', due_date, payment_date) AS days_overdue;

-- 7. Product Shelf Life
SELECT 
    product_id,
    manufacture_date,
    expiry_date,
    DATEDIFF('day', manufacture_date, expiry_date) AS shelf_life_days;

-- 8. Event Duration
SELECT 
    event_id,
    start_time,
    end_time,
    DATEDIFF('minute', start_time, end_time) AS event_duration;

-- 9. Account Inactivity
SELECT 
    user_id,
    last_login,
    DATEDIFF('day', last_login, CURRENT_TIMESTAMP) AS days_inactive;

-- 10. Contract Term Analysis
SELECT 
    contract_id,
    effective_date,
    termination_date,
    DATEDIFF('month', effective_date, termination_date) AS contract_term;

/* Key Applications:
1. HR Analytics
2. Project Management
3. Customer Demographics
4. Operations Metrics
5. Subscription Management
6. Financial Analysis
7. Inventory Management
8. Event Planning
9. User Activity Tracking
10. Contract Management
*/
