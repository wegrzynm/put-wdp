//Zd.4
SELECT * FROM Products WHERE InStock = 1;

//Zd.5
SELECT ProductName, Price FROM Products WHERE Price > 100;

//Zd.6
SELECT Price FROM Products WHERE ProductName = 'Mouse';

//Zd.7
CREATE TABLE LoginAttempts (
    AttemptID int primary key,
    Username varchar(50),
    IPAddress varchar(15),
    Success tinyint, //bool
    Timestamp datetime //Timestamp
);

//Zd.8
INSERT INTO LoginAttempts(Username, IPAddress, Success, Timestamp)
VALUES (1,"admin","192.168.1.10",1,"	2025-01-12 10:00:00"), (2,"alice","192.168.1.20",1,"2025-01-12 10:05:00"), (3,"admin","203.0.113.5",0,"2025-01-12 10:10:00"),(4,"admin","203.0.113.5",0,"2025-01-12 10:12:00"),(5,"bob","192.168.1.30",1,"2025-01-12 10:15:00");
SELECT * FROM LoginAttempts;

