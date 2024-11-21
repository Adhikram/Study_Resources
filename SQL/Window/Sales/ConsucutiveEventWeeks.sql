/*
Problem: Identify High-Engagement Marketing Contacts
- Find contacts with 3+ consecutive weeks of marketing touches
- Must have at least one trial_request event
- Return unique email addresses sorted alphabetically
*/

-- Input Tables Structure:
-- marketing_touches
-- event_id         INT
-- contact_id       INT
-- event_type       VARCHAR ('webinar', 'conference_registration', 'trial_request')
-- event_date       DATE

-- crm_contacts
-- contact_id       INT
-- email           VARCHAR

-- Sample Input:
-- marketing_touches
-- event_id    contact_id    event_type    event_date
-- 1           1            webinar        2022-04-17
-- 2           1            trial_request  2022-04-23
-- 3           1            whitepaper     2022-04-30

-- Identify trial request contacts
WITH trial_contacts AS (
    SELECT DISTINCT 
        contact_id
    FROM marketing_touches
    WHERE 
        event_type = 'trial_request'
),

-- Analyze weekly engagement patterns
weekly_touches AS (
    SELECT 
        contact_id,
        DATE_TRUNC('week', event_date) AS event_week,
        ROW_NUMBER() OVER (
            PARTITION BY contact_id 
            ORDER BY DATE_TRUNC('week', event_date)
        ) AS week_number
    FROM marketing_touches
    GROUP BY 
        contact_id,
        DATE_TRUNC('week', event_date)
),

-- Find contacts with consecutive weeks
consecutive_contacts AS (
    SELECT 
        contact_id
    FROM weekly_touches
    GROUP BY contact_id
    HAVING COUNT(*) >= 3
)

-- Get qualifying contact emails
SELECT DISTINCT 
    c.email
FROM crm_contacts c
INNER JOIN consecutive_contacts cc 
    ON c.contact_id = cc.contact_id
INNER JOIN trial_contacts tc 
    ON c.contact_id = tc.contact_id
ORDER BY c.email;

-- Expected Output:
-- email
-- andy.markus@att.net
-- rajan.bhatt@capitalone.com

/* Performance Optimizations:
1. Used CTEs for logical separation
2. Efficient date truncation
3. Consider indexes on:
   - marketing_touches(contact_id, event_type, event_date)
   - crm_contacts(contact_id, email)
4. DISTINCT for unique emails
5. Optimized JOIN sequence
*/
