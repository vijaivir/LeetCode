# Write your MySQL query statement below
SELECT
    (CASE
        WHEN MOD(id, 2) != 0 AND total_count != id THEN id + 1
        WHEN MOD(id, 2) != 0 AND total_count = id THEN id
        ELSE id - 1
    END) AS id,
    student
FROM
    seat,
    (SELECT
        COUNT(*) AS total_count
    FROM
        seat) AS seat_count
ORDER BY id ASC;
