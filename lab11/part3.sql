-- Zd.9
SELECT * FROM LoginAttempts WHERE Success = 0;

-- Zd.10
SELECT * FROM LoginAttempts WHERE IPAddress = '203.0.113.5';

-- Zd.11
SELECT * FROM LoginAttempts WHERE Username = 'admin' AND Success = 0;

-- Zd.12
SELECT COUNT(1) FROM LoginAttempts;

SELECT COUNT(1) FROM LoginAttempts WHERE Success = 0;

-- Zd.13
SELECT DISTINCT Username FROM LoginAttempts; 
-- Lub
SELECT Username FROM LoginAttempts
GROUP BY Username;
-- Zd.14
SELECT * FROM LoginAttempts WHERE IPAddress LIKE '192.168.%';

-- Zd.15
SELECT * FROM LoginAttempts
WHERE (Success = 0 AND Username = 'admin') AND IPAddress NOT LIKE '192.168.%'; 