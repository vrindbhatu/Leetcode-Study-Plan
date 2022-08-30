# Write your MySQL query statement below
UPDATE Salary
SET sex = 
Case 
 WHEN sex = 'f' THEN 'm'
 WHEN sex = 'm' THEN 'f'
END