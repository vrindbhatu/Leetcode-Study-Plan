# Write your MySQL query statement below
select email as Email
from Person
GROUP BY email
HAVING count(id) > 1

