-- =====================================================
-- Day 35: The Art of Joining Tables in SQL
-- Tool: MySQL
-- Goal: Combine data from multiple tables confidently
-- =====================================================


-- =====================================================
-- STEP 1: USE DATABASE
-- =====================================================

-- 1code

-- =====================================================
-- WHY DO WE NEED JOINS?
-- =====================================================

-- In real-world databases, data is NEVER stored in one table
-- To avoid:
-- 1. Data redundancy (Retundancy - duplication of data within a database.)
-- 2. Memory wastage
-- 3. Update anomalies (Anamolies means DIRTY DATA/errors in data )

-- Example:
-- employees   -> employee details
-- departments -> department details

-- To see employee name + department name together,
-- we must COMBINE tables using JOINs

-- Definition:
-- A JOIN combines rows from two or more tables
-- based on a related column


-- =====================================================
-- TABLE RELATIONSHIP USED
-- =====================================================

-- employees.emp_id    -> Primary Key
-- employees.dept_id   -> Foreign Key
-- departments.dept_id -> Primary Key

-- This relationship enables JOIN operations

-- TYPES OF JOINS IN SQL 
-- INNER JOIN
-- LEFT JOIN 
-- RIGHT JOIN 
-- FULL OUTER JOIN (LEFT UNION RIGHT)
-- CROSS JOIN 

-- =====================================================
-- INNER JOIN
-- =====================================================

-- INNER JOIN returns ONLY matching records
-- Rows without matching keys are excluded

-- Syntax:
-- SELECT columns
-- FROM table1
-- INNER JOIN table2
-- ON condition;

-- 2code 

-- Use case:
-- Show employees who are assigned to valid departments
-- Most commonly used JOIN in real-world projects


-- =====================================================
-- LEFT JOIN
-- =====================================================

-- LEFT JOIN returns:
-- ALL rows from LEFT table
-- Matching rows from RIGHT table
-- Non-matching rows as NULL

-- 3code

-- Use case:
-- Show ALL employees
-- Even if department is not assigned

-- Key rule:
-- LEFT JOIN never loses LEFT table data


-- =====================================================
-- RIGHT JOIN
-- =====================================================

-- RIGHT JOIN returns:
-- ALL rows from RIGHT table
-- Matching rows from LEFT table

-- 4code

-- Use case:
-- Show ALL departments
-- Even if no employees exist

-- Note:
-- RIGHT JOIN is used less often
-- Can be rewritten using LEFT JOIN by swapping tables


-- =====================================================
-- FULL OUTER JOIN (MySQL WORKAROUND)
-- =====================================================

-- FULL OUTER JOIN returns:
-- All rows from BOTH tables
-- Matching + non-matching records

-- MySQL does NOT support FULL OUTER JOIN directly
-- We simulate it using LEFT JOIN + UNION + RIGHT JOIN

-- 5code

-- Use case:
-- Complete data comparison
-- Data auditing and reconciliation


-- =====================================================
-- CROSS JOIN
-- =====================================================

-- CROSS JOIN produces Cartesian Product
-- Every row from table A joins with every row from table B

-- 6code

-- Example:
-- 5 employees × 3 departments = 15 rows

-- Use case:
-- Rare in real-world applications
-- Used in combinations, testing, simulations


-- =====================================================
-- JOINING MORE THAN TWO TABLES
-- =====================================================

-- SQL allows joining multiple tables in one query
-- Join order and conditions must be clear

-- Example structure:

-- =====================================================
-- THIS QUERY COMBINES DATA FROM 3 RELATED TABLES
-- =====================================================
-- Tables involved:
-- 1) employees
-- 2) departments
-- 3) locations

-- Goal:
-- To display employee name,
-- their department name,
-- and the location of that department
-- in a single result set

-- NOT USED WIDELY / JUST AN OVERVIEW 
-- SELECT
--     e.emp_name,
--     d.dept_name,
--     l.location_name
-- FROM employees e
-- INNER JOIN departments d ON e.dept_id = d.dept_id         (This query Match employees with there department)
-- INNER JOIN locations l ON d.location_id = l.location_id;  (This query match department with there locations)

-- =====================================================
-- OUTPUT OF THE QUERY
-- =====================================================
-- emp_name | dept_name | location_name
-- -----------------------------------
-- Rahul   | IT        | Bangalore
-- Anjali  | HR        | Pune
-- Amit    | Finance   | Mumbai



-- =====================================================
-- COMMON BEGINNER MISTAKES
-- =====================================================

-- Forgetting ON condition (creates Cartesian product)
-- Confusing LEFT JOIN with INNER JOIN
-- Expecting FULL OUTER JOIN to work directly in MySQL
-- Using wrong join key columns

-- EXAMPLE 
-- Wrong joins Wwe may try
-- ON e.emp_id = d.dept_id      -- ❌ No relationship
-- ON e.dept_id = d.dept_name   -- ❌ Different data types

-- Result:
-- Empty output
-- Duplicate rows
-- Confusion


-- =====================================================
-- PRACTICE QUERIES
-- =====================================================

-- 1. Display employee names with department names
-- 2. Show all employees even if department is NULL
-- 3. Show all departments even if no employees exist
-- 4. Find employees without a department
-- 5. Create FULL OUTER JOIN result using UNION


-- =====================================================
-- DAY 35 SUMMARY
-- =====================================================

-- Learned why JOINs are required
-- Understood table relationships
-- INNER JOIN: matching records only
-- LEFT JOIN: all left table rows
-- RIGHT JOIN: all right table rows
-- FULL OUTER JOIN: simulated in MySQL
-- CROSS JOIN: Cartesian product
-- Confidently joining multiple tables


-- =====================================================
-- NEXT DAY PREVIEW (DAY 36)
-- =====================================================

-- Subqueries
-- Nested SELECT statements
-- WHERE vs FROM subqueries
-- Real-world filtering scenarios

