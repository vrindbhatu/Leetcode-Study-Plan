# Write your MySQL query statement below

SELECT DATE_FORMAT(trans_date,"%Y-%m") as month,country, COUNT(*) as trans_count,COUNT(IF(state = "approved",1,NULL)) approved_count, SUM(amount) AS trans_total_amount, SUM(IF(state = "approved",amount,0)) AS approved_total_amount
FROM Transactions
GROUP BY 1,2