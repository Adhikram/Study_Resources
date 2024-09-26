CREATE DATABASE test;
-- \c test
-- Insert data into tables
CREATE TABLE table_a (
    key INT
);

CREATE TABLE table_b (
    key INT
);
INSERT INTO table_a (key) VALUES (1);
INSERT INTO table_a (key) VALUES (1);
INSERT INTO table_a (key) VALUES (null);
INSERT INTO table_a (key) VALUES (null);

INSERT INTO table_b (key) VALUES (1);
INSERT INTO table_b (key) VALUES (null);
INSERT INTO table_b (key) VALUES (null);

-- LEFT JOIN
-- Query: SELECT * FROM table_a LEFT JOIN table_b ON table_a.key = table_b.key;
--  key | key 
-- -----+-----
--    1 |   1
--    1 |   1
--      |    
--      |    
-- (4 rows)
SELECT * FROM table_a LEFT JOIN table_b ON table_a.key = table_b.key;

-- RIGHT JOIN
-- Query: SELECT * FROM table_a RIGHT JOIN table_b ON table_a.key = table_b.key;
-- key | key 
-- -----+-----
--    1 |   1
--    1 |   1
--      |    
--      |    
-- (4 rows)
SELECT * FROM table_a RIGHT JOIN table_b ON table_a.key = table_b.key;

-- FULL OUTER JOIN
-- Query: SELECT * FROM table_a FULL OUTER JOIN table_b ON table_a.key = table_b.key;
--  key | key 
-- -----+-----
--    1 |   1
--    1 |   1
--      |    
--      |    
--      |    
--      |    
-- (6 rows)
SELECT * FROM table_a FULL OUTER JOIN table_b ON table_a.key = table_b.key;

-- INNER JOIN
-- Query: SELECT * FROM table_a INNER JOIN table_b ON table_a.key = table_b.key;
--  key | key 
-- -----+-----
--    1 |   1
--    1 |   1
-- (2 rows)
SELECT * FROM table_a INNER JOIN table_b ON table_a.key = table_b.key;

-- CROSS JOIN
-- Query: SELECT * FROM table_a CROSS JOIN table_b;
--  key | key 
-- -----+-----
--    1 |   1
--    1 |    
--    1 |    
--    1 |   1
--    1 |    
--    1 |    
--      |   1
--      |    
--      |    
--      |   1
--      |    
--      |    
-- (12 rows)
SELECT * FROM table_a CROSS JOIN table_b;