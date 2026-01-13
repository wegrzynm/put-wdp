Zadanie: Stwórz tabelę Courses z kursami:

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    InstructorID INT,
    FOREIGN KEY (InstructorID) REFERENCES Users(UserID)
);
Dodaj 3 kursy:

INSERT INTO Courses VALUES
(101, 'Introduction to Programming', 1),
(102, 'Databases & SQL', 1),
(103, 'Cybersecurity Basics', 2);
InstructorID wskazuje na Users!

Kursy 101 i 102: prowadzi admin (UserID=1)
Kurs 103: prowadzi alice (UserID=2)
Pytanie: Co się stanie jak spróbujesz dodać kurs z InstructorID = 999?

✍️ Miejsce na odpowiedź:
FOREIGN KEY ERROR, InstructorID not found

-- B2
SELECT Courses.CourseName, Users.Username
FROM Courses
JOIN Users ON Courses.InstructorID = Users.UserID;

-- B3
SELECT COUNT(*), Users.Username
FROM Courses
JOIN Users ON Courses.InstructorID = Users.UserID
GROUP BY Courses.CourseID

-- B4
CREATE TABLE Lecturers (
    LecturerId int primary key,
    Name varchar(25),
    Lastname varchar(25),
    Title varchar(50)
);

CREATE TABLE Courses (
    CourseID int primary key,
    CourseName varchar(50),
    LecturerId int,
    FOREIGN KEY (LecturerId) REFERENCES Lecturers(LecturerId)
);

CREATE TABLE Students (
    StudentID int primary key,
    Name varchar(25),
    Lastname varchar(25)
);

CREATE TABLE Enrollments (
    CourseID int,
    StudentID int,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

INSERT INTO Lecturers(LecturerId, Name, Lastname, Title)
VALUES (1,'Jerzy', 'Nawrocki', 'Professor'), (2,'Bartosz', 'Lewandowski', 'PhD');

INSERT INTO Students(StudentID, Name, Lastname) 
VALUES (1, 'Mateusz', 'Weg'), (2,'Jan','Adamski');

INSERT INTO Courses(CourseID, CourseName, LecturerId) 
VALUES (1, 'Introduction to programming', 1), (2, 'Introduction to Python', 2), (3, 'Example', 1);

INSERT INTO Enrollments(CourseID, StudentID)
VALUES (1,1), (1,2), (2,2), (3,1);

SELECT Students.Name, Students.Lastname
FROM Courses
JOIN Enrollments ON Enrollments.CourseID = Courses.CourseID
JOIN Students ON Enrollments.StudentID = Students.StudentID
WHERE Courses.CourseID = 1;