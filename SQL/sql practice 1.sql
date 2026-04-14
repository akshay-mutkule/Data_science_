 CREATE DATABASE temp;
 DROP DATABASE temp;
 CREATE DATABASE temp2;
 DROP DATABASE temp2;
 
 
 CREATE DATABASE college;
 
 USE college;
 
 CREATE TABLE  student (
 id INT PRIMARY KEY,
 name  VARCHAR(50),
 age INT NOT NULL);


INSERT student
 values (1,"Akshay",21),
 (2,"tanuja",20);
 
 select * from student;
 
 
 INSERT INTO student
 (id,name,age)
 values
 (3,"priya",23),
 (4,"sham",34);
 
 
 CREATE DATABASE xyz_company;
 use xyz_company;
 
 CREATE TABLE employee (
 id INT PRIMARY KEY,
 name VARCHAR(50) ,
 salary int);
 
 insert into employee
 (id,name,salary)
 values (1,"Akshay",500000),
 (102,"avi",34000), 
 (103,"tushar",320000);
 
 select * from employee;
 
 CREATE TABLE temp1(
 id int unique);
 
 insert into temp1 values(101);
 select *from temp1;
 
 
 CREATE TABLE emp (
 id int,
 salary INT default 25000);
 
 insert into emp (id)
 values (101);
 select *from emp;
 
 
 CREATE TABLE city(
 id int primary key,
 city varchar(50),
 age int,
CONSTRAINT age_check CHECK (age >= 18 AND city = "Delhi"));
 
 select * from city;
  
 
 CREATE TABLE stud (
 rollno INT PRIMARY KEY,
 name  VARCHAR(50),
 mark int NOT NULL,
 grade VARCHAR (1),
 city VARCHAR(20));

 
 INSERT INTO stud(rollno,name,mark,grade,city)
 values(11,"sanjay",98,"A","Pune"),
 (12,"ranjeet",90,"A","Mumbai"),
 (13,"pawan",34,"C","nagpur"),
 (14,"ronit",76,"B","beed"),
 (15,"yash",99,"O","SambhajiNagar");
 
 select distinct  city from stud;
 DESC stud;
 
 select *from stud
 where mark >80 AND city = "Mumbai";
 
 select * from stud
 limit 3;
 
 select * from stud;
 
 
 
 
 
 
 
 
 
 CREATE DATABASE CompanyDB;
USE CompanyDB;

-- Department Table
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(50)
);

-- Employees Table
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100) NOT NULL,
    salary DECIMAL(10,2),
    dept_id INT,
    hire_date DATE,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);

-- Projects Table
CREATE TABLE Projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);
INSERT INTO Departments VALUES
(1, 'IT', 'Pune'),
(2, 'HR', 'Mumbai'),
(3, 'Finance', 'Delhi');

INSERT INTO Employees VALUES
(101, 'Amit', 60000, 1, '2022-01-15'),
(102, 'Sneha', 75000, 1, '2021-03-10'),
(103, 'Rahul', 50000, 2, '2023-06-20'),
(104, 'Priya', 90000, 3, '2020-09-12'),
(105, 'Vikram', 45000, 2, '2024-02-01');

INSERT INTO Projects VALUES
(1, 'AI System', 1),
(2, 'Recruitment Portal', 2),
(3, 'Budget Analysis', 3);

-- View all employees
SELECT * FROM Employees;

-- Select specific columns
SELECT emp_name, salary FROM Employees;

-- WHERE condition
SELECT * FROM Employees WHERE salary > 60000;

-- AND condition
SELECT * FROM Employees WHERE salary > 50000 AND dept_id = 1;

-- BETWEEN
SELECT * FROM Employees WHERE salary BETWEEN 50000 AND 80000;

-- LIKE
SELECT * FROM Employees WHERE emp_name LIKE 'A%';

-- ORDER BY
SELECT * FROM Employees ORDER BY salary DESC;

-- LIMIT (MySQL)
SELECT * FROM Employees LIMIT 3;


-- COUNT
SELECT COUNT(*) FROM Employees;

-- SUM
SELECT SUM(salary) FROM Employees;

-- AVG
SELECT AVG(salary) FROM Employees;

-- MAX
SELECT MAX(salary) FROM Employees;

-- MIN
SELECT MIN(salary) FROM Employees;


-- Total salary per department
SELECT dept_id, SUM(salary) AS total_salary
FROM Employees
GROUP BY dept_id;

-- Departments having more than 1 employee
SELECT dept_id, COUNT(emp_id) AS emp_count
FROM Employees
GROUP BY dept_id
HAVING COUNT(emp_id) > 1;

-- INNER JOIN
SELECT e.emp_name, e.salary, d.dept_name
FROM Employees e
INNER JOIN Departments d
ON e.dept_id = d.dept_id;

-- LEFT JOIN
SELECT e.emp_name, d.dept_name
FROM Employees e
LEFT JOIN Departments d
ON e.dept_id = d.dept_id;

-- RIGHT JOIN
SELECT e.emp_name, d.dept_name
FROM Employees e
RIGHT JOIN Departments d
ON e.dept_id = d.dept_id;

-- Employees with highest salary
SELECT * FROM Employees
WHERE salary = (SELECT MAX(salary) FROM Employees);

-- Employees earning above average salary
SELECT * FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);


-- Update salary
UPDATE Employees
SET salary = salary + 5000
WHERE emp_id = 101;

-- Delete employee
DELETE FROM Employees
WHERE emp_id = 105;

-- Add column
ALTER TABLE Employees
ADD email VARCHAR(100);

-- Drop column
ALTER TABLE Employees
DROP COLUMN email;

-- Drop table
-- DROP TABLE Projects;


CREATE VIEW HighSalaryEmployees AS
SELECT emp_name, salary
FROM Employees
WHERE salary > 70000;

-- Use View
SELECT * FROM HighSalaryEmployees;


CREATE INDEX idx_emp_name
ON Employees(emp_name);

START TRANSACTION;

UPDATE Employees
SET salary = salary + 2000
WHERE dept_id = 1;
