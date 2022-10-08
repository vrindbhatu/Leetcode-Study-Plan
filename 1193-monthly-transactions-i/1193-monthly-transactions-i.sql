# Write your MySQL query statement below

SELECT DATE_FORMAT(trans_date,"%Y-%m") as month,country, COUNT(*) as trans_count,COUNT(IF(state = "approved",1,NULL)) approved_count, SUM(amount) AS trans_total_amount, SUM(IF(state = "approved",amount,0)) AS approved_total_amount
FROM Transactions
GROUP BY 1,2

# select date_format(trans_date,"%Y-%m") as month, country, count(*) as trans_count, count(if (state = "approved",1,NULL)) as approved_count, sum(amount) as trans_total_amount, sum(if(state = "approved",amount,0)) as approved_total_amount
# from Transactions
# GROUP BY 1,2
