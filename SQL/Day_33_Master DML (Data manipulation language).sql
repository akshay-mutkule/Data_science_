-- =====================================================
-- Day 33: Data Manipulation Language (DML)
-- Topic: INSERT, UPDATE, DELETE, SELECT, WHERE, AND, OR, NOT, IN
-- Tool: MySQL Workbench
-- =====================================================

-- =====================================================
-- STEP 1: Select Database (Always Do This First)
-- =====================================================
-- 1code
	USE company_db;
    show databases;
    show tables;


-- Check current database
-- 2code



-- =====================================================
-- WHAT IS DML?
-- =====================================================

-- DML = Data Manipulation Language
-- Used to WORK WITH DATA inside tables
-- DML does NOT change table structure (DDL does that)

-- Main DML Commands:
-- INSERT  -> Add new records
-- UPDATE  -> Modify existing records
-- DELETE  -> Remove records
-- SELECT  -> Retrieve records

-- =====================================================
-- INSERT COMMAND (Adding Data)
-- =====================================================

-- ---------------------------
-- INSERT SYNTAX (Single Row)
-- ---------------------------
-- INSERT INTO table_name (column1, column2, ...)
-- VALUES (value1, value2, ...);


-- Example: Insert departments
-- 3code
INSERT INTO departments (dept_id,dept_name)
VALUES (1,"HR");
-- * All the records

-- 4code
INSERT INTO departments (dept_id,dept_name)
VALUES (2,"CEO");


-- 5code
INSERT INTO departments (dept_id,dept_name)
VALUES (3,"PO");

-- View inserted data
-- 6code

SELECT *FROM departments;
-- ---------------------------
-- INSERT SYNTAX (Multiple Rows) 
-- ---------------------------
-- Insert values in employee table
-- INSERT INTO table_name
-- VALUES
-- (row1),
-- (row2),
-- (row3);

-- 7code
CREATE TABLE employees(
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50)NOT NULL,
dept_id INT,
salary INT,
joining_date Date,
FOREIGN KEY (dept_id) REFERENCES departments(dept_id));


SELECT*FROM employees;

INSERT INTO employees (emp_id, emp_name, dept_id, salary, joining_date)
VALUES 
(101, 'Akshay', 1, 50000, '2025-09-10'),
(102, 'Saurabh', 3, 50000, '2025-09-09'),
(104, 'Arjun', 1, 50000, '2025-06-10'),
(105, 'Anna', 2, 50000, '2025-10-10');
-- View employees table
-- 8code
SELECT * FROM employees;

-- ---------------------------
-- COMMON INSERT ERRORS
-- ---------------------------

-- PRIMARY KEY violation (Duplicate ID)
-- INSERT INTO departments VALUES (1, 'Sales');

-- NOT NULL violation
-- INSERT INTO employees VALUES (105, NULL, 1, 40000, '2025-05-01');

-- FOREIGN KEY violation
-- INSERT INTO employees VALUES (106, 'Ravi', 10, 45000, '2025-05-10');

-- =====================================================
-- SELECT COMMAND (Viewing Data)
-- =====================================================

-- ---------------------------
-- SELECT ALL COLUMNS
-- ---------------------------

-- 9code
select * from employees;

-- ---------------------------
-- SELECT SPECIFIC COLUMNS (Display emp_name & salary from employeees)
-- ---------------------------

-- 10code
select emp_id, emp_name from employees;

-- ---------------------------
-- COLUMN ALIAS (Readable Output) - Alias mean --> giving  temporary name to Columns / variables /queries
-- ---------------------------

-- 11code

select emp_id AS "Employee id", emp_name AS "Name" from employees;
-- =====================================================
-- WHERE CLAUSE (Filtering Records)
-- =====================================================

-- WHERE is used to filter rows based on condition

-- ---------------------------
-- BASIC WHERE CONDITION
-- ---------------------------

-- See employess whose salary is greater than 50000
-- 12code
select * from employees
where salary>50000;


-- ---------------------------
-- AND OPERATOR
-- Both conditions must be TRUE
-- ---------------------------

-- see employees from 1 department whose salary> 45000
-- 13code

select * from employees
where dept_id = 1 and salary >45000;


-- ---------------------------
-- OR OPERATOR
-- Any one condition TRUE
-- ---------------------------

-- see all employees from any department from 1 ,2
-- 14code

select * from employees
where dept_id = 1 or dept_id = 2;


-- ---------------------------
-- NOT OPERATOR
-- Reverse the condition
-- ---------------------------

-- see employees from all department accept dept 3
-- 15code
select * from employees
where not dept_id = 3;




-- ---------------------------
-- IN OPERATOR
-- Multiple values filter
-- ---------------------------

-- see all employees from department 1 and 3 
-- 16code


select * from employees
where dept_id IN (1,3);

-- =====================================================
-- UPDATE COMMAND (Modify Data)
-- =====================================================

-- ---------------------------
-- UPDATE SYNTAX
-- ---------------------------
-- UPDATE table_name
-- SET column = value
-- WHERE condition;

-- ---------------------------
-- Update Single Column (Update salary of emp 102 to 65000)
-- ---------------------------
-- 17code

select * from employees;
update employees
set salary = 80000
where dept_id = 1;
select dept_id, salary from employees
where emp_id = 1;
select * from employees;

-- Check result
-- 18code

select * from employees;
-- ---------------------------
-- Update Multiple Columns (Set salary of employee 103 in department 2 as 70000)
-- ---------------------------
-- 19code

SELECT * FROM employees;
UPDATE employees
set salary = 70000,
dept_id = 3
where emp_id = 105;
select *from employees;




-- ---------------------------
-- DANGER EXAMPLE (Never Do)
-- ---------------------------

-- UPDATE employees SET salary = 30000;

-- This updates ALL rows (very dangerous)

-- =====================================================
-- DELETE COMMAND (Remove Records)
-- =====================================================

-- ---------------------------
-- DELETE SYNTAX
-- ---------------------------
-- DELETE FROM table_name
-- WHERE condition;

-- ---------------------------
-- Delete Single Record (Delete the record of ID 104)
-- ---------------------------
-- 20code
delete FROM employees
where emp_id = 104;

select*from employees;

-- Check result
-- 21code

-- ---------------------------
-- DANGER EXAMPLE
-- ---------------------------

-- DELETE FROM employees;

-- This deletes ALL rows

-- =====================================================
-- DELETE vs TRUNCATE (Important Concept)
-- =====================================================

-- DELETE:
-- Can use WHERE function
-- Can rollback (with transactions)
-- Slower

-- TRUNCATE:
-- No WHERE allowed
-- Faster
-- Cannot rollback
-- Removes all rows at once

-- =====================================================
-- PRACTICE QUERIES 
-- =====================================================

-- 1. Show employees with salary greater than 55000
select * from employees
where salary> 55000;

-- 2. Show employees from HR department (dept_id = 1)
select *from employees
where dept_id = 1;
-- 3. Increase salary of Rahul by 5000

UPDATE employees
set salary = salary + 5000
where emp_id = 101;
select*from employees;
-- 4. Delete employee with emp_id = 101
delete from employees
where emp_id =101;
select *from emploees;
-- 5. Display only names and joining dates
select emp_name , joining_date from employees;

-- =====================================================
-- DAY 33 SUMMARY
-- =====================================================

-- You Learned:

-- INSERT -> Add data
-- UPDATE -> Modify data
-- DELETE -> Remove data
-- SELECT -> Retrieve data
-- WHERE  -> Filter rows
-- AND, OR, NOT -> Logical filtering
-- IN -> Multi-value filtering

-- You can now CONTROL table data safely and professionally.

-- =====================================================
-- NEXT DAY PREVIEW (DAY 34)
-- =====================================================

-- Aggregate Functions:
-- COUNT, SUM, AVG, MIN, MAX

-- GROUP BY
-- ORDER BY
-- HAVING
-- COMMIT & ROLLBACK

-- =====================================================
-- SQL QUERY ORDER (HOW WE WRITE SQL)
-- =====================================================

-- =====================================================
-- SQL QUERY ORDER (HOW WE WRITE SQL)
-- =====================================================

-- SELECT
-- FROM
-- WHERE
-- GROUP BY
-- HAVING
-- ORDER BY
-- LIMIT

-- =====================================================
-- SQL QUERY EXECUTION ORDER (HOW SQL EXECUTES INTERNALLY)
-- =====================================================

-- 1) FROM       → Identify the table
-- 2) WHERE      → Filter rows
-- 3) GROUP BY   → Make groups
-- 4) HAVING     → Filter groups
-- 5) SELECT     → Choose columns
-- 6) ORDER BY   → Sort output
-- 7) LIMIT      → Restrict rows (if used)

-- =====================================================
-- IMPORTANT NOTE FOR STUDENTS
-- =====================================================
-- SQL does NOT execute queries in the same order
-- in which we write them.
-- SQL follows the EXECUTION ORDER shown above.



