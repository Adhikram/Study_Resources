 /*
Select Employee ID and the team count. Every employee should be displayed

Employee Table:
+-------------+------------+
| employee_id | team_id    |
+-------------+------------+
|     1       |     8      |
|     2       |     8      |
|     3       |     8      |
|     4       |     7      |
|     5       |     9      |
|     6       |     9      |
+-------------+------------+ 

with team_data as (
    select team_id, count(*) as team_count from employee group by team_id
)
select em.employee_id, td.team_count from employee as 
em join team_data as td on em.team_id = td.team_id;*/

/*
Transpose the subjects by class. Each class can have max of 5 subjects. 

class	subject rank
A	MATH    1
B	SCIENCE 1
A	ARTS    2
B	ECONOMICS   2
A	HISTORY 3
A	GEOGRAPHY 4
A	CHEMISTRY 5
B	PHYSICS 3
B	CHEMISTRY 4
B	BIOLOGY  5 */

-- list collect As  group by on class 
 -- class sub 1  sub 2 sub 3  sub 4 sub5 
-- A MAths Arts ...
-- B H .. .. 
/* 
Approach 1: Using CASE Statements
Pros: Simple to understand, works in all SQL versions
Cons: Requires manual column specification
*/
SELECT class,
    MAX(CASE WHEN rn = 1 THEN subject END) AS subject1,
    MAX(CASE WHEN rn = 2 THEN subject END) AS subject2,
    MAX(CASE WHEN rn = 3 THEN subject END) AS subject3,
    MAX(CASE WHEN rn = 4 THEN subject END) AS subject4,
    MAX(CASE WHEN rn = 5 THEN subject END) AS subject5
FROM (
    SELECT class, subject,
           ROW_NUMBER() OVER (PARTITION BY class ORDER BY subject) as rn
    FROM class_subjects
) t
GROUP BY class;

/* 
Approach 2: Using Conditional Aggregation with IF
Pros: More concise than CASE statements
Cons: MySQL specific, less readable
*/
SELECT class,
    MAX(IF(rn = 1, subject, NULL)) AS subject1,
    MAX(IF(rn = 2, subject, NULL)) AS subject2,
    MAX(IF(rn = 3, subject, NULL)) AS subject3,
    MAX(IF(rn = 4, subject, NULL)) AS subject4,
    MAX(IF(rn = 5, subject, NULL)) AS subject5
FROM (
    SELECT class, subject,
           ROW_NUMBER() OVER (PARTITION BY class ORDER BY subject) as rn
    FROM class_subjects
) t
GROUP BY class;

/* 
Approach 3: Using Multiple Self Joins
Pros: Works without window functions
Cons: Performance degrades with more columns
*/
SELECT 
    c1.class,
    c1.subject AS subject1,
    c2.subject AS subject2,
    c3.subject AS subject3,
    c4.subject AS subject4,
    c5.subject AS subject5
FROM 
    (SELECT DISTINCT class FROM class_subjects) base
LEFT JOIN class_subjects c1 ON base.class = c1.class AND c1.rank = 1
LEFT JOIN class_subjects c2 ON base.class = c2.class AND c2.rank = 2
LEFT JOIN class_subjects c3 ON base.class = c3.class AND c3.rank = 3
LEFT JOIN class_subjects c4 ON base.class = c4.class AND c4.rank = 4
LEFT JOIN class_subjects c5 ON base.class = c5.class AND c5.rank = 5;

/* 
Approach 4: Using Dynamic SQL (Stored Procedure)
Pros: Handles dynamic number of columns
Cons: More complex, requires stored procedure
*/
DELIMITER //
CREATE PROCEDURE dynamic_pivot()
BEGIN
    SET @sql = NULL;
    SELECT GROUP_CONCAT(DISTINCT
        CONCAT('MAX(CASE WHEN rn = ', rn, 
              ' THEN subject END) AS subject', rn)
    )
    INTO @sql
    FROM (
        SELECT ROW_NUMBER() OVER (PARTITION BY class ORDER BY subject) as rn
        FROM class_subjects
    ) t;

    SET @sql = CONCAT('SELECT class, ', @sql, ' 
                      FROM (
                          SELECT class, subject,
                                 ROW_NUMBER() OVER (PARTITION BY class ORDER BY subject) as rn
                          FROM class_subjects
                      ) t
                      GROUP BY class');

    PREPARE stmt FROM @sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END //
DELIMITER ;

/* 
Performance Optimization Tips:
1. Index on (class, subject) for better sorting
2. Materialize subqueries for large datasets
3. Use covering indexes where possible
4. Consider partitioning for very large tables
*/