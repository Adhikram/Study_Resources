/*
Problem: Demonstrate TO_CHAR Date Formatting
- Format dates into specific string patterns
- Support multiple locale formats
- Enable custom date representations
*/

-- Input Table Structure:
-- appointments
-- appt_id       INT
-- appt_time     TIMESTAMP
-- description   VARCHAR

-- Basic Date Formatting
SELECT 
    appt_time,
    TO_CHAR(appt_time, 'YYYY-MM-DD') AS standard_date,
    TO_CHAR(appt_time, 'Month DD, YYYY') AS long_date,
    TO_CHAR(appt_time, 'DY, DD Mon YYYY') AS custom_date,
    TO_CHAR(appt_time, 'HH24:MI:SS') AS time_only
FROM appointments;

-- Custom Business Formats
SELECT 
    TO_CHAR(appt_time, 'FMMonth') AS month_name,
    TO_CHAR(appt_time, 'Q') AS quarter,
    TO_CHAR(appt_time, 'W') AS week_of_month,
    TO_CHAR(appt_time, 'Day, HH12:MI AM') AS readable_time
FROM appointments;

-- Report Generation
SELECT 
    TO_CHAR(CURRENT_DATE, 'FMDay, Month DD, YYYY') AS report_date,
    TO_CHAR(appt_time, 'DD-Mon-YY HH24:MI') AS appointment,
    description
FROM appointments;

-- Expected Output:
-- standard_date    long_date           custom_date         time_only
-- 2024-01-20      January 20, 2024    SAT, 20 Jan 2024    14:30:00

/* Performance Optimizations:
1. Cache frequently used formats
2. Use for display purposes only
3. Keep date calculations in native format
4. Consider locale settings
5. Index original timestamp columns
*/
