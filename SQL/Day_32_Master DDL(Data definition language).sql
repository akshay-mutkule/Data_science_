-- =============================================================================
-- DAY 32: DATA DEFINITION LANGUAGE (DDL)
show databases;

-- Tool: MySQL Workbench
-- Goal: Learn how to design tables and apply rules on data
-- =============================================================================


-- =============================================================================
-- SECTION 1: RECAP (FROM DAY 31)
-- =============================================================================

-- SQL is used to interact with databases
-- Database stores structured data
-- Previously learned:
-- CREATE DATABASE
-- USE DATABASE
-- DROP DATABASE

-- Today we will learn:
-- How to create tables
-- How to modify table structure
-- How to apply constraints (Constraints mean rules to the columns)


-- =============================================================================
-- SECTION 2: WHAT IS DDL?
-- =============================================================================

-- DDL = Data Definition Language

-- DDL is used to:
-- Define database structure
-- Create tables
-- Modify table design
-- Remove tables

-- DDL works on:
-- Structure (Schema)
-- NOT on actual data

-- Main DDL Commands:
-- CREATE
-- ALTER
-- DROP
-- TRUNCATE
-- RENAME


-- =============================================================================
-- SECTION 3: WHAT IS A TABLE?
-- =============================================================================

-- A table stores data in rows and columns

-- Example: Employees Table
-- emp_id      -> Employee ID
-- emp_name    -> Employee Name
-- salary      -> Salary
-- dept_id     -> Department ID

-- Important:
-- Columns and data types must be defined BEFORE inserting data


-- =============================================================================
-- SECTION 4: DATABASE SELECTION (MANDATORY)
-- =============================================================================

-- SYNTAX:
-- USE database_name;
-- 1code

use company_db;

-- =============================================================================
-- SECTION 5: DATA TYPES
-- =============================================================================

-- INT       -> Whole numbers/Numerical numbers
-- BIGINT    -> Large numbers
-- VARCHAR   -> Text values
-- DATE      -> Date values
-- CHAR      -> Only add the character values

-- Example:
-- emp_id INT
-- emp_name VARCHAR(50)
-- joining_date DATE



-- =============================================================================
-- SECTION 6: CREATE TABLE
-- =============================================================================

-- CREATE TABLE is used to create new tables

-- SYNTAX:
-- CREATE TABLE table_name (
--     column_name datatype,
--     column_name datatype
-- );

-- Example: Create Departments Table
-- 2code
CREATE TABLE departments(
dept_id INT PRIMARY KEY,
dept_name VARCHAR(50) UNIQUE
);

SELECT * FROM departments;




-- Example: Create Employees Table
-- 3code
CREATE TABLE employees(
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50) NOT NULL,
dept_id INT,
salary INT,
joining_date DATE,
FOREIGN KEY (dept_id) references departments(dept_id)
);
SELECT *from employees;
ALTER TABLE employees ADD email VARCHAR(100);
SELECT *from employees;
-- =============================================================================
-- SECTION 7: ALTER TABLE
-- =============================================================================

-- ALTER TABLE is used to modify table structure (Only structure , no data inside it)

-- ----------------------------
-- ADD COLUMN - (This is used to add columns in table with sepcified datatypes)
-- ----------------------------

-- SYNTAX:
-- ALTER TABLE table_name ADD column_name datatype;
-- 4code (Add email column in employee)




-- QUICK CHEATSHEET MOST WIDELY USED :
-- Purpose         | Query
-- ----------------|----------------------------
-- See databases   | SHOW DATABASES;
-- Use database    | USE db_name;
-- See tables      | SHOW TABLES;
-- Table structure | DESC table_name;
-- See table data  | SELECT * FROM table_name;


-- ----------------------------
-- MODIFY COLUMN
-- ----------------------------

-- SYNTAX:
-- ALTER TABLE table_name MODIFY column_name new_datatype;
-- 5code (Change the salary datatype from int to Bigint)
ALTER TABLE employees MODIFY salary BIGINT;


-- ----------------------------
-- DROP COLUMN
-- ----------------------------

-- SYNTAX:
-- ALTER TABLE table_name DROP column_name;
-- 6code (Drop email column)

ALTER TABLE employees DROP email;
select * from employees;


-- =============================================================================
-- SECTION 8: TRUNCATE TABLE
-- =============================================================================

-- TRUNCATE removes all rows but keeps table structure
TRUNCATE TABLE employees;
SELECT * FROM employees;
-- SYNTAX:
-- TRUNCATE TABLE table_name;
-- 7code



-- =============================================================================
-- SECTION 9: RENAME TABLE
-- =============================================================================

-- Used to rename a table

-- SYNTAX:
-- RENAME TABLE old_name TO new_name;
-- 8code (Rename employees to Staff)
RENAME TABLE employees TO staff;
SELECT * FROM staff;



-- =============================================================================
-- SECTION 10: DROP TABLE
-- =============================================================================

-- DROP deletes table permanently

-- SYNTAX:
-- DROP TABLE table_name;
-- 9code (Drop Staff table)
DROP TABLE staff;




-- =============================================================================
-- SECTION 11: CONSTRAINTS (DATA RULES)
-- =============================================================================

-- Constraints are rules applied on columns
-- Used to maintain data integrity (Integrity - Data security)
-- This rules restrict to add the type of data we required from user to get added in columns 

-- Types:
-- PRIMARY KEY
-- NOT NULL
-- UNIQUE
-- FOREIGN KEY


-- =============================================================================
-- PRIMARY KEY
-- =============================================================================

-- PRIMARY KEY:
-- Uniquely identifies each row
-- Due to this keys the column Cannot be NULL
-- Due to this keys the column Cannot have duplicates entries / values
-- We can add Only ONE primary key per table

-- SYNTAX:
-- 10code
CREATE TABLE students(
std_id INT PRIMARY KEY,
std_name VARCHAR(50));

select * FROM students;


-- Few Invalid Example while entering the entries in columns (Duplicate Key):
-- Lets assume if student_id is my primary key in table :
-- INSERT INTO students VALUES (1,'Rahul');
-- INSERT INTO students VALUES (1,'Amit');


-- =============================================================================
-- NOT NULL
-- =============================================================================

-- NOT NULL:
-- Column must always have value IT CAN'T REMAIN VACANT 

-- SYNTAX:
-- 11code (Course name can never be null)


-- Invalid Example:
-- INSERT INTO courses VALUES (101,NULL);


-- =============================================================================
-- UNIQUE
-- =============================================================================

-- UNIQUE:
-- No duplicate values allowed in column 
-- NULL allowed once

-- SYNTAX:
-- 12code (Set email ids to be unique )

CREATE TABLE users(
user_id INT PRIMARY KEY,
email VARCHAR(50)UNIQUE);
-- Invalid Example:
-- INSERT INTO users VALUES (1,'test@gmail.com');
-- INSERT INTO users VALUES (2,'test@gmail.com');


-- =============================================================================
-- FOREIGN KEY
-- =============================================================================

-- FOREIGN KEY:
-- Creates relationship between two tables
-- Maintains referential integrity (Refrential integrity mean Connection between 2 tables)
-- Child table depends on parent table (Relate with python class and object concept)

-- SYNTAX:
-- 13code

-- Parent table : (Primary key )
CREATE TABLE users1(
user_id INT PRIMARY KEY,
email VARCHAR(50)UNIQUE);

-- Child Table :(Foreign key)

CREATE TABLE orders(
order_id INT PRIMARY KEY,
cust_id INT NOT null,
user_id int unique);
-- Primary Key → Uniquely identifies a record in the same table
-- Foreign Key → Connects one table to another table
-- orders.customer_id depends on users.user_id

-- Meaning:
-- You cannot create an order for a customer that does not exist in the users table

-- Examples : 

-- VALID: 
-- user_id exists in users table
-- INSERT INTO users VALUES (1, 'Rahul');
-- INSERT INTO orders VALUES (101, 1);

-- INVALID: 
-- customer_id does not exist in users table
-- INSERT INTO orders VALUES (102, 5);  -- Foreign Key violation



-- =============================================================================
-- SECTION 12: COMMON BEGINNER MISTAKES
-- =============================================================================

-- Forgetting PRIMARY KEY
-- Wrong data types
-- Ignoring FOREIGN KEY
-- Dropping tables accidentally


-- =============================================================================
-- SECTION 13: INTERVIEW QUESTIONS (REVISION)
-- =============================================================================

-- What is DDL?
-- Difference between DROP and TRUNCATE?
-- Difference between PRIMARY KEY and UNIQUE?
-- Why FOREIGN KEY is important?
-- Difference between ALTER and UPDATE?


-- =============================================================================
-- SECTION 14: PRACTICE TASKS
-- =============================================================================

-- Task 1:
-- Create students table with PRIMARY KEY and NOT NULL

CREATE TABLE students(
std_id INT PRIMARY KEY,
std_name VARCHAR(50),
std_class varchar(50));
-- Task 2:
-- Create courses table with UNIQUE column
CREATE TABLE courses(
course_id INT PRIMARY KEY,
course_name varchar(50));
-- Task 3:
-- Create users and orders table using FOREIGN KEY

-- Task 4:
-- Try inserting wrong data and observe errors


-- =============================================================================
-- DAY 32 SUMMARY
-- =============================================================================

-- Learned table creation
-- Learned structure modification
-- Learned all constraints
-- Learned schema design fundamentals


