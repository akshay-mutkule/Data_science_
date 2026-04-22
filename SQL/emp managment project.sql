use employees;

select * from jobdepartment;
select* from leaves;
select* from payroll;
select * from salary_bonus;
select * from employee;
select * from qualification;

ALTER TABLE Jobdepartment
ADD PRIMARY KEY (JobID);

alter table employee
ADD  CONSTRAINT job_dept
FOREIGN KEY (JobID) REFERENCES Jobdepartment(JobID);

select *from jobdepartment;

ALTER TABLE salary_bonus
ADD salary_ID INT;

ALTER TABLE salary_bonus
ADD PRIMARY KEY (SalaryID);

ALTER TABLE salary_bonus
ADD CONSTRAINT fk_salary_job
FOREIGN KEY (JobID)
REFERENCES jobdepartment(JobID)
ON DELETE CASCADE
ON UPDATE CASCADE;

alter table employee
add primary key (EmpId);

alter table qualification
add primary key (QualID);

alter table leaves
add primary key (LeaveID);

alter table payroll 
add primary key (PayrollID);

alter table leaves
add constraint fk_for_empid foreign key(EmpID) references employee(EmpID);

alter table qualification
add constraint fk_emp_qual foreign key (EmpID) references employee(EmpID);

alter table payroll 
add constraint foreign key (EmpID)
references employee (EmpID);

alter table payroll 
add constraint foreign key (LeaveID)
references leaves (LeaveID);

alter table payroll 
add constraint foreign key (SalaryID)
references salary_bonus (SalaryID);

alter table payroll
add constraint foreign key (JobID)
references jobdepartment (JobID);

DESCRIBE payroll;
DESCRIBE jobdepartment;

alter table payroll
change JobID JobID int;

-- INSIGHTS

-- EMPLOYEE INSIGHTS

-- How many unique employees are currently in the system?
select count(EmpID) from employee;

-- Which departments have the highest number of employees?
select JobDept ,count(EmpID)from jobdepartment
join employee on employee.JobID = jobdepartment.JobID
group by JobDept
order by count(EmpID) desc
limit 1;

-- What is the average salary per department?
select JobDept , avg(Annual) from jobdepartment
join salary_bonus on jobdepartment.JobID = salary_bonus.JobID
group by JobDept;

-- Who are the top 5 highest-paid employees?
select FirstName,LastName, Annual from employee
join salary_bonus on salary_bonus.JobID = employee.JobID
order by Annual DESC
limit 5;

-- What is the total salary expenditure across the company?
select sum(Annual)from salary_bonus;

-- JOB ROLE AND DEPARTMENT ANALYSIS

-- How many different job roles exist in each department?
select jobDept, count(distinct Name) from jobdepartment
group by JobDept;

-- What is the average salary range per department?
select JobDept ,avg(Amount) as Average_monthly_salary from jobdepartment
join salary_bonus on salary_bonus.JobID = jobdepartment.JobID
group by JobDept;

-- Which job roles offer the highest salary?
select Name ,max(Amount) as high_salary from jobdepartment
join salary_bonus on  salary_bonus.JobID=jobdepartment.JobId
group by Name
order by high_salary DESC
limit 1;

-- Which departments have the highest total salary allocation?
select JobDept ,sum(Amount) AS total_salary from jobdepartment
join salary_bonus on salary_bonus.JobID = jobdepartment.JobID
group by JobDept
order by total_salary desc
limit 1;

-- QUALIFICATION AND SKILLS ANALYSIS

-- How many employees have at least one qualification listed?
SELECT COUNT(DISTINCT EmpID) AS EmployeesWithQualification
FROM qualification;

-- Which positions require the most qualifications?
SELECT j.JobDept, COUNT(q.QualID) AS QualificationCount
FROM JobDepartment j
JOIN Employee e 
    ON j.JobID = e.JobID
JOIN Qualification q 
    ON e.EmpID = q.EmpID
GROUP BY j.JobDept
ORDER BY QualificationCount DESC;

-- Which employees have the highest number of qualifications?
SELECT e.EmpID, e.FirstName, e.LastName,
       COUNT(q.QualID) AS QualificationCount
FROM Employee e
JOIN Qualification q 
    ON e.EmpID = q.EmpID
GROUP BY e.EmpID, e.FirstName, e.LastName
ORDER BY QualificationCount DESC;

--  LEAVE AND ABSENCE PATTERNS

-- ●Which year had the most employees taking leaves?
SELECT YEAR(Date) AS LeaveYear,
       COUNT(DISTINCT EmpID) AS EmployeesOnLeave
FROM Leaves
GROUP BY LeaveYear
ORDER BY EmployeesOnLeave DESC;

-- What is the average number of leave days taken by its employees per department?
SELECT j.JobDept,
       COUNT(l.LeaveID) / COUNT(DISTINCT e.EmpID) AS AvgLeavePerEmployee
FROM Employee e
JOIN JobDepartment j 
    ON e.JobID = j.JobID
LEFT JOIN Leaves l 
    ON e.EmpID = l.EmpID
GROUP BY j.JobDept;

-- Which employees have taken the most leaves?
SELECT e.EmpID,
       COUNT(l.LeaveID) AS TotalLeaves
FROM Employee e
JOIN Leaves l 
    ON e.EmpID = l.EmpID
GROUP BY e.EmpID
ORDER BY TotalLeaves DESC;

-- What is the total number of leave days taken company-wide?
SELECT COUNT(*) AS TotalLeaveDays
FROM Leaves;







