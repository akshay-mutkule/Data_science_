-- =====================================================
-- Day 34: Data Transaction Language (DTL) & Aggregate Functions

-- =====================================================
-- STEP 1: USE DATABASE
-- =====================================================

-- 1code
use company_db;

-- Verify active database
-- 2code
select database();

-- =====================================================
-- INTRODUCTION TO DTL
-- =====================================================

-- DTL = Data Transaction Language
-- DTL is used to CONTROL database transactions and permissions
-- It ensures:
-- 1. Data safety
-- 2. Data consistency
-- 3. Controlled access in multi-user environments

-- DTL commands work mainly with DATA CHANGES, not structure


-- =====================================================
-- DTL COMMANDS OVERVIEW
-- =====================================================

-- GRANT    -> Give permissions to users
-- REVOKE  -> Remove permissions from users
-- COMMIT  -> used to save the changes made to the table permanently, the changes gets uploaded in server and things gets saved 
-- ROLLBACK-> Undo only uncommitted changes. Used to get back to the previous permanent status of the table similar to UNDO command.


-- =====================================================
-- TRANSACTIONS IN SQL
-- =====================================================

-- A TRANSACTION is a group of SQL operations
-- All operations succeed together or fail together
-- This process follows ACID principles (Atomicity, Consistency, Isolation, Durability)

-- Common use cases:
-- - Salary updates
-- - Bank transfers
-- - Multi-table inserts

-- 1) SALARY UPDATES
-- Salary updates usually affect multiple employees.
-- If even one update fails, the entire operation should fail.
-- Transactions ensure all salaries are updated together or none are updated.
-- This prevents partial or incorrect salary updates.

-- 2) BANK TRANSFERS
-- Bank transfer involves deducting money from one account
-- and adding it to another account.
-- Both operations must succeed together.
-- Transactions prevent money loss or incorrect balances.

-- 3) MULTI-TABLE INSERTS
-- One operation inserts data into multiple related tables.
-- Example: order, order_items, payment tables.
-- If one insert fails, all inserts should be rolled back.
-- Transactions maintain data consistency across tables.



-- =====================================================
-- STARTING A TRANSACTION
-- =====================================================



-- Temporary inserts
-- 3code
select *from employees;
insert into employees (emp_id,emp_name,dept_id,salary,joining_date)
values (201,"Rohit",1,45000,"2025-04-22"),
(202,"Akanksha",3,65000,"2025-05-22"),
(203,"priyanka",1,400000,"2025-08-22");
-- View data inside transaction
-- 4code


-- =====================================================
-- ROLLBACK (UNDO CHANGES)
-- =====================================================

-- 5code 
ROLLBACK;
-- Data is reverted
-- 6code
SELECT *FROM employees;

-- =====================================================
-- COMMIT (SAVE CHANGES PERMANENTLY)
-- =====================================================

-- 7code

-- 8code

-- 9code

-- Changes are now permanent
-- 10code

-- =====================================================
-- COMMON TRANSACTION MISTAKES
-- =====================================================

-- Forgetting COMMIT
-- Using transactions inconsistently
-- Making changes without rollback safety


-- =====================================================
-- PERMISSIONS: GRANT & REVOKE
-- =====================================================

-- Permissions are important in real projects with multiple users

-- Create test user (optional)
-- CREATE USER 'test_user'@'localhost' IDENTIFIED BY 'Test123';

-- Grant SELECT permission
-- GRANT SELECT ON company_db.employees TO 'test_user'@'localhost';

-- Revoke permission
-- REVOKE SELECT ON company_db.employees FROM 'test_user'@'localhost';



-- =====================================================
-- AGGREGATE FUNCTIONS
-- =====================================================

-- Aggregate functions summarize multiple rows into ONE result

-- COUNT() -> Number of rows
-- 11code
select count(*) as total_employee from employees;
-- SUM() -> Total of numeric column
-- 12code

-- AVG() -> Average value
-- 13code 

-- MIN() -> Minimum value
-- 14code

-- MAX() -> Maximum value
-- 15code


-- =====================================================
-- AGGREGATES WITH WHERE
-- =====================================================

-- Aggregate after filtering
-- 16code
select avg(salary) as avg_salary 
from employees
where dept_id = 1;

-- =====================================================
-- GROUP BY CLAUSE
-- =====================================================

-- GROUP BY divides rows into groups
-- Each group produces one output row

-- Total salary per department
-- 17code
select *from employees;
select dept_id, sum(salary)
from employees
group by dept_id;
-- Employee count per department
-- 18code


-- =====================================================
-- ORDER BY CLAUSE
-- =====================================================

-- Sort results

-- Salary ascending
-- 19code
select emp_name,salary from employees
order  by salary DESC;
-- Salary descending
-- 20code


-- =====================================================
-- HAVING CLAUSE
-- =====================================================

-- HAVING filters aggregated data
-- WHERE cannot filter aggregate results

-- Departments with total salary > 100000
-- 21code

select 
dept_id, sum(salary)  from employees
group by dept_id
having sum(salary)> 100000;
-- =====================================================
-- WHERE vs HAVING (KEY DIFFERENCE) (Most asked interview question)
-- =====================================================

-- WHERE -> Filters rows BEFORE grouping
-- HAVING -> Filters groups AFTER aggregation


-- =====================================================
-- PRACTICE QUERIES
-- =====================================================
select * from employees;
-- 1. Count employees in each department
select dept_id, count(emp_id) from employees
group by dept_id;
-- 2. Show departments with more than 2 employees
SELECT dept_id, COUNT(*) AS employee_count
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 2;

-- 3. Find highest salary per department
SELECT dept_id, MAX(salary) AS highest_salary
FROM employees
GROUP BY dept_id;
-- 4. Show average salary of employees earning above 50000
SELECT AVG(salary) AS average_salary
FROM employees
WHERE salary > 50000;
-- 5. Sort departments by total salary descending
SELECT dept_id, SUM(salary) AS total_salary
FROM employees
GROUP BY dept_id
ORDER BY total_salary DESC;

-- =====================================================
-- DAY 34 SUMMARY
-- =====================================================

-- Covered:
-- Transactions using COMMIT & ROLLBACK
-- Permissions using GRANT & REVOKE
-- Aggregate functions: COUNT, SUM, AVG, MIN, MAX
-- GROUP BY for grouping data
-- ORDER BY for sorting results
-- HAVING for filtering aggregated results

-- Students can now:
-- Safely manage database changes
-- Analyze data using aggregation
-- Write professional SQL queries


-- =====================================================
-- NEXT DAY PREVIEW (DAY 35)
-- =====================================================

-- SQL JOINS:
-- INNER JOIN
-- LEFT JOIN
-- RIGHT JOIN
-- FULL JOIN
-- Real-world multi-table analysis

