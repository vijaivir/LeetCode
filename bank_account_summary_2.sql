# Write your MySQL query statement below
SELECT name, total AS balance
FROM Users 
JOIN
    (SELECT account, SUM(amount) AS total
    FROM Transactions
    GROUP BY account) AS T
ON Users.account = T.account
WHERE T.total > 10000
