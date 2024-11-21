/*
Problem: Comprehensive Type Conversion Applications
*/

-- 1. Numeric Conversions
SELECT 
    CAST(string_number AS INTEGER) AS to_integer,
    CAST(float_number AS DECIMAL(10,2)) AS to_decimal,
    price::NUMERIC(10,2) AS to_numeric,
    CAST(text_amount AS MONEY) AS to_money;

-- 2. Date/Time Conversions
SELECT 
    TO_DATE(date_string, 'YYYY-MM-DD') AS to_date,
    TO_TIMESTAMP(timestamp_string, 'YYYY-MM-DD HH24:MI:SS') AS to_timestamp,
    CAST(epoch_value AS TIMESTAMP) AS from_epoch,
    date_column::TIME AS extract_time;

-- 3. String Conversions
SELECT 
    number_value::TEXT AS to_string,
    CAST(date_value AS VARCHAR) AS date_string,
    array_to_string(string_array, ', ') AS array_to_text,
    boolean_value::TEXT AS bool_string;

-- 4. Boolean Conversions
SELECT 
    CAST(integer_flag AS BOOLEAN) AS to_boolean,
    CASE 
        WHEN text_value IN ('true', 'yes', '1') THEN TRUE
        ELSE FALSE 
    END AS text_to_bool;

-- 5. Array Conversions
SELECT 
    string_to_array(comma_list, ',') AS to_array,
    ARRAY[1,2,3]::TEXT[] AS number_to_text_array,
    array_agg(distinct_values)::INTEGER[] AS to_integer_array;

-- 6. JSON Conversions
SELECT 
    row_to_json(table_row) AS to_json,
    json_object::TEXT AS json_to_text,
    json_array_elements(json_data) AS json_to_records;

-- 7. Network Data Types
SELECT 
    CAST(ip_string AS INET) AS to_inet,
    CAST(mac_string AS MACADDR) AS to_macaddr,
    network_column::CIDR AS to_cidr;

-- 8. Geometric Types
SELECT 
    CAST(point_string AS POINT) AS to_point,
    CAST(line_string AS LINE) AS to_line,
    polygon_string::POLYGON AS to_polygon;

-- 9. Range Types
SELECT 
    int4range(start_num, end_num) AS integer_range,
    daterange(start_date, end_date) AS date_range,
    numrange(low, high, '[]') AS numeric_range;

-- 10. Custom Type Conversions
SELECT 
    CAST(status_code AS custom_status) AS to_enum,
    complex_data::custom_type AS to_custom,
    xml_string::XML AS to_xml;

/* Key Applications:
1. Data Type Standardization
2. Date/Time Processing
3. String Manipulation
4. Boolean Logic
5. Array Operations
6. JSON Processing
7. Network Data Handling
8. Geometric Data
9. Range Operations
10. Custom Type Management
*/
