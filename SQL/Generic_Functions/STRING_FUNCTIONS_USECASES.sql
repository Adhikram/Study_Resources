/*
Problem: Comprehensive String Manipulation Applications
*/

-- 1. Name Formatting
SELECT 
    INITCAP(first_name) AS formatted_first,
    UPPER(last_name) AS formatted_last,
    CONCAT(
        INITCAP(first_name), 
        ' ', 
        UPPER(last_name)
    ) AS full_name;

-- 2. Email Processing
SELECT 
    LOWER(email) AS normalized_email,
    SPLIT_PART(email, '@', 1) AS username,
    SPLIT_PART(email, '@', 2) AS domain,
    OVERLAY(email PLACING '***' FROM 2 FOR 3) AS masked_email;

-- 3. Address Standardization
SELECT 
    TRIM(BOTH ' ' FROM address) AS cleaned_address,
    INITCAP(city) AS formatted_city,
    UPPER(state_code) AS state,
    REGEXP_REPLACE(zip, '[^0-9]', '') AS cleaned_zip;

-- 4. Product Code Processing
SELECT 
    LEFT(product_code, 3) AS category_code,
    RIGHT(product_code, 4) AS item_number,
    SUBSTRING(product_code FROM 4 FOR 2) AS variant_code;

-- 5. Search Optimization
SELECT 
    product_name,
    LOWER(product_name) AS search_term,
    REPLACE(product_name, ' ', '_') AS url_slug,
    SOUNDEX(product_name) AS phonetic_code;

-- 6. Data Cleaning
SELECT 
    TRIM(BOTH FROM description) AS cleaned_text,
    REGEXP_REPLACE(phone, '[^0-9]', '') AS cleaned_phone,
    NULLIF(TRIM(field), '') AS non_empty_field;

-- 7. Text Analysis
SELECT 
    LENGTH(content) AS content_length,
    CHAR_LENGTH(content) AS char_count,
    REGEXP_COUNT(content, '\w+') AS word_count,
    STRING_AGG(tag, ', ') AS combined_tags;

-- 8. Security and Privacy
SELECT 
    OVERLAY(credit_card PLACING '****' FROM 13 FOR 4) AS masked_cc,
    OVERLAY(phone PLACING '***' FROM 4 FOR 3) AS masked_phone,
    REGEXP_REPLACE(ssn, '\d', '*') AS masked_ssn;

-- 9. URL Processing
SELECT 
    SPLIT_PART(url, '://', 1) AS protocol,
    SPLIT_PART(SPLIT_PART(url, '://', 2), '/', 1) AS domain,
    REGEXP_REPLACE(url, '^https?://([^/]+).*', '\1') AS extracted_domain;

-- 10. Report Generation
SELECT 
    LPAD(invoice_number::text, 8, '0') AS formatted_invoice,
    RPAD(status, 10, '.') AS status_display,
    STRING_AGG(item_name, ', ' ORDER BY item_name) AS item_list;

/* Key Applications:
1. Name Management
2. Email Handling
3. Address Management
4. Product Management
5. Search Functionality
6. Data Cleansing
7. Content Analysis
8. Data Security
9. URL Handling
10. Report Formatting
*/
