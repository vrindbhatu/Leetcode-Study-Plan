/* Write your T-SQL query statement below */
select max(salary) AS SecondHighestSalary
from Employee
WHERE salary NOT IN (SELECT max(salary) from Employee);