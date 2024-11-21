/*
Problem: Facebook Friend Recommendations Based on Shared Events
- Input: Event RSVPs and friendship status tables
- Output: Potential friend pairs who share multiple private events
- Requirements: 
* Users must share 2+ private events
* Users must not be current friends
* Sort by user_a_id, user_b_id
*/

-- CTE to identify users interested in private events
WITH private_events AS (
  SELECT 
      user_id,
      event_id
  FROM event_rsvp
  WHERE 
      -- Only consider positive responses to private events
      attendance_status IN ('going', 'maybe')
      AND event_type = 'private'
)

-- Main query to find matching user pairs
SELECT 
  friends.user_a_id, 
  friends.user_b_id
FROM private_events AS events_1
INNER JOIN private_events AS events_2
  -- Match users who attended same events
  ON events_1.user_id != events_2.user_id
  AND events_1.event_id = events_2.event_id
INNER JOIN friendship_status AS friends
  -- Connect with friendship status
  ON events_1.user_id = friends.user_a_id
  AND events_2.user_id = friends.user_b_id
WHERE 
  friends.status = 'not_friends'
GROUP BY 
  friends.user_a_id, 
  friends.user_b_id
HAVING 
  COUNT(*) >= 2  -- Must share at least 2 events
ORDER BY 
  friends.user_a_id, 
  friends.user_b_id;

/* Performance Optimizations:
1. Used CTE to filter relevant event data early
2. Optimized JOIN conditions for better execution plan
3. Added meaningful table aliases
4. Consider indexes on:
 - event_rsvp(user_id, event_id, attendance_status, event_type)
 - friendship_status(user_a_id, user_b_id, status)
5. Efficient GROUP BY with minimal columns
*/