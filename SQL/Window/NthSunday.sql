DECLARE @N INT = 14;
-- Change N to the desired Sunday number
SELECT DATEADD(
        day,
        (@N - 1) * 7 - (DATEPART(dw, GETDATE()) + @@DATEFIRST - 2) % 7,
        GETDATE()
    ) AS NthSunday


-- Replace @N with the desired Sunday number.
-- DATEADD() adds the appropriate number of days to the current date to get to the Nth Sunday.
-- (@N - 1) * 7 calculates the number of days to add to get to the Nth Sunday.
--(DATEPART(dw, GETDATE()) + @@DATEFIRST - 2) % 7 calculates the difference in days between the current day of the week and
--  Sunday, adjusting for the DATEFIRST setting, which determines the first day of the week. 
--  This is subtracted from the total days to add to ensure we land on a Sunday.