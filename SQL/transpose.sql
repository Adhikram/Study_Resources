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
with ranked_subjects as (
    select class , subject , row_number() over (partition by class) as rn from class
),cl1 as (
    select class , subject  from ranked_subjects where rn = 1 
), cl2 as (
    select class , subject  from ranked_subjects where rn = 2 
), cl3 as (
    select class , subject  from ranked_subjects where rn = 3
), cl4 as (
    select class , subject  from ranked_subjects where rn = 4
), cl5 as (
    select class , subject  from ranked_subjects where rn = 5 
)

SELECT cl1.class, cl1.subject, cl2.subject, cl3.subject, cl4.subject, cl5.subject
 from cl1
left join cl2 on cl1.class = cl2.class
left join cl3 on cl1.class = cl3.class
left join cl4 on cl1.class = cl4.class
left join cl5 on cl1.class = cl5.class

-- with collected_data AS(
--     select class , collect_list(subject) from class
-- )
-- select class , 
