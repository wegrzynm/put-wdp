
Lab11 exercises students
🎯 LABORATORIUM 11: DATABASES & SQL
Ćwiczenia dla Studentów
Imię i Nazwisko: ____
Numer Indeksu: ____
Grupa: ____
Data: ____

📋 INFORMACJE OGÓLNE
Czas na wykonanie: 90 minut (z czego ~60 minut na ćwiczenia)
Narzędzie: SQLite Online Compiler - https://www.programiz.com/sql/online-compiler/
Cel: Nauka podstaw SQL i ich zastosowania w kontekście cyberbezpieczeństwa

🎓 SYSTEM OCENIANIA
MINIMUM (ocena 3.0): Zadania 1-8 (zadania podstawowe)
OCENA WYŻSZA: Im więcej zadań rozszerzonych, tym lepiej

Punkty	Ocena
8-9	3.0
10-11	3.5
12-13	4.0
14	4.5
15	5.0
UWAGA: Pokazuj rozwiązania prowadzącemu na bieżąco, nie czekaj do końca!

🔧 PRZYGOTOWANIE
Krok 1: Otwórz narzędzie
Wejdź na: https://www.programiz.com/sql/online-compiler/
Zobaczysz editor SQL po lewej stronie
Wyniki będą po prawej stronie
Przycisk "Run SQL" u góry
Krok 2: Wyczyść domyślny kod
Usuń wszystko co jest w edytorze
Zaczynamy od zera!
Krok 3: Gotowy do pracy!
Możesz pisać wiele komend naraz (oddzielone średnikami)
Możesz kopiować-wklejać kod
Możesz testować i eksperymentować
🌡️ CZĘŚĆ 1: ROZGRZEWKA (Zadania 1-3)
Cel: Oswojenie się z SQL i narzędziem

✅ ZADANIE 1: Pierwsza tabela (1 pkt)
Zadanie: Stwórz tabelę Products z następującymi kolumnami:

ProductID (INT, PRIMARY KEY)
ProductName (VARCHAR 100 znaków)
Price (INT)
InStock (INT) - 1 = dostępny, 0 = niedostępny
Kod do napisania:

-- Twój kod tutaj:
CREATE TABLE ...
Sprawdzenie: Wykonaj: SELECT * FROM Products;
Powinno pokazać pustą tabelę z 4 kolumnami.

✍️ Miejsce na kod:

☑️ Status: [ ] Zrobione [ ] Sprawdzone przez prowadzącego

✅ ZADANIE 2: Dodaj produkty (1 pkt)
Zadanie: Dodaj 3 produkty do tabeli Products:

ID=1, Nazwa="Laptop", Cena=3000, InStock=1
ID=2, Nazwa="Mouse", Cena=50, InStock=1
ID=3, Nazwa="Monitor", Cena=800, InStock=0
Wskazówka:

INSERT INTO Products (ProductID, ProductName, Price, InStock)
VALUES (..., ..., ..., ...);
✍️ Miejsce na kod:

Sprawdzenie: Wykonaj: SELECT * FROM Products;
Powinno pokazać 3 wiersze z produktami.

☑️ Status: [ ] Zrobione [ ] Sprawdzone przez prowadzącego

✅ ZADANIE 3: Podstawowe zapytanie (1 pkt)
Zadanie: Napisz zapytanie które zwróci tylko nazwy produktów (kolumna ProductName).

Oczekiwany wynik:

ProductName
-----------
Laptop
Mouse
Monitor
✍️ Miejsce na kod:

SELECT ...




☑️ Status: [ ] Zrobione [ ] Sprawdzone przez prowadzącego

📚 CZĘŚĆ 2: PODSTAWOWE OPERACJE (Zadania 4-8)
Cel: Opanowanie SELECT z warunkami WHERE

✅ ZADANIE 4: Filtrowanie - produkty dostępne (1 pkt)
Zadanie: Napisz zapytanie które zwróci wszystkie kolumny tylko dla produktów dostępnych (InStock = 1).

Oczekiwany wynik:

ProductID | ProductName | Price | InStock
1         | Laptop      | 3000  | 1
2         | Mouse       | 50    | 1
Wskazówka: Użyj WHERE

✍️ Miejsce na kod:

SELECT ...




☑️ Status: [ ] Zrobione [ ] Sprawdzone przez prowadzącego

✅ ZADANIE 5: Filtrowanie - drogie produkty (1 pkt)
Zadanie: Zwróć nazwy i ceny produktów które kosztują więcej niż 100 PLN.

Oczekiwany wynik:

ProductName | Price
Laptop      | 3000
Monitor     | 800
Wskazówka: Operator > (większe niż)

✍️ Miejsce na kod:

SELECT ...




☑️ Status: [ ] Zrobione [ ] Sprawdzone przez prowadzącego

✅ ZADANIE 6: Konkretny produkt (1 pkt)
Zadanie: Znajdź cenę produktu o nazwie "Mouse".

Oczekiwany wynik:

Price
50
Wskazówka: WHERE ProductName = '...' (tekst w apostrofach!)

✍️ Miejsce na kod:

SELECT ...




☑️ Status: [ ] Zrobione [ ] Sprawdzone przez prowadzącego

✅ ZADANIE 7: Nowa tabela - Cybersecurity scenario (1 pkt)
Zadanie: Stwórz tabelę LoginAttempts (próby logowania) z kolumnami:

AttemptID (INT, PRIMARY KEY)
Username (VARCHAR 50)
IPAddress (VARCHAR 15)
Success (INT) - 1 = sukces, 0 = porażka
Timestamp (VARCHAR 20)
Kontext: Monitoring prób logowania to typowe zadanie w cybersecurity!

✍️ Miejsce na kod:

CREATE TABLE ...









☑️ Status: [ ] Zrobione [ ] Sprawdzone przez prowadzącego

✅ ZADANIE 8: Dodaj logi logowania (1 pkt)
Zadanie: Dodaj 5 prób logowania do tabeli LoginAttempts:

ID	Username	IPAddress	Success	Timestamp
1	admin	192.168.1.10	1	2025-01-12 10:00:00
2	alice	192.168.1.20	1	2025-01-12 10:05:00
3	admin	203.0.113.5	0	2025-01-12 10:10:00
4	admin	203.0.113.5	0	2025-01-12 10:12:00
5	bob	192.168.1.30	1	2025-01-12 10:15:00
✍️ Miejsce na kod:

INSERT INTO ...













Sprawdzenie: SELECT * FROM LoginAttempts; - powinno być 5 wierszy.

☑️ Status: [ ] Zrobione [ ] Sprawdzone przez prowadzącego

🔥 CZĘŚĆ 3: ZADANIA ROZSZERZONE (Zadania 9-15)
Cel: Bardziej zaawansowane zapytania i security thinking

✅ ZADANIE 9: Wykryj nieudane logowania (1 pkt)
Zadanie: Zwróć wszystkie nieudane próby logowania (Success = 0). Pokaż: Username, IPAddress, Timestamp.

Kontekst security: To pierwszy krok w wykrywaniu ataków brute-force!

Oczekiwany wynik:

Username | IPAddress   | Timestamp
admin    | 203.0.113.5 | 2025-01-12 10:10:00
admin    | 203.0.113.5 | 2025-01-12 10:12:00
✍️ Miejsce na kod:

SELECT ...




☑️ Status: [ ] Zrobione [ ] Sprawdzone przez prowadzącego

✅ ZADANIE 10: Podejrzany IP (1 pkt)
Zadanie: Znajdź wszystkie próby logowania z adresu IP: 203.0.113.5

Kontekst security: Analizowanie aktywności z konkretnego IP to podstawa threat hunting!

Oczekiwany wynik:

AttemptID | Username | Success | Timestamp
3         | admin    | 0       | 2025-01-12 10:10:00
4         | admin    | 0       | 2025-01-12 10:12:00
✍️ Miejsce na kod:

SELECT ...




☑️ Status: [ ] Zrobione [ ] Sprawdzone przez prowadzącego

✅ ZADANIE 11: Kombinacja warunków - AND (1 pkt)
Zadanie: Znajdź nieudane logowania (Success = 0) na konto 'admin'.

Wskazówka: Użyj WHERE ... AND ...

Oczekiwany wynik:

AttemptID | Username | IPAddress   | Success | Timestamp
3         | admin    | 203.0.113.5 | 0       | 2025-01-12 10:10:00
4         | admin    | 203.0.113.5 | 0       | 2025-01-12 10:12:00
✍️ Miejsce na kod:

SELECT ...




☑️ Status: [ ] Zrobione [ ] Sprawdzone przez prowadzącego

✅ ZADANIE 12: Funkcje agregujące - COUNT (1 pkt)
Zadanie: Policz ile było łącznie prób logowania w systemie.

Wskazówka: SELECT COUNT(*) FROM ...

Oczekiwany wynik:

5
✍️ Miejsce na kod:

SELECT ...




Dodatkowe pytanie: Ile było nieudanych prób? (dodaj WHERE)

✍️ Miejsce na kod:

SELECT ...




☑️ Status: [ ] Zrobione [ ] Sprawdzone przez prowadzącego

✅ ZADANIE 13: DISTINCT - unikalne wartości (1 pkt)
Zadanie: Zwróć listę unikalnych usernames którzy próbowali się zalogować.

Wskazówka: SELECT DISTINCT ...

Oczekiwany wynik:

Username
admin
alice
bob
Kontekst: Szybkie zobaczenie kto próbował uzyskać dostęp.

✍️ Miejsce na kod:

SELECT ...




☑️ Status: [ ] Zrobione [ ] Sprawdzone przez prowadzącego

✅ ZADANIE 14: LIKE - pattern matching (1 pkt)
Zadanie: Znajdź wszystkie próby logowania z IP zaczynającego się od 192.168. (to są lokalne IP - internal network).

Wskazówka: WHERE IPAddress LIKE '192.168.%'
(% = wildcard, dopasowuje cokolwiek)

Oczekiwany wynik:

Username | IPAddress    | Success
admin    | 192.168.1.10 | 1
alice    | 192.168.1.20 | 1
bob      | 192.168.1.30 | 1
Kontekst security: Rozróżnianie internal vs external traffic!

✍️ Miejsce na kod:

SELECT ...




☑️ Status: [ ] Zrobione [ ] Sprawdzone przez prowadzącego

✅ ZADANIE 15: CHALLENGE - Security Alert! (1 pkt)
Zadanie: Napisz zapytanie które znajdzie podejrzaną aktywność:

Nieudane logowania (Success = 0)
NA konto 'admin'
Z zewnętrznego IP (NIE zaczyna się od '192.168.')
Wskazówka:

WHERE Success = 0 
  AND Username = '...' 
  AND IPAddress NOT LIKE '192.168.%'
Oczekiwany wynik:

AttemptID | Username | IPAddress   | Timestamp
3         | admin    | 203.0.113.5 | 2025-01-12 10:10:00
4         | admin    | 203.0.113.5 | 2025-01-12 10:12:00
Kontekst security: To jest realny security use case!
Brute-force attack na admin z external IP = RED FLAG 🚨

✍️ Miejsce na kod:

SELECT ...






Gratulacje! To jest security monitoring w akcji! 🎉

☑️ Status: [ ] Zrobione [ ] Sprawdzone przez prowadzącego

🚀 BONUS: FOREIGN KEYS & RELATIONSHIPS (Opcjonalne, bez punktów)
UWAGA: To jest advanced! Ale jeśli zrobiłeś/aś wszystkie zadania 1-15 - spróbuj!

📊 BONUS 1: Zrozumienie Foreign Keys
Teoria: FOREIGN KEY (klucz obcy) łączy dwie tabele.

Przykład:

Tabela Users (UserID = PRIMARY KEY)
Tabela Posts (AuthorID = FOREIGN KEY → Users.UserID)
To tworzy relationship: Users ←→ Posts

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

_________________________________
_________________________________
📊 BONUS 2: JOIN - Łączenie tabel
Zadanie: Napisz query które pokaże:

Nazwę kursu
Nazwisko instruktora (z tabeli Users!)
Hint: Użyj JOIN

SELECT Courses.CourseName, Users.Username
FROM Courses
JOIN Users ON Courses.InstructorID = Users.UserID;
Oczekiwany wynik:

CourseName                     | Username
Introduction to Programming    | admin
Databases & SQL                | admin
Cybersecurity Basics           | alice
✍️ Miejsce na kod:

📊 BONUS 3: Ile kursów prowadzi każdy instructor?
Zadanie: Policz ile kursów ma każdy instruktor.

Hint: GROUP BY + COUNT + JOIN

✍️ Miejsce na kod:

SELECT ...













Oczekiwany wynik:

Username | CourseCount
admin    | 2
alice    | 1
📊 BONUS 4: Własny przykład relationships!
Zadanie: Wymyśl własny przykład z foreign key!

Pomysły:

Students ←→ Enrollments ←→ Courses
Products ←→ Orders
Authors ←→ Books
Stwórz 2 tabele z foreign key:

✍️ Miejsce na kod:

-- Twoja pierwsza tabela:





-- Twoja druga tabela (z FOREIGN KEY):





-- INSERT przykładowe dane:





-- Query z JOIN:





Opisz co stworzyłeś/aś:

_________________________________
_________________________________
_________________________________
🎓 GRATULACJE!
UWAGA: To jest educacyjny experiment. NIE rób tego na produkcyjnych systemach!

Eksperyment: Vulnerable Login
Scenariusz: Wyobraź sobie że backend robi takie zapytanie:

SELECT * FROM LoginAttempts 
WHERE Username = '[USER_INPUT]' AND Success = 1;
Użytkownik wpisuje w pole login: admin Query staje się:

SELECT * FROM LoginAttempts 
WHERE Username = 'admin' AND Success = 1;
Pytanie: Co się stanie jeśli user wpisze: admin' OR '1'='1?

Query staje się:

SELECT * FROM LoginAttempts 
WHERE Username = 'admin' OR '1'='1' AND Success = 1;
'1'='1' jest zawsze TRUE!

Spróbuj:
-- Normalne query (tylko sukces dla admin):
SELECT * FROM LoginAttempts 
WHERE Username = 'admin' AND Success = 1;

-- SQL Injection (pomija warunek Success):
SELECT * FROM LoginAttempts 
WHERE Username = 'admin' OR '1'='1';
Co widzisz? SQL Injection zwraca WSZYSTKIE rekordy!

Obrona: Prepared statements (nie konkatenacja stringów).

✍️ Twoje obserwacje:

Normalne query zwróciło: _____ wierszy
Injection zwrócił: _____ wierszy

Dlaczego to jest niebezpieczne:
_________________________________
_________________________________
📊 PODSUMOWANIE
✅ CHECKLIST
Zadania podstawowe (minimum):

Zadanie 1: Pierwsza tabela
Zadanie 2: Dodaj produkty
Zadanie 3: Podstawowe zapytanie
Zadanie 4: Filtrowanie - dostępne produkty
Zadanie 5: Filtrowanie - drogie produkty
Zadanie 6: Konkretny produkt
Zadanie 7: Tabela LoginAttempts
Zadanie 8: Dodaj logi
Zadania rozszerzone (wyższa ocena):

Zadanie 9: Wykryj nieudane logowania
Zadanie 10: Podejrzany IP
Zadanie 11: Kombinacja AND
Zadanie 12: COUNT
Zadanie 13: DISTINCT
Zadanie 14: LIKE pattern
Zadanie 15: Security Alert (CHALLENGE)
Bonus:

SQL Injection experiment
📝 TWOJE PUNKTY
Policzone przez prowadzącego:

Zadania podstawowe (1-8): _ / 8
Zadania rozszerzone (9-15): _ / 7
RAZEM: _ / 15

OCENA: _

🎓 CO NAUCZYŁEŚ/NAUCZYŁAŚ SIĘ DZISIAJ?
Umiejętności techniczne:

✓ CREATE TABLE - tworzenie struktury bazy danych
✓ INSERT - dodawanie rekordów
✓ SELECT - podstawowe zapytania
✓ WHERE - filtrowanie danych
✓ COUNT, DISTINCT, LIKE - zaawansowane operacje
Kontekst cybersecurity:

✓ Monitoring logowania (LoginAttempts table)
✓ Wykrywanie brute-force attacks
✓ Analiza IP addresses (internal vs external)
✓ Security alerts (kombinacja warunków)
✓ SQL Injection threat awareness
📚 DALSZE KROKI
Jeśli chcesz pogłębić wiedzę:

1. Praktyka
Spędź 1h na: https://www.programiz.com/sql/online-compiler/
Eksperymentuj z własnymi tabelami
Spróbuj stworzyć bazę danych dla mini-projektu
2. Kolejne tematy SQL
JOIN - łączenie tabel
UPDATE - modyfikacja danych
DELETE - usuwanie rekordów
GROUP BY - grupowanie i agregacje
Subqueries - zapytania w zapytaniach
3. Security deep dive
OWASP SQL Injection: https://owasp.org/www-community/attacks/SQL_Injection
PortSwigger Academy: https://portswigger.net/web-security/sql-injection
HackTheBox / TryHackMe: legal hacking practice
4. Real databases
PostgreSQL - najpopularniejszy open-source
MySQL - używany przez WordPress, Drupal
MongoDB - NoSQL alternative
💬 FEEDBACK
Co było najtrudniejsze?

_________________________________
_________________________________
Co było najciekawsze?

_________________________________
_________________________________
Pytania/uwagi?

_________________________________
_________________________________
🎉 GRATULACJE!
Ukończyłeś/aś Lab 11 - Databases & SQL!

SQL to skill który będziesz używać przez całą karierę w IT/cybersecurity. Dzisiaj położyłeś/aś fundamenty. Keep learning! 🚀

Podpis prowadzącego: ____
Data sprawdzenia: ____