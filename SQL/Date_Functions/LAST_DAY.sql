/*
Problem: Comprehensive DATEADD Applications
*/

-- 1. Scheduling Future Events
SELECT 
    event_id,
    start_date,
    DATEADD(hour, 2, start_date) AS end_time,
    DATEADD(day, 7, start_date) AS follow_up_date,
    DATEADD(month, 1, start_date) AS monthly_recurring;

-- 2. Subscription Management
SELECT 
    subscription_id,
    start_date,
    DATEADD(month, subscription_length, start_date) AS renewal_date,
    DATEADD(day, -7, DATEADD(month, subscription_length, start_date)) AS reminder_date;

-- 3. Financial Deadlines
SELECT 
    invoice_id,
    issue_date,
    DATEADD(day, 30, issue_date) AS payment_due_date,
    DATEADD(day, 45, issue_date) AS late_payment_date;

-- 4. Product Lifecycle
SELECT 
    product_id,
    manufacture_date,
    DATEADD(year, 2, manufacture_date) AS warranty_end,
    DATEADD(month, shelf_life, manufacture_date) AS expiry_date;

-- 5. HR Planning
SELECT 
    employee_id,
    hire_date,
    DATEADD(month, 3, hire_date) AS probation_end,
    DATEADD(year, 1, hire_date) AS first_review_date;

-- 6. Maintenance Scheduling
SELECT 
    equipment_id,
    last_service,
    DATEADD(month, service_interval, last_service) AS next_service,
    DATEADD(year, 5, installation_date) AS replacement_date;

-- 7. Project Milestones
SELECT 
    project_id,
    start_date,
    DATEADD(week, 2, start_date) AS phase1_deadline,
    DATEADD(month, 3, start_date) AS midpoint_review;

-- 8. Inventory Management
SELECT 
    batch_id,
    received_date,
    DATEADD(day, 90, received_date) AS stock_review_date,
    DATEADD(year, 1, received_date) AS inventory_depreciation;

-- 9. Customer Engagement
SELECT 
    customer_id,
    signup_date,
    DATEADD(day, 7, signup_date) AS welcome_email_date,
    DATEADD(month, 6, signup_date) AS loyalty_program_eligible;

-- 10. System Maintenance
SELECT 
    server_id,
    last_backup,
    DATEADD(hour, 12, last_backup) AS next_backup,
    DATEADD(day, 30, last_backup) AS monthly_maintenance;

/* Key Applications:
1. Event Management
2. Subscription Services
3. Financial Planning
4. Product Management
5. Human Resources
6. Maintenance Planning
7. Project Management
8. Inventory Control
9. Customer Relations
10. System Administration
*/
