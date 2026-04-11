-- ============================================================================
-- DAY 37: SQL MINI PROJECT (FINAL MASTER SCRIPT)
-- PROJECT: Student Performance & Course Analytics System
-- TOOL: MySQL Workbench
-- ============================================================================

-- ❓ WHAT IS THIS PROJECT?
-- A real-world SQL project that demonstrates database design,
-- data insertion, and analytical querying using SQL.

-- ❓ WHY ARE WE DOING THIS?
-- To understand how SQL is used in real companies to:
-- 1. Design databases
-- 2. Store structured data
-- 3. Analyze and answer business questions

-- ❓ WHAT WILL WE SEE AT THE END?
-- - Student distribution across departments
-- - Course popularity
-- - Student performance analysis
-- - Usage of joins & aggregate functions
-- ============================================================================


-- ============================================================================
-- STEP 1: CREATE DATABASE
-- ============================================================================

-- ❓ QUESTION:
-- Why create a new database?
-- To isolate project data and avoid confusion with other databases.

-- code 1 


-- code 2



-- ============================================================================
-- STEP 2: ER DESIGN THINKING (VERY IMPORTANT)
-- ============================================================================

-- ENTITIES:
-- Departments → Students → Enrollments ← Courses

-- RELATIONSHIPS:
-- 1 Department → Many Students
-- 1 Student → Many Courses
-- Many-to-Many handled using ENROLLMENTS table

-- ❓ QUESTION:
-- Why not store everything in one table?
-- ❌ Causes redundancy and inconsistency
-- ✅ Proper normalization avoids problems


-- ============================================================================
-- STEP 3: CREATE TABLES (DDL)
-- ============================================================================

-- --------------------
-- DEPARTMENTS TABLE
-- --------------------
-- ❓ Why separate department table?
-- To avoid repeating department names again and again

-- code3


-- --------------------
-- STUDENTS TABLE
-- --------------------
-- ❓ Why FOREIGN KEY here?
-- To ensure students belong only to valid departments

-- code4







-- --------------------
-- COURSES TABLE
-- --------------------
-- ❓ Why separate courses?
-- One course can have many students

-- code5






-- --------------------
-- ENROLLMENTS TABLE
-- --------------------
-- ❓ Why this table?
-- To handle Many-to-Many relationship between students and courses

-- code6





-- ============================================================================
-- STEP 4: INSERT SAMPLE DATA (DML)
-- ============================================================================

-- ❓ Why insert data?
-- Without data, analysis is impossible

-- code7









-- ============================================================================
-- STEP 5: ANALYTICAL QUESTIONS (THIS IS THE FUN PART )
-- ============================================================================

-- ❓ QUESTION 1:
-- How many students are there in each department?

-- code8



-- ❓ QUESTION 2:
-- Which courses are most popular?

-- code9


-- ❓ QUESTION 3:
-- Show student names along with their department names

-- code10



-- ❓ QUESTION 4:
-- What is the average marks scored in each course?

-- code11



-- ❓ QUESTION 5:
-- Which students scored more than 85 marks and in which course?

-- code12







-- ============================================================================
-- FINAL INTERVIEW SUMMARY
-- ============================================================================

-- This project demonstrates:
-- ✔ Database design using SQL
-- ✔ Proper use of primary & foreign keys
-- ✔ Handling real relationships using joins
-- ✔ Writing analytical SQL queries
-- ✔ End-to-end SQL thinking for Data Analyst roles

-- ============================================================================
-- ADDITIONAL ANALYTICAL QUESTIONS (STUDENT ANALYTICS) - If you want you can again do deep analysis and solve the questions 
-- PURPOSE: Strengthen analytical thinking + interview readiness
-- ============================================================================

-- ❓ QUESTION 6:
-- List all students along with the number of courses they are enrolled in

-- THINK:
-- Count enrollments per student

SELECT s.student_name,
       COUNT(e.course_id) AS total_courses
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_name;


-- ❓ QUESTION 7:
-- Find students who are enrolled in MORE THAN 1 course

-- THINK:
-- GROUP BY + HAVING

SELECT s.student_name,
       COUNT(e.course_id) AS course_count
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_name
HAVING COUNT(e.course_id) > 1;


-- ❓ QUESTION 8:
-- Display department-wise average marks

-- THINK:
-- Join students → departments → enrollments

SELECT d.dept_name,
       AVG(e.marks) AS avg_marks
FROM departments d
JOIN students s ON d.dept_id = s.dept_id
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY d.dept_name;


-- ❓ QUESTION 9:
-- Identify the TOP performing student (highest total marks)

-- THINK:
-- SUM marks per student
-- ORDER BY descending

SELECT s.student_name,
       SUM(e.marks) AS total_marks
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_name
ORDER BY total_marks DESC
LIMIT 1;


-- ❓ QUESTION 10:
-- Find the MOST popular course (highest enrollments)

SELECT c.course_name,
       COUNT(e.student_id) AS enrollment_count
FROM courses c
JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_name
ORDER BY enrollment_count DESC
LIMIT 1;


-- ❓ QUESTION 11:
-- List students who scored ABOVE the overall average marks

-- THINK:
-- Subquery required

SELECT s.student_name, e.marks
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
WHERE e.marks >
      (SELECT AVG(marks) FROM enrollments);


-- ❓ QUESTION 12:
-- Show department-wise student count and total enrollments

SELECT d.dept_name,
       COUNT(DISTINCT s.student_id) AS total_students,
       COUNT(e.course_id) AS total_enrollments
FROM departments d
LEFT JOIN students s ON d.dept_id = s.dept_id
LEFT JOIN enrollments e ON s.student_id = e.student_id
GROUP BY d.dept_name;


-- ❓ QUESTION 13:
-- Find students who are NOT enrolled in any course

-- THINK:
-- LEFT JOIN + NULL check

SELECT s.student_name
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id
WHERE e.course_id IS NULL;


-- ❓ QUESTION 14:
-- Display course-wise highest and lowest marks

SELECT c.course_name,
       MAX(e.marks) AS highest_marks,
       MIN(e.marks) AS lowest_marks
FROM courses c
JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_name;


-- ❓ QUESTION 15:
-- Rank courses based on average marks (basic ranking logic)

SELECT c.course_name,
       AVG(e.marks) AS avg_marks
FROM courses c
JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_name
ORDER BY avg_marks DESC;


-- ============================================================================
-- INTERVIEW-LEVEL THINKING QUESTIONS (DISCUSSION ONLY)
-- ============================================================================

-- ❓ Why LEFT JOIN instead of INNER JOIN in some queries?
-- ❓ Why DISTINCT is used with COUNT?
-- ❓ When do we use HAVING instead of WHERE?
-- ❓ Why subquery is required in Question 11?
-- ❓ How would this scale for 1 million students?

