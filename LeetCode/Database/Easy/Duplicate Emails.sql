-- Write your PostgreSQL query statement below
WITH Sol(Email, Count) AS (SELECT email, count(email) 
From Person p
Group by email)

select email AS "Email"
FROM Sol
Where count > 1
