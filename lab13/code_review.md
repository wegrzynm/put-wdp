# Code Review Report - vulnerable_app.py

## Błąd 1: SQL Injection w funkcji login()
- **Linia:** 12
- **Problem:** Zapytanie SQL budowane przez konkatenację stringów z danymi użytkownika
- **Ryzyko:** KRYTYCZNE
- **Naprawa:** Użyć parametryzowanych zapytań: `cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))`

## Błąd 2: SQL Injection w funkcji register()
- **Linia:** 26
- **Problem:** Zapytanie INSERT budowane przez f-string z danymi użytkownika
- **Ryzyko:** KRYTYCZNE
- **Naprawa:** Użyć parametryzowanych zapytań: `cursor.execute("INSERT INTO users VALUES (?, ?)", (username, hashed))`

## Błąd 3: SQL Injection w funkcji change_password()
- **Linia:** 40
- **Problem:** Zapytanie UPDATE budowane przez f-string
- **Ryzyko:** KRYTYCZNE
- **Naprawa:** Użyć parametryzowanych zapytań: `cursor.execute("UPDATE users SET password=? WHERE username=?", (hashed, username))`

## Błąd 4: SQL Injection w funkcji get_user_data()
- **Linia:** 51
- **Problem:** Zapytanie SELECT budowane przez f-string z user_id
- **Ryzyko:** KRYTYCZNE
- **Naprawa:** Użyć parametryzowanych zapytań: `cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))`

## Błąd 5: Słabe hashowanie MD5
- **Linia:** 25, 39
- **Problem:** Użycie MD5 do hashowania haseł - algorytm uznany za niebezpieczny
- **Ryzyko:** WYSOKIE
- **Naprawa:** Użyć bcrypt lub argon2: `import bcrypt; hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())`

## Błąd 6: Brak saltingu haseł
- **Linia:** 25, 39
- **Problem:** Hasła hashowane bez soli, co umożliwia ataki rainbow table
- **Ryzyko:** WYSOKIE
- **Naprawa:** Użyć bcrypt lub dodać unikalny salt dla każdego hasła

## Błąd 7: Wyciek informacji w konsoli
- **Linia:** 29
- **Problem:** Wypisywanie hashu hasła do konsoli - może być zapisane w logach
- **Ryzyko:** ŚREDNIE
- **Naprawa:** Usunąć lub zamienić na logging.info bez wrażliwych danych

## Błąd 8: Przechowywanie haseł w plain text
- **Linia:** 12
- **Problem:** Funkcja login() porównuje hasło z bazą bez hashowania - hasła przechowywane w plain text
- **Ryzyko:** KRYTYCZNE
- **Naprawa:** Hashować hasło przed porównaniem i porównać hashe

## Błąd 9: Niezamknięte połączenia z bazą danych
- **Linia:** 8, 21, 36, 48 (wszystkie funkcje)
- **Problem:** Połączenia z bazą nie są zamykane (brak conn.close())
- **Ryzyko:** ŚREDNIE
- **Naprawa:** Użyć context managera: `with sqlite3.connect('users.db') as conn:`

## Błąd 10: Zbyt słabe wymagania hasła
- **Linia:** 55-58
- **Problem:** Minimalna długość 4 znaki, brak wymagań specjalnych znaków i wielkich liter
- **Ryzyko:** WYSOKIE
- **Naprawa:** Zwiększyć min_length do 12, wymagać wielkich liter, cyfr i znaków specjalnych

## Błąd 11: Brak walidacji długości hasła
- **Linia:** 62-66
- **Problem:** Funkcja validate_new_password() sprawdza tylko długość, nie wykorzystuje pozostałych parametrów
- **Ryzyko:** ŚREDNIE
- **Naprawa:** Dodać sprawdzanie require_special i require_uppercase z PASSWORD_REQUIREMENTS

## Błąd 12: Brak ochrony przed brute-force
- **Linia:** Cały kod
- **Problem:** Brak limitowania prób logowania
- **Ryzyko:** WYSOKIE
- **Naprawa:** Dodać rate limiting i blokadę konta po N nieudanych próbach

## Analiza pylint

### password_utils.py
- Wynik: 7.83/10
- Główne uwagi: 'Trailing whitespace', 'Unnecessary "elif" after "return", remove the leading "el" from "elif"'

### test_passwords.py próba 1   
- Wynik: 4.11/10
- Główne uwagi: 'Line too long (104/100)', 'Missing function or method docstring', 'Comparison 'is_common_password('123456') == True' should be 'is_common_password('123456') is True' if checking for the singleton value True, or 'is_common_password('123456')' if testing for falsiness (singleton-comparison)', 'Comparison 'result['is_common'] == False' should be 'result['is_common'] is False' if checking for the singleton value False, or 'not result['is_common']' if testing for truthiness (singleton-comparison)', 'Comparison 'result['valid'] == True' should be 'result['valid'] is True' if checking for the singleton value True, or 'result['valid']' if testing for truthiness (singleton-comparison)', 'Redefining name 'sample_passwords' from outer scope (line 96) (redefined-outer-name)'

### test_passwords.py (po poprawkach)
- Wynik: 10.00/10 ✅
- Co poprawiłem po zobaczeniu uwag pylint:
  - Dodano docstringi do wszystkich funkcji testowych
  - Zmieniono porównania `== True/False` na bardziej pythoniczne `assert value` / `assert not value`
  - Poprawiono długość linii importu (podzielono na 2 linie)
  - Usunięto konflikt nazw w fixtures (dodano parametr `name=`)
  - Zmieniono porównanie z pustą listą `== []` na `assert not list`

