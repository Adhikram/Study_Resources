/*
Problem: Advanced JSON Data Manipulation and Analysis
*/

-- 1. Nested JSON Extraction
SELECT 
    -- Basic JSON Path Navigation
    data->>'name' AS user_name,
    data#>>'{address,street}' AS street,
    data#>>'{address,city}' AS city,
    data#>>'{address,country}' AS country,
    
    -- Array Handling
    jsonb_array_elements(data->'phones') AS phone_numbers,
    jsonb_array_length(data->'orders') AS order_count;

-- 2. JSON Construction and Modification
SELECT 
    -- Building JSON Objects
    json_build_object(
        'id', user_id,
        'profile', json_build_object(
            'name', user_name,
            'email', email,
            'age', age
        ),
        'settings', user_settings
    ) AS user_json,
    
    -- Modifying JSON
    jsonb_set(data, '{status}', '"active"') AS updated_status,
    jsonb_insert(data, '{tags,0}', '"new"') AS modified_tags;

-- 3. JSON Aggregation and Analysis
SELECT 
    department,
    jsonb_object_agg(employee_id, salary) AS salary_map,
    jsonb_agg(json_build_object(
        'id', employee_id,
        'name', name,
        'role', role
    )) AS team_details;

-- 4. JSON Validation and Type Checking
SELECT 
    jsonb_typeof(data) AS json_type,
    jsonb_strip_nulls(data) AS cleaned_json,
    jsonb_pretty(data) AS formatted_json;

-- 5. Complex JSON Querying
SELECT *
FROM users,
    jsonb_array_elements(data->'orders') AS orders
WHERE orders->>'status' = 'completed'
AND (data->>'account_type' = 'premium');

/* Key Features:
1. Deep JSON Navigation
2. Dynamic JSON Construction
3. Array and Object Operations
4. Type Validation
5. Complex JSON Querying
*/