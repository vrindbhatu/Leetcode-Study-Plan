# Write your MySQL query statement below
SELECT user_id, MAX(time_stamp) as last_stamp
FROM Logins
WHERE YEAR(DATE(time_stamp)) = '2020'
GROUP BY user_id
# ORDER BY MAX(DATE(time_stamp)) 