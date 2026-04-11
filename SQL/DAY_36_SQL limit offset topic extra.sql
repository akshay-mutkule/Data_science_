-- =====================================================
-- DAY_36_SQL : LIMIT & OFFSET (LAST DAY)
-- =====================================================

-- LIMIT → how many rows to show
-- OFFSET → how many rows to skip
-- Used mainly with ORDER BY

-- =====================================================
-- SAMPLE TABLE
-- =====================================================
-- code1

-- =====================================================
-- 1) SHOW ONLY FIRST 3 RECORDS
-- =====================================================
-- code2

-- =====================================================
-- 2) TOP 2 HIGHEST PAID EMPLOYEES
-- =====================================================
-- code3

-- =====================================================
-- 3) LOWEST SALARY EMPLOYEE
-- =====================================================
-- code4

-- =====================================================
-- 4) LIMIT WITH OFFSET (SKIP + SHOW)
-- Skip first 2 rows, show next 2 rows
-- =====================================================
-- code5


-- =====================================================
-- SAME QUERY (MySQL SHORT FORM)
-- =====================================================
-- code6

-- =====================================================
-- 5) REAL-LIFE Iplementation mostly used 
-- =====================================================
-- Page 1 → LIMIT 2 OFFSET 0
-- Page 2 → LIMIT 2 OFFSET 2
-- Page 3 → LIMIT 2 OFFSET 4

-- =====================================================
-- IMPORTANT RULE (TELL STUDENTS)
-- =====================================================
-- ❌ LIMIT without ORDER BY → unpredictable result
-- ✅ ORDER BY + LIMIT → correct & meaningful output


-- “Till now we are limiting rows… but what if we want to filter data based on another query? That’s where Subqueries come in.”

-- PART 2: SUBQUERIES

-- What is Subquery?
-- A query inside another query

-- SYNTAX : 
-- SELECT * FROM table
-- WHERE column = (SELECT something FROM table);

-- 1. FIND EMPLOYEE WITH MAX SALARY (SUBQUERY)
-- 1code

-- Insight:
-- Inner query → finds max salary
-- Outer query → finds that employee

-- 2. EMPLOYEES EARNING MORE THAN AVERAGE
-- 2code

-- 3. SECOND HIGHEST SALARY (INTERVIEW QUESTION)
-- 3code

-- 4. SUBQUERY WITH LIMIT
-- 4code

-- 5. USING SUBQUERY IN FROM (DERIVED TABLE)
-- 5code


-- PRACTISE QUESTIONS

-- Get 3rd highest salary
-- Get employees below average salary
-- Show 2 employees from 2nd page
-- Find employee with minimum salary using subquery


