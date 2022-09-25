# Write your MySQL query statement below
SELECT class
FROM(
    SELECT class, COUNT(*) as count
    FROM Courses
    GROUP BY class
    HAVING count >= 5
    ) AS T
