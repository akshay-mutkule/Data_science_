-- =============================================================================
-- DAY 31: GETTING STARTED WITH SQL & DATABASES
-- Audience: Absolute Beginners
-- Tool: MySQL Workbench
-- =============================================================================


-- =============================================================================
-- SECTION 1: WHAT IS DATA?
-- =============================================================================

-- Structured Data:
-- Data stored in rows and columns (tables)
-- Example: Employee table

-- Unstructured Data:
-- Images, videos, audio, free text

-- Semi-Structured Data:
-- JSON, XML (commonly used in APIs)


-- =============================================================================
-- SECTION 2: WHAT IS A DATABASE?
-- =============================================================================

-- A database is an organized collection of data stored electronically.

-- Real-world analogy:
-- Library   -> Database
-- Books     -> Tables
-- Pages     -> Rows
-- Columns   -> Attributes


-- =============================================================================
-- SECTION 3: DBMS vs RDBMS
-- =============================================================================

-- DBMS:
-- Software used to store and manage data

-- RDBMS:
-- Data stored in tables with relationships

-- Example relationship:
-- One department -> Many employees


-- =============================================================================
-- SECTION 4: WHAT IS SQL?
-- =============================================================================

-- SQL (Structured Query Language) is used to:
-- Create databases
-- Create tables
-- Insert data
-- Retrieve data
-- Update data
-- Secure data

-- SQL is a declarative language:
-- You tell WHAT you want, not HOW to get it


-- =============================================================================
-- SECTION 5: MYSQL INTRODUCTION
-- =============================================================================

-- MySQL is an RDBMS that uses SQL

-- Components:
-- MySQL Server  -> Stores data
-- MySQL Workbench -> GUI tool to write SQL
-- MySQL CLI -> Command line tool


-- =============================================================================
-- SECTION 6: DATABASE HIERARCHY
-- =============================================================================

-- MySQL Server
--    └── Database
--         └── Tables
--              └── Rows
--                   └── Columns


-- =============================================================================
-- ========================= PRACTICAL EXECUTION START =========================
-- =============================================================================


-- =============================================================================
-- SECTION 7: VIEW ALL DATABASES
-- =============================================================================

-- SYNTAX:
-- SHOW DATABASES;
-- 1code:




-- =============================================================================
-- SECTION 8: CREATE DATABASE
-- =============================================================================

-- SYNTAX:
-- CREATE DATABASE database_name;
-- 2code




-- =============================================================================
-- SECTION 9: USE DATABASE
-- =============================================================================

-- SYNTAX:
-- USE database_name;
-- 3code




-- =============================================================================
-- SECTION 10: VERIFY CURRENT DATABASE
-- =============================================================================

-- SYNTAX:
-- SELECT DATABASE();
-- 4code





-- =============================================================================
-- SECTION 11: CREATE ANOTHER DATABASE
-- =============================================================================

-- SYNTAX:
-- CREATE DATABASE database_name;
-- 5code



-- =============================================================================
-- SECTION 12: SWITCH TO ANOTHER DATABASE
-- =============================================================================

-- SYNTAX:
-- USE database_name;
-- 6code 



-- =============================================================================
-- SECTION 13: DROP DATABASE
-- =============================================================================

-- SYNTAX:
-- DROP DATABASE database_name;

-- WARNING:
-- DROP permanently deletes the database and all data
-- 7code


-- how to create dabase 
-- how to create multiple database '
-- how to use database to store the data 
-- how to switch between the database 
-- how to drop the unnecessary databases 

-- =============================================================================
-- SECTION 14: IMPORTANT SQL TERMINOLOGY
-- =============================================================================

-- SQL -> Query Language
-- MySQL -> Database Software
-- Database -> Container for tables
-- Table -> Stores rows and columns
-- Row -> Single record
-- Column -> Attribute / field


-- =============================================================================
-- SECTION 15: REVISION QUESTIONS
-- =============================================================================

-- What is SQL?
-- Difference between DBMS and RDBMS?
-- What is structured data?
-- Difference between SQL and MySQL?
-- Why SQL is important for Data Analysts?


-- =============================================================================
-- SECTION 16: PRACTICE TASKS
-- =============================================================================

-- TASK 1:
-- Create a database named student_db

-- TASK 2:
-- Switch to student_db

-- TASK 3:
-- Verify current database using SELECT DATABASE();



