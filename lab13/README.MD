
Lab13 exercises self study
🧪 Laboratorium 13: Software Quality Assessment
Kurs: Introduction to Programming
Kierunek: Cybersecurity, rok 1
Forma: Praca samodzielna (do wykonania w domu)
Termin oddania: Przed egzaminem (luty)
Forma oddania: Kod źródłowy wysłany mailem do prowadzącego

📋 Informacje organizacyjne
Co musisz oddać?
Jeden plik ZIP zawierający:

test_passwords.py - testy jednostkowe (zadania Z1-Z5)
test_security.py - testy bezpieczeństwa (zadania Z6-Z7)
code_review.md - raport z code review (zadanie Z8)
screenshots/ - folder ze zrzutami ekranu z pylint (zadanie Z9)
System oceniania
Zakres	Punkty	Ocena
Z1-Z5 (podstawy pytest)	10 pkt	3.0 (minimum)
Z6-Z7 (testy security)	+4 pkt	4.0
Z8-Z9 (code review + pylint)	+4 pkt	4.5
Z10-Z12 (zadania rozszerzone)	+6 pkt	5.0
Minimum do zaliczenia: 10 punktów (zadania Z1-Z5)

🎯 Cele laboratorium
Po wykonaniu tych zadań będziesz potrafić:

Napisać i uruchomić testy jednostkowe w pytest
Testować wyjątki i przypadki brzegowe
Używać parametryzacji testów
Przeprowadzić code review pod kątem bezpieczeństwa
Używać narzędzi do analizy statycznej (pylint)
📚 Niezbędna teoria
Testing vs Debugging
Testing = szukanie błędów (czy coś jest źle?)
Debugging = naprawianie błędów (dlaczego jest źle?)
Łańcuch przyczynowy błędów
Mistake (błąd programisty) 
    → Defect (błąd w kodzie) 
        → Failure (widoczne nieprawidłowe działanie)
Ważne: Nie każdy defect prowadzi do failure! Błąd może "spać" w kodzie latami.

7 zasad testowania (ISTQB)
Testing shows presence of defects - testy pokazują OBECNOŚĆ błędów, nie ich BRAK
Exhaustive testing is impossible - nie da się przetestować wszystkiego
Early testing - im wcześniej testujesz, tym taniej naprawiasz
Defect clustering - 80% błędów jest w 20% kodu
Pesticide paradox - te same testy przestają znajdować nowe błędy
Testing is context-dependent - inne testy dla banku, inne dla gry
Absence-of-errors fallacy - brak błędów ≠ dobry produkt
Static vs Dynamic Testing
Typ	Opis	Przykłady
Static	Analiza BEZ uruchamiania kodu	Code review, pylint, linters
Dynamic	Analiza Z uruchamianiem kodu	Unit testy, testy integracyjne
🔧 Przygotowanie środowiska
Krok 1: Zainstaluj pytest
pip install pytest
Krok 2: Sprawdź instalację
pytest --version
⚠️ Problem na Windows?
Jeśli komenda pytest nie działa (np. "command not found"), użyj:

python -m pytest --version
Od teraz wszędzie gdzie widzisz pytest, możesz użyć python -m pytest

Przykład:

Zamiast: pytest test_passwords.py -v
Użyj: python -m pytest test_passwords.py -v
Krok 3: Zainstaluj pylint (do zadań rozszerzonych)
pip install pylint
Struktura projektu
Utwórz folder lab13/ z taką strukturą:

lab13/
├── password_utils.py      # kod do testowania (skopiuj poniżej)
├── test_passwords.py      # twoje testy (zadania Z1-Z5)
├── test_security.py       # testy security (zadania Z6-Z7)
├── vulnerable_app.py      # kod z lukami (do code review)
├── code_review.md         # twój raport
└── screenshots/           # zrzuty z pylint
📄 Kod do testowania
Skopiuj ten plik jako password_utils.py:

"""
Password utilities module for security applications.
This module contains functions for password validation and hashing.
"""
import hashlib
import re


def check_password_strength(password: str) -> str:
    """
    Check password strength and return category.
    
    Args:
        password: The password to check
        
    Returns:
        'Weak', 'Medium', or 'Strong'
        
    Raises:
        ValueError: If password is empty or None
    """
    if not password:
        raise ValueError("Password cannot be empty")
    
    score = 0
    
    # Length check
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    
    # Character variety
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    
    # Categorize
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def hash_password(password: str, algorithm: str = "sha256") -> str:
    """
    Hash a password using specified algorithm.
    
    Args:
        password: The password to hash
        algorithm: Hash algorithm ('sha256', 'sha512', 'md5')
        
    Returns:
        Hexadecimal hash string
        
    Raises:
        ValueError: If password is empty or algorithm unsupported
    """
    if not password:
        raise ValueError("Password cannot be empty")
    
    supported = ['sha256', 'sha512', 'md5']
    if algorithm not in supported:
        raise ValueError(f"Unsupported algorithm. Use: {supported}")
    
    if algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == 'sha512':
        return hashlib.sha512(password.encode()).hexdigest()
    else:  # md5
        return hashlib.md5(password.encode()).hexdigest()


def is_common_password(password: str) -> bool:
    """
    Check if password is in the list of common passwords.
    
    Args:
        password: The password to check
        
    Returns:
        True if password is common, False otherwise
    """
    common_passwords = [
        "123456", "password", "123456789", "12345678", "12345",
        "1234567", "1234567890", "qwerty", "abc123", "111111",
        "password1", "admin", "letmein", "welcome", "monkey",
        "dragon", "master", "login", "princess", "qwerty123"
    ]
    return password.lower() in common_passwords


def validate_password(password: str) -> dict:
    """
    Comprehensive password validation.
    
    Args:
        password: The password to validate
        
    Returns:
        Dictionary with validation results:
        {
            'valid': bool,
            'strength': str,
            'is_common': bool,
            'errors': list[str]
        }
    """
    result = {
        'valid': True,
        'strength': 'Unknown',
        'is_common': False,
        'errors': []
    }
    
    # Check if empty
    if not password:
        result['valid'] = False
        result['errors'].append("Password cannot be empty")
        return result
    
    # Check minimum length
    if len(password) < 8:
        result['valid'] = False
        result['errors'].append("Password must be at least 8 characters")
    
    # Check for common password
    if is_common_password(password):
        result['valid'] = False
        result['is_common'] = True
        result['errors'].append("Password is too common")
    
    # Get strength
    try:
        result['strength'] = check_password_strength(password)
    except ValueError as e:
        result['errors'].append(str(e))
    
    return result


def generate_password_hash(password: str, salt: str = "") -> str:
    """
    Generate a salted password hash.
    
    Args:
        password: The password to hash
        salt: Optional salt value
        
    Returns:
        Salted SHA-256 hash
    """
    salted = salt + password + salt
    return hashlib.sha256(salted.encode()).hexdigest()
🏋️ ZADANIA PODSTAWOWE (10 punktów - minimum do zaliczenia)
Zadanie Z1: Pierwszy test (2 punkty)
Utwórz plik test_passwords.py i napisz swój pierwszy test:

"""Unit tests for password_utils module."""
import pytest
from password_utils import check_password_strength


def test_weak_password():
    """Test that short password is classified as Weak."""
    # TODO: Napisz test sprawdzający, że hasło "abc" jest "Weak"
    pass


def test_strong_password():
    """Test that complex password is classified as Strong."""
    # TODO: Napisz test sprawdzający, że hasło "MyStr0ng!Pass2024" jest "Strong"
    pass
Jak uruchomić test:

cd lab13
pytest test_passwords.py -v
Lub na Windows (jeśli pytest nie działa):

python -m pytest test_passwords.py -v
Oczekiwany wynik:

test_passwords.py::test_weak_password PASSED
test_passwords.py::test_strong_password PASSED
Wskazówka: Użyj assert do porównania:

assert check_password_strength("abc") == "Weak"
Zadanie Z2: Testowanie wyjątków (2 punkty)
Dodaj testy sprawdzające, czy funkcja rzuca wyjątki dla nieprawidłowych danych:

def test_empty_password_raises_error():
    """Test that empty password raises ValueError."""
    # TODO: Użyj pytest.raises() aby sprawdzić, że "" rzuca ValueError
    pass


def test_none_password_raises_error():
    """Test that None password raises ValueError."""
    # TODO: Użyj pytest.raises() aby sprawdzić, że None rzuca ValueError
    pass
Składnia pytest.raises:

with pytest.raises(ValueError):
    # kod który powinien rzucić wyjątek
    funkcja_ktora_rzuci_wyjatek()
Bonus (0.5 pkt): Sprawdź też treść komunikatu błędu:

with pytest.raises(ValueError) as exc_info:
    check_password_strength("")
assert "empty" in str(exc_info.value).lower()
Zadanie Z3: Testowanie funkcji hash (2 punkty)
Dodaj testy dla funkcji hash_password:

from password_utils import hash_password


def test_sha256_hash_length():
    """Test that SHA-256 hash has correct length (64 characters)."""
    # TODO: Sprawdź, że hash SHA-256 ma długość 64 znaków
    pass


def test_sha512_hash_length():
    """Test that SHA-512 hash has correct length (128 characters)."""
    # TODO: Sprawdź, że hash SHA-512 ma długość 128 znaków
    pass


def test_same_password_same_hash():
    """Test that same password always produces same hash."""
    # TODO: Sprawdź, że to samo hasło daje ten sam hash
    pass


def test_different_passwords_different_hashes():
    """Test that different passwords produce different hashes."""
    # TODO: Sprawdź, że różne hasła dają różne hashe
    pass


def test_unsupported_algorithm_raises_error():
    """Test that unsupported algorithm raises ValueError."""
    # TODO: Sprawdź, że nieobsługiwany algorytm (np. "sha1") rzuca ValueError
    pass
Informacja o długości hashy:

MD5: 32 znaki
SHA-256: 64 znaki
SHA-512: 128 znaków
Zadanie Z4: Testowanie funkcji is_common_password (2 punkty)
from password_utils import is_common_password


def test_common_password_detected():
    """Test that common passwords are detected."""
    # TODO: Sprawdź kilka znanych słabych haseł: "123456", "password", "qwerty"
    pass


def test_uncommon_password_not_detected():
    """Test that unique passwords are not flagged as common."""
    # TODO: Sprawdź, że unikalne hasło nie jest oznaczone jako common
    pass


def test_common_password_case_insensitive():
    """Test that common password check is case insensitive."""
    # TODO: Sprawdź, że "PASSWORD" i "Password" są wykrywane jako common
    pass
Zadanie Z5: Testowanie validate_password (2 punkty)
from password_utils import validate_password


def test_valid_password():
    """Test that valid password passes all checks."""
    result = validate_password("SecurePass123!")
    # TODO: Sprawdź, że result['valid'] == True
    # TODO: Sprawdź, że result['errors'] jest pustą listą
    pass


def test_too_short_password():
    """Test that short password fails validation."""
    result = validate_password("Short1!")
    # TODO: Sprawdź, że result['valid'] == False
    # TODO: Sprawdź, że jest błąd o długości w result['errors']
    pass


def test_common_password_fails():
    """Test that common password fails validation."""
    result = validate_password("password123")
    # TODO: Sprawdź, że result['is_common'] == True
    pass
🔐 ZADANIA SECURITY (4 punkty)
Zadanie Z6: Testy bezpieczeństwa - SQL Injection (2 punkty)
Utwórz plik test_security.py:

"""Security-focused tests."""
import pytest
from password_utils import check_password_strength, hash_password


class TestSQLInjectionAttempts:
    """Test how functions handle SQL injection attempts."""
    
    def test_sql_injection_in_password(self):
        """Test that SQL injection attempt doesn't crash the function."""
        malicious_inputs = [
            "'; DROP TABLE users; --",
            "' OR '1'='1",
            "admin'--",
            "1; DELETE FROM passwords WHERE '1'='1",
        ]
        
        for payload in malicious_inputs:
            # TODO: Sprawdź, że funkcja nie crashuje dla tych inputów
            # Użyj try/except lub sprawdź, że zwraca poprawny typ
            pass
    
    def test_special_characters_in_password(self):
        """Test handling of special characters that might cause issues."""
        special_passwords = [
            "pass\x00word",      # NULL byte
            "pass\nword",        # newline
            "pass\tword",        # tab
            "pass\\word",        # backslash
            "pass'word",         # single quote
            'pass"word',         # double quote
        ]
        
        for password in special_passwords:
            # TODO: Sprawdź, że funkcja obsługuje te znaki bez crashu
            pass
Kontekst cybersecurity: W prawdziwych aplikacjach, dane od użytkownika (w tym hasła) mogą zawierać złośliwy kod. Funkcje muszą być odporne na takie próby ataków.

Zadanie Z7: Testy timing attacks (2 punkty)
import time


class TestTimingAttacks:
    """Test for potential timing vulnerabilities."""
    
    def test_hash_timing_consistency(self):
        """
        Test that hashing time doesn't vary significantly with input.
        Timing differences could leak information about the password.
        """
        short_password = "a"
        long_password = "a" * 1000
        
        # Measure time for short password (average of 100 runs)
        start = time.perf_counter()
        for _ in range(100):
            hash_password(short_password)
        short_time = time.perf_counter() - start
        
        # Measure time for long password
        start = time.perf_counter()
        for _ in range(100):
            hash_password(long_password)
        long_time = time.perf_counter() - start
        
        # TODO: Sprawdź, że różnica czasów nie jest zbyt duża
        # Różnica > 10x może wskazywać na podatność timing attack
        # Użyj: assert long_time < short_time * 10
        pass
    
    def test_common_password_check_timing(self):
        """
        Test that common password check has consistent timing.
        Early-exit could reveal if password is in the list.
        """
        # TODO: Podobny test dla is_common_password()
        # Sprawdź, czy czas sprawdzania pierwszego i ostatniego hasła z listy
        # jest podobny
        pass
Kontekst cybersecurity: Timing attacks pozwalają atakującemu zgadnąć informacje na podstawie czasu odpowiedzi. Jeśli sprawdzenie hasła "admin" trwa 1ms, a "xyzzy" trwa 5ms, atakujący wie, że "admin" jest na początku listy.

📝 ZADANIA CODE REVIEW (4 punkty)
Zadanie Z8: Code Review - znajdź błędy (2 punkty)
Przeanalizuj poniższy kod i znajdź minimum 5 błędów/problemów bezpieczeństwa.

Zapisz swoje odpowiedzi w pliku code_review.md.

# vulnerable_app.py - KOD DO ANALIZY (NIE URUCHAMIAJ!)

import sqlite3
import hashlib

def login(username, password):
    """Authenticate user and return True if valid."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Check credentials
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    
    result = cursor.fetchone()
    return result is not None


def register(username, password):
    """Register a new user."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Store user
    hashed = hashlib.md5(password.encode()).hexdigest()
    cursor.execute(f"INSERT INTO users VALUES ('{username}', '{hashed}')")
    conn.commit()
    
    print(f"User {username} registered with password hash: {hashed}")
    return True


def change_password(username, old_password, new_password):
    """Change user password."""
    if login(username, old_password):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        hashed = hashlib.md5(new_password.encode()).hexdigest()
        cursor.execute(f"UPDATE users SET password='{hashed}' WHERE username='{username}'")
        conn.commit()
        return True
    return False


def get_user_data(user_id):
    """Get user data by ID."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM users WHERE id={user_id}")
    return cursor.fetchone()


PASSWORD_REQUIREMENTS = {
    'min_length': 4,
    'require_special': False,
    'require_uppercase': False
}


def validate_new_password(password):
    """Validate password meets requirements."""
    if len(password) >= PASSWORD_REQUIREMENTS['min_length']:
        return True
    return False
Format odpowiedzi w code_review.md:

# Code Review Report - vulnerable_app.py

## Błąd 1: [nazwa błędu]
- **Linia:** X
- **Problem:** [opis]
- **Ryzyko:** [niskie/średnie/wysokie/krytyczne]
- **Naprawa:** [jak naprawić]

## Błąd 2: ...
Podpowiedzi co szukać:

SQL Injection
Słabe hashowanie
Wyciek informacji
Brak walidacji
Zbyt słabe wymagania
Niezamknięte połączenia
Zadanie Z9: Analiza statyczna z pylint (2 punkty)
Uruchom pylint na pliku password_utils.py:
pylint password_utils.py
Zrób zrzut ekranu wyniku
Uruchom pylint na swoim pliku testowym:
pylint test_passwords.py
Zrób zrzut ekranu wyniku
W pliku code_review.md dodaj sekcję:
## Analiza pylint

### password_utils.py
- Wynik: X.XX/10
- Główne uwagi: [lista]

### test_passwords.py  
- Wynik: X.XX/10
- Co poprawiłem po zobaczeniu uwag: [lista]
🚀 ZADANIA ROZSZERZONE (6 punktów - dla oceny 5.0)
Zadanie Z10: Parametryzacja testów (2 punkty)
Przepisz testy używając @pytest.mark.parametrize:

@pytest.mark.parametrize("password,expected", [
    ("abc", "Weak"),
    ("abcdefgh", "Medium"),
    ("Abcdefgh1", "Medium"),
    ("MyStr0ng!Pass", "Strong"),
    # TODO: Dodaj więcej przypadków
])
def test_password_strength_parametrized(password, expected):
    """Test password strength with multiple inputs."""
    assert check_password_strength(password) == expected
Wymagania:

Minimum 10 przypadków testowych
Pokryj wszystkie kategorie (Weak, Medium, Strong)
Dodaj przypadki brzegowe (dokładnie 8 znaków, dokładnie 12 znaków, itp.)
Zadanie Z11: Testy fixtures (2 punkty)
Użyj fixtures do współdzielenia danych testowych:

@pytest.fixture
def sample_passwords():
    """Provide sample passwords for testing."""
    return {
        'weak': ['abc', '123', 'pass'],
        'medium': ['Password1', 'Abcdefgh1'],
        'strong': ['MyStr0ng!Pass2024', 'C0mpl3x!P@ssw0rd']
    }


@pytest.fixture
def common_passwords_list():
    """Provide list of known common passwords."""
    return ["123456", "password", "qwerty", "admin"]


def test_weak_passwords_with_fixture(sample_passwords):
    """Test all weak passwords from fixture."""
    for password in sample_passwords['weak']:
        assert check_password_strength(password) == "Weak"


# TODO: Dodaj więcej testów używających fixtures
Zadanie Z12: Test coverage (2 punkty)
Zainstaluj pytest-cov:
pip install pytest-cov
Uruchom testy z pomiarem pokrycia:
pytest --cov=password_utils --cov-report=html test_passwords.py
Otwórz raport htmlcov/index.html w przeglądarce
Dodaj brakujące testy, aby osiągnąć minimum 90% pokrycia
Zrób zrzut ekranu raportu pokrycia i dodaj do folderu screenshots/
📚 Materiały pomocnicze
Przydatne komendy pytest
# Uruchom wszystkie testy
pytest

# Uruchom z verbose output
pytest -v

# Uruchom konkretny plik
pytest test_passwords.py

# Uruchom konkretny test
pytest test_passwords.py::test_weak_password

# Uruchom testy pasujące do wzorca
pytest -k "hash"

# Pokaż print() w testach
pytest -s

# Zatrzymaj się na pierwszym błędzie
pytest -x
Struktura testu (AAA)
def test_something():
    # Arrange - przygotuj dane
    password = "TestPassword123!"
    
    # Act - wykonaj akcję
    result = check_password_strength(password)
    
    # Assert - sprawdź wynik
    assert result == "Strong"
Częste błędy
Brak import pytest - potrzebny do pytest.raises()
Nazwa pliku nie zaczyna się od test_ - pytest go nie znajdzie
Nazwa funkcji nie zaczyna się od test_ - pytest ją pominie
Porównanie == zamiast assert - test zawsze przejdzie!
❓ FAQ
P: Czy mogę używać innych narzędzi niż pytest? O: Nie, proszę użyć pytest - to standard w branży.

P: Ile testów muszę napisać? O: Minimum to zadania Z1-Z5 (około 15 testów). Dla wyższej oceny - więcej.

P: Co jeśli test nie przechodzi? O: To może oznaczać, że znalazłeś bug w kodzie! Sprawdź, czy Twój test jest poprawny.

P: Czy mogę modyfikować password_utils.py? O: Nie, testujemy istniejący kod. Możesz tylko pisać testy.

P: Jak oddać zadanie? O: Spakuj folder lab13/ do ZIP i wyślij mailem przed egzaminem.

🎯 Checklist przed oddaniem
Plik test_passwords.py zawiera testy Z1-Z5
Wszystkie testy przechodzą (pytest pokazuje zielone)
Plik test_security.py zawiera testy Z6-Z7 (jeśli robisz)
Plik code_review.md zawiera raport (jeśli robisz)
Folder screenshots/ zawiera zrzuty z pylint (jeśli robisz)
Kod jest czytelny i ma komentarze
ZIP zawiera wszystkie pliki
Powodzenia! 🚀

"Testing shows the presence, not the absence of bugs." — Edsger Dijkstra