/*
Problem: Generate IPL Match Schedules
- Create match combinations for teams
- Handle both single and double round-robin formats
- Maintain unique team pairings
*/

-- Input Table Structure:
-- teams
-- team_name    VARCHAR

-- Sample Input:
-- team_name
-- Mumbai Indians
-- Chennai Super Kings
-- Royal Challengers
-- Delhi Capitals

-- Method 1: Single Round-Robin (Each team plays once)
WITH matches AS (
    SELECT 
        ROW_NUMBER() OVER(
            ORDER BY team_name
        ) AS id,
        t.*
    FROM teams t
)
SELECT 
    team.team_name AS team,
    opponent.team_name AS opponent
FROM matches team
JOIN matches opponent 
    ON team.id < opponent.id
ORDER BY team;

-- Method 2: Double Round-Robin (Home and Away matches)
WITH matches AS (
    SELECT 
        ROW_NUMBER() OVER(
            ORDER BY team_name
        ) AS id,
        t.*
    FROM teams t
)
SELECT 
    team.team_name AS team,
    opponent.team_name AS opponent
FROM matches team
JOIN matches opponent 
    ON team.id <> opponent.id
ORDER BY team;

-- Expected Output (Single Round-Robin):
-- team                  opponent
-- Chennai Super Kings   Delhi Capitals
-- Chennai Super Kings   Mumbai Indians
-- Delhi Capitals       Mumbai Indians

/* Performance Optimizations:
1. Efficient ROW_NUMBER for team identification
2. Smart join conditions for match pairing
3. Consider index on team_name
4. Multiple format options
5. Optimal sort strategy
*/
