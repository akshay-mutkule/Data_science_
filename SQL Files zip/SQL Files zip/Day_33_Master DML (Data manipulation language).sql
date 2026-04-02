-- =====================================================
-- Day 33: Data Manipulation Language (DML)
-- Topic: INSERT, UPDATE, DELETE, SELECT, WHERE, AND, OR, NOT, IN
-- Tool: MySQL Workbench
-- =====================================================

-- =====================================================
-- STEP 1: Select Database (Always Do This First)
-- =====================================================
-- 1code



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

-- * All the records


-- 4code


-- 5code


-- View inserted data
-- 6code


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


-- View employees table
-- 8code


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


-- ---------------------------
-- SELECT SPECIFIC COLUMNS (Display emp_name & salary from employeees)
-- ---------------------------

-- 10code


-- ---------------------------
-- COLUMN ALIAS (Readable Output) - Alias mean --> giving  temporary name to Columns / variables /queries
-- ---------------------------

-- 11code


-- =====================================================
-- WHERE CLAUSE (Filtering Records)
-- =====================================================

-- WHERE is used to filter rows based on condition

-- ---------------------------
-- BASIC WHERE CONDITION
-- ---------------------------

-- See employess whose salary is greater than 50000
-- 12code



-- ---------------------------
-- AND OPERATOR
-- Both conditions must be TRUE
-- ---------------------------

-- see employees from 1 department whose salary> 45000
-- 13code




-- ---------------------------
-- OR OPERATOR
-- Any one condition TRUE
-- ---------------------------

-- see all employees from any department from 1 ,2
-- 14code




-- ---------------------------
-- NOT OPERATOR
-- Reverse the condition
-- ---------------------------

-- see employees from all department accept dept 3
-- 15code





-- ---------------------------
-- IN OPERATOR
-- Multiple values filter
-- ---------------------------

-- see all employees from department 1 and 3 
-- 16code




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




-- Check result
-- 18code


-- ---------------------------
-- Update Multiple Columns (Set salary of employee 103 in department 2 as 70000)
-- ---------------------------
-- 19code




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

-- 2. Show employees from HR department (dept_id = 1)

-- 3. Increase salary of Rahul by 5000

-- 4. Delete employee with emp_id = 101

-- 5. Display only names and joining dates

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



