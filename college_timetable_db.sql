create database college_timetable;

use college_timetable;

CREATE TABLE Departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Instructors (
    instructor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

CREATE TABLE Classrooms (
    classroom_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(20) UNIQUE NOT NULL,
    capacity INT NOT NULL,
    building VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credits INT NOT NULL,
    department_id INT NOT NULL,
    instructor_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id),
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id)
);

CREATE TABLE Timetables (
    timetable_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    classroom_id INT NOT NULL,
    day_of_week VARCHAR(10) NOT NULL,
    start_time VARCHAR(8) NOT NULL,  -- Store as string in 'HH:MM:SS' format
    end_time VARCHAR(8) NOT NULL,    -- Store as string in 'HH:MM:SS' format
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    FOREIGN KEY (classroom_id) REFERENCES Classrooms(classroom_id)
);


INSERT INTO Departments (department_name) 
VALUES 
('Computer Science'),
('Mathematics'),
('Physics'),
('Biology'),
('Chemistry');

INSERT INTO Instructors (first_name, last_name, email, department_id)
VALUES 
('Amit', 'Roy', 'amit.roy@example.com', 1),
('Tushar', 'Singh', 'tusharsingh@example.com', 2),
('Rohit', 'Sharma', 'rohitsharma@example.com', 3),
('Mohit', 'Yadav', 'mohit.yadav@example.com', 4),
('Ishita', 'Roy', 'ishita.roy@example.com', 5);

INSERT INTO Courses (course_name, credits, department_id, instructor_id)
VALUES 
('Database Systems', 4, 1, 1),
('Calculus I', 3, 2, 2),
('Quantum Physics', 5, 3, 3),
('Genetics', 4, 4, 4),
('Organic Chemistry', 3, 5, 5);

INSERT INTO Classrooms (room_number, capacity, building)
VALUES 
('B101', 30, 'Science Building'),
('C202', 40, 'Mathematics Building'),
('D303', 50, 'Physics Building'),
('E404', 35, 'Biology Building'),
('F505', 45, 'Chemistry Building');

INSERT INTO Timetables (course_id, classroom_id, day_of_week, start_time, end_time)
VALUES 
(1, 1, 'Monday', '09:00:00', '11:00:00'),
(2, 2, 'Wednesday', '10:00:00', '12:00:00'),
(3, 3, 'Friday', '13:00:00', '15:00:00'),
(4, 4, 'Tuesday', '10:00:00', '12:00:00'),
(5, 5, 'Thursday', '14:00:00', '16:00:00');

SELECT C.course_name, I.first_name, I.last_name
FROM courses C
JOIN instructors I ON C.instructor_id = I.instructor_id;

SELECT C.course_name
FROM courses C
JOIN departments D ON C.department_id = D.department_id
WHERE D.department_name = 'Computer Science';

SELECT I.first_name, I.last_name, COUNT(C.course_id) AS course_count
FROM instructors I
JOIN courses C ON I.instructor_id = C.instructor_id
GROUP BY I.instructor_id, I.first_name, I.last_name
HAVING COUNT(C.course_id) > 1;

SELECT C.course_name, T.start_time, T.end_time, CR.room_number
FROM timetables T
JOIN courses C ON T.course_id = C.course_id
JOIN classrooms CR ON T.classroom_id = CR.classroom_id
WHERE T.day_of_week = 'Monday';

SELECT room_number, capacity, building
FROM classrooms
WHERE capacity > 40;

SELECT I.first_name, I.last_name, I.email, D.department_name
FROM instructors I
JOIN departments D ON I.department_id = D.department_id
ORDER BY D.department_name;

SELECT C.course_name, T.day_of_week, T.start_time, T.end_time
FROM timetables T
JOIN courses C ON T.course_id = C.course_id
JOIN classrooms CR ON T.classroom_id = CR.classroom_id
WHERE CR.room_number = 'B101';

SELECT D.department_name, COUNT(C.course_id) AS course_count
FROM departments D
JOIN courses C ON D.department_id = C.department_id
GROUP BY D.department_name;

SELECT course_name, credits
FROM courses;

SELECT I.first_name, I.last_name, C.course_name, C.credits
FROM instructors I
JOIN courses C ON I.instructor_id = C.instructor_id
WHERE C.credits > 3;

SELECT D.department_id, I.first_name, I.last_name, C.course_name, C.course_id
FROM departments AS D, instructors AS I, courses AS C
WHERE D.department_id = I.department_id 
  AND D.department_id = C.department_id 
  AND C.credits > 3;

SELECT D.department_id, I.first_name, I.last_name, C.course_name, C.course_id
FROM departments AS D
JOIN instructors AS I ON D.department_id = I.department_id
JOIN courses AS C ON I.instructor_id = C.instructor_id;

