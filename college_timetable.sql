create database college_timetable;

use college_timetable;

CREATE TABLE Department (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100)
);

CREATE TABLE Instructor (
    InstructorID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);

CREATE TABLE Course (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    Credits INT,
    DepartmentID INT,
    InstructorID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID),
    FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
);

CREATE TABLE Classroom (
    ClassroomID INT PRIMARY KEY,
    RoomNumber VARCHAR(50),
    Capacity INT,
    Building VARCHAR(100)
);

CREATE TABLE Timetable (
    TimetableID INT PRIMARY KEY,
    CourseID INT,
    ClassroomID INT,
    DayOfWeek VARCHAR(10),
    StartTime TIME,
    EndTime TIME,
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
    FOREIGN KEY (ClassroomID) REFERENCES Classroom(ClassroomID)
);

INSERT INTO Department (DepartmentID, DepartmentName) 
VALUES 
(1, 'Computer Science'),
(2, 'Mathematics'),
(3, 'Physics'),
(4, 'Biology'),
(5, 'Chemistry');

INSERT INTO Instructor (InstructorID, FirstName, LastName, Email, DepartmentID)
VALUES 
(1, 'Amit', 'Roy', 'amit.roy@example.com', 1),
(2, 'Tushar', 'Singh', 'tusharsingh@example.com', 2),
(3, 'Rohit', 'Sharma', 'rohitsharma@example.com', 3),
(4, 'Mohit', 'Yadav', 'mohit.yadav@example.com', 4),
(5, 'Ishita', 'Roy', 'ishita.roy@example.com', 5);

INSERT INTO Course (CourseID, CourseName, Credits, DepartmentID, InstructorID)
VALUES 
(101, 'Database Systems', 4, 1, 1),
(102, 'Calculus I', 3, 2, 2),
(103, 'Quantum Physics', 5, 3, 3),
(104, 'Genetics', 4, 4, 4),
(105, 'Organic Chemistry', 3, 5, 5);

INSERT INTO Classroom (ClassroomID, RoomNumber, Capacity, Building)
VALUES 
(1, 'B101', 30, 'Science Building'),
(2, 'C202', 40, 'Mathematics Building'),
(3, 'D303', 50, 'Physics Building'),
(4, 'E404', 35, 'Biology Building'),
(5, 'F505', 45, 'Chemistry Building');

INSERT INTO Timetable (TimetableID, CourseID, ClassroomID, DayOfWeek, StartTime, EndTime)
VALUES 
(1, 101, 1, 'Monday', '09:00:00', '11:00:00'),
(2, 102, 2, 'Wednesday', '10:00:00', '12:00:00'),
(3, 103, 3, 'Friday', '13:00:00', '15:00:00'),
(4, 104, 4, 'Tuesday', '10:00:00', '12:00:00'),
(5, 105, 5, 'Thursday', '14:00:00', '16:00:00');


SELECT C.CourseName, I.FirstName, I.LastName
FROM Course C
JOIN Instructor I ON C.InstructorID = I.InstructorID;

SELECT C.CourseName
FROM Course C
JOIN Department D ON C.DepartmentID = D.DepartmentID
WHERE D.DepartmentName = 'Computer Science';

SELECT I.FirstName, I.LastName, COUNT(C.CourseID) AS CourseCount
FROM Instructor I
JOIN Course C ON I.InstructorID = C.InstructorID
GROUP BY I.InstructorID, I.FirstName, I.LastName
HAVING COUNT(C.CourseID) > 1;

SELECT C.CourseName, T.StartTime, T.EndTime, CR.RoomNumber
FROM Timetable T
JOIN Course C ON T.CourseID = C.CourseID
JOIN Classroom CR ON T.ClassroomID = CR.ClassroomID
WHERE T.DayOfWeek = 'Monday';

SELECT RoomNumber, Capacity, Building
FROM Classroom
WHERE Capacity > 40;

SELECT I.FirstName, I.LastName, I.Email, D.DepartmentName
FROM Instructor I
JOIN Department D ON I.DepartmentID = D.DepartmentID
ORDER BY D.DepartmentName;

SELECT C.CourseName, T.DayOfWeek, T.StartTime, T.EndTime
FROM Timetable T
JOIN Course C ON T.CourseID = C.CourseID
JOIN Classroom CR ON T.ClassroomID = CR.ClassroomID
WHERE CR.RoomNumber = 'B101';

SELECT D.DepartmentName, COUNT(C.CourseID) AS CourseCount
FROM Department D
JOIN Course C ON D.DepartmentID = C.DepartmentID
GROUP BY D.DepartmentName;

SELECT CourseName, Credits
FROM Course;

SELECT I.FirstName, I.LastName, C.CourseName, C.Credits
FROM Instructor I
JOIN Course C ON I.InstructorID = C.InstructorID
WHERE C.Credits > 3;
