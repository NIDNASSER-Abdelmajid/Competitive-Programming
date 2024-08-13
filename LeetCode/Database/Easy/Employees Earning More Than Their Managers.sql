-- Write your PostgreSQL query statement below
SELECT E1.NAME AS Employee 
from EMPLOYEE E1
JOIN EMPLOYEE E2
on E1.managerId = E2.id
where E1.salary>E2.salary