/*
Problem: Comprehensive Split Function Applications in MySQL
*/

-- 1. Splitting a comma-separated list of values (first element)
SELECT 
    customer_id,
    SUBSTRING_INDEX(preferences, ',', 1) AS first_preference
FROM customers;

-- 2. Extracting domain from email addresses
SELECT 
    user_id,
    SUBSTRING_INDEX(email, '@', -1) AS domain
FROM users;

-- 3. Parsing full names into first and last names
SELECT 
    employee_id,
    SUBSTRING_INDEX(full_name, ' ', 1) AS first_name,
    SUBSTRING_INDEX(SUBSTRING_INDEX(full_name, ' ', 2), ' ', -1) AS last_name
FROM employees;

-- 4. Splitting URL into protocol, domain, and path
SELECT 
    page_id,
    SUBSTRING_INDEX(url, '://', 1) AS protocol,
    SUBSTRING_INDEX(SUBSTRING_INDEX(url, '://', -1), '/', 1) AS domain,
    SUBSTRING_INDEX(url, '/', -1) AS path
FROM web_pages;

-- 5. Splitting a CSV string into individual columns (first three elements)
SELECT 
    order_id,
    SUBSTRING_INDEX(order_details, ',', 1) AS product_id,
    SUBSTRING_INDEX(SUBSTRING_INDEX(order_details, ',', 2), ',', -1) AS quantity,
    SUBSTRING_INDEX(SUBSTRING_INDEX(order_details, ',', 3), ',', -1) AS price
FROM orders;

-- 6. Extracting year, month, and day from a date string
SELECT 
    event_id,
    SUBSTRING_INDEX(event_date, '-', 1) AS year,
    SUBSTRING_INDEX(SUBSTRING_INDEX(event_date, '-', 2), '-', -1) AS month,
    SUBSTRING_INDEX(event_date, '-', -1) AS day
FROM events;

-- 7. Splitting a path into directory and file name
SELECT 
    file_id,
    SUBSTRING_INDEX(file_path, '/', -2) AS directory,
    SUBSTRING_INDEX(file_path, '/', -1) AS file_name
FROM files;

/* Key Applications:
1. Data Parsing
2. Email Processing
3. Name Handling
4. URL Manipulation
5. CSV Handling
6. Date Processing
7. File System Navigation
*/

-- Note: For more complex splitting tasks, consider using stored procedures or user-defined functions.
