# Write your MySQL query statement below
select u.name, sum(t.amount) as balance
FROM Users u, Transactions t
where u.account = t.account
Group by t.account
having sum(t.amount) > 10000
