
Lab07 zadania studenci
Lab 7: Text Processing & Regular Expressions
Zadania dla studentów
Przedmiot: Introduction to Programming
Kierunek: Cybersecurity, rok I
Prowadzący: Bartosz Lewandowski
Czas: 90 minut
Język programowania: Python 3

📋 Informacje ogólne
Struktura laboratorium:
Sekcja 1: Rozgrzewka - Character & String Basics (3 zadania, 3.0 pkt)
Sekcja 2: String Processing Fundamentals (3 zadania, 3.0 pkt)
Sekcja 3: Regular Expressions - Basics (5 zadań, 5.0 pkt)
Sekcja 4: Regular Expressions - Intermediate (4 zadania, 5.0 pkt)
Sekcja 5: Regular Expressions - Advanced (3 zadania, 6.0 pkt)
Sekcja 6: AI Text Detection - Bonus (2 zadania, 3.0 pkt)
Razem: 20 zadań, 25.0 punktów (22.0 podstawowe + 3.0 bonus)

System oceniania:
Ocena	Punkty potrzebne	% z podstawy (22 pkt)
3.0	11.0 / 22.0	50%
3.5	13.0 / 22.0	59%
4.0	15.0 / 22.0	68%
4.5	17.0 / 22.0	77%
5.0	19.0 / 22.0	86%
Bonus: Sekcja 6 (+3.0 pkt) może poprawić ocenę o 0.5

Wskazówki:
✅ Regex Cheatsheet dostępny! - Plik Lab07_Regex_Cheatsheet.md
✅ Zaczynaj od łatwych - Sekcje 1-2 to rozgrzewka
✅ Testuj na regex101.com - Online tester dla debugowania patterns
✅ Pytaj prowadzącego - Jeśli utkniesz, pomoc jest dostępna
✅ Raw strings! - Zawsze używaj r"pattern" dla regex

SEKCJA 1: Rozgrzewka - Character & String Basics
Cel: Przypomnienie operacji na znakach i podstawach stringów
Czas: ~12 minut
Punkty: 3.0 (min do zaliczenia: 1.5)

Zadanie 1.1: ASCII Explorer (0.5 pkt)
Napisz program, który wczytuje pojedynczy znak i wyświetla jego kod ASCII.

Input:

A
Output:

65
Wymagania:

Użyj funkcji input() do wczytania znaku
Użyj funkcji ord() do konwersji na kod ASCII
Wyświetl tylko liczbę (bez dodatkowego tekstu)
Hint: ord('A') zwraca 65

Zadanie 1.2: Caesar Cipher - Basic (1.5 pkt)
Zaszyfruj tekst szyfrem Cezara z przesunięciem o 3 pozycje w prawo.

Zasady:

Szyfruj TYLKO małe litery a-z
Po z wracamy do a (wraparound)
Wielkie litery, cyfry, spacje - pozostają bez zmian
Input:

hello world
Output:

khoor zruog
Wyjaśnienie:

h (kod 104) + 3 = k (kod 107)
e → h, l → o, o → r
Spacja pozostaje bez zmian
Wymagania:

Użyj ord() i chr() do konwersji
Pamiętaj o wraparound: jeśli przekroczysz z, wróć do a
Cybersecurity context: Szyfr Cezara to najprostszy szyfr substytucyjny. Łatwo złamać (tylko 26 możliwości). W praktyce używa się znacznie silniejszych algorytmów (AES, RSA).

Zadanie 1.3: Case Converter (1.0 pkt)
Napisz funkcję fix_title_case(text), która naprawia "AI Title Case" na normalny polski tekst.

AI Title Case: Każde słowo zaczyna się od wielkiej litery (kalka z angielskiego)
Normalny polski: Tylko pierwsze słowo zdania z wielkiej litery

Input:

To Jest Przykładowy Tekst. Kolejne Zdanie Tutaj.
Output:

To jest przykładowy tekst. Kolejne zdanie tutaj.
Wymagania:

Podziel tekst na zdania (separator: kropka + spacja)
Dla każdego zdania:
Pierwsze słowo: wielka pierwsza litera, reszta małe
Pozostałe słowa: wszystkie litery małe
Złącz zdania z powrotem
Hint: Użyj .split('. '), .capitalize(), .lower()

Cybersecurity context: Detekcja AI-generated content - Title Case to jeden z głównych red flags.

SEKCJA 2: String Processing Fundamentals
Cel: Podstawowe operacje na stringach (bez regex)
Czas: ~15 minut
Punkty: 3.0 (min do zaliczenia: 1.5)

Zadanie 2.1: Password Strength Checker (1.0 pkt)
Sprawdź siłę hasła według następujących kryteriów:

Kryteria:

WEAK: Nie spełnia wymogów MEDIUM
MEDIUM: Min 8 znaków + zawiera cyfrę
STRONG: MEDIUM + zawiera wielką literę
Przykłady:

password → WEAK (brak cyfry)
password1 → MEDIUM (8+ znaków, cyfra, ale brak wielkiej)
Password1 → STRONG (wszystkie kryteria spełnione)
Wymagania:

Funkcja: check_password_strength(password) → zwraca "WEAK", "MEDIUM" lub "STRONG"
Użyj metod stringów: .isdigit(), .isupper(), len()
Cybersecurity context: Podstawowa walidacja haseł. W produkcji używa się bardziej zaawansowanych metod (entropy, common passwords check).

Zadanie 2.2: Simple Log Parser (1.0 pkt)
Parsuj linię z (uproszczonego) access loga i wyciągnij komponenty.

Format loga:

IP - METHOD ENDPOINT - STATUS
Input:

192.168.1.1 - GET /admin - 403
Output:

IP: 192.168.1.1
Method: GET
Endpoint: /admin
Status: 403
Wymagania:

Użyj .split() do podzielenia linii
Wyciągnij 4 komponenty: IP, Method, Endpoint, Status
Usuń białe znaki (.strip())
Cybersecurity context: Parsing security logs - pierwszy krok w analizie incydentów.

Zadanie 2.3: Count Suspicious Keywords (1.0 pkt)
Policz ile razy w tekście występują podejrzane słowa (case-insensitive).

Lista suspicious keywords:

SUSPICIOUS = ['password', 'urgent', 'click here', 'verify', 'credit card']
Input:

URGENT: Verify your PASSWORD now! Click here to update credit card details.
Output:

4
Wyjaśnienie: Znaleziono urgent, verify, password, click here (4 słowa)

Wymagania:

Przekonwertuj tekst na lowercase (.lower())
Policz wystąpienia każdego keyword
Zwróć sumę
Cybersecurity context: Phishing detection - keyword analysis to podstawowa technika wykrywania podejrzanych emaili.

SEKCJA 3: Regular Expressions - Basics
Cel: Nauka podstawowych operatorów regex
Czas: ~25 minut
Punkty: 5.0 (min do zaliczenia: 2.5)

Zadanie 3.1: Match Simple Pattern (0.5 pkt)
Sprawdź czy tekst zawiera słowo admin (case-insensitive).

Przykłady:

"User logged to admin panel" → True
"User logged to ADMIN panel" → True
"User logged to user panel" → False
Wymagania:

import re

def contains_admin(text):
    # Twój kod tutaj
    pass
Hint: re.search(r"admin", text, re.IGNORECASE)

Cybersecurity context: Keyword detection w security logs.

Zadanie 3.2: Email Validator (1.0 pkt)
Zwaliduj email używając regex.

Pattern:

^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
Wyjaśnienie pattern:

^ - początek stringa
[a-zA-Z0-9._-]+ - nazwa użytkownika (litery, cyfry, kropka, underscore, myślnik)
@ - wymagany znak @
[a-zA-Z0-9.-]+ - domena
\. - wymagana kropka (escaped!)
[a-zA-Z]{2,} - TLD minimum 2 znaki (com, pl, org)
$ - koniec stringa
Przykłady VALID:

user@example.com
john.doe@company.co.uk
test_123@domain.org
Przykłady INVALID:

@example.com (brak nazwy użytkownika)
user@ (brak domeny)
user.example.com (brak @)
Wymagania:

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    # Zwróć True jeśli valid, False jeśli nie
Cybersecurity context: Input validation - pierwsza linia obrony przed injection attacks.

Zadanie 3.3: Find All Digits (1.0 pkt)
Znajdź wszystkie liczby w tekście.

Pattern: \d+

Input:

Port 8080 on 192.168.1.1 failed at 14:32
Output:

['8080', '192', '168', '1', '1', '14', '32']
Wymagania:

import re

def find_numbers(text):
    pattern = r"\d+"
    return re.findall(pattern, text)
Hint: re.findall() zwraca listę wszystkich matchów

Cybersecurity context: Extracting numerical data z logów (porty, IP parts, timestamps).

Zadanie 3.4: Phone Number Extractor (1.5 pkt)
Znajdź polskie numery telefonów w tekście.

Formaty do wykrycia:

+48 123 456 789 (z prefiksem międzynarodowym)
123-456-789 (z myślnikami)
123456789 (bez separatorów)
Pattern:

r"(\+48\s?)?\d{3}[\s-]?\d{3}[\s-]?\d{3}"
Wyjaśnienie:

(\+48\s?)? - opcjonalny prefix +48 z optional spacją (grupa non-capturing można użyć (?:...))
\d{3} - dokładnie 3 cyfry
[\s-]? - opcjonalna spacja lub myślnik
powtórzone 3 razy dla trzech grup cyfr
Przykładowy input:

Call me at +48 123 456 789 or 987-654-321 for urgent matters.
Przykładowy output:

['+48 123 456 789', '987-654-321']
Wymagania:

import re

def extract_phone_numbers(text):
    pattern = r"(\+48\s?)?\d{3}[\s-]?\d{3}[\s-]?\d{3}"
    return re.findall(pattern, text)
Cybersecurity context: OSINT - extracting contact info from leaked data.

Zadanie 3.5: IP Address Extractor (1.0 pkt)
Wyciągnij adresy IPv4 z tekstu.

Pattern: \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}

Input:

Failed login from 192.168.1.1 and 10.0.0.5 detected.
Output:

['192.168.1.1', '10.0.0.5']
Wymagania:

import re

def extract_ips(text):
    pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    return re.findall(pattern, text)
Bonus challenge (opcjonalnie, bez punktów): Zwaliduj że każdy oktet jest 0-255.

Cybersecurity context: Security log analysis - identyfikacja źródeł ataków.

SEKCJA 4: Regular Expressions - Intermediate
Cel: Zaawansowane patterns, alternacje, character classes
Czas: ~25 minut
Punkty: 5.0 (min do zaliczenia: 2.5)

Zadanie 4.1: Extract URLs (1.0 pkt)
Wyciągnij URLs (http/https) z tekstu.

Pattern:

r"https?://[a-zA-Z0-9.-]+(/[a-zA-Z0-9._-]*)?"
Wyjaśnienie:

https? - http LUB https (? = optional 's')
:// - literal ://
[a-zA-Z0-9.-]+ - domena (litery, cyfry, kropka, myślnik)
(/[a-zA-Z0-9._-]*)? - opcjonalna ścieżka
Input:

Visit https://example.com/page and http://test.org for more info.
Output:

['https://example.com/page', 'http://test.org']
Wymagania:

import re

def extract_urls(text):
    pattern = r"https?://[a-zA-Z0-9.-]+(/[a-zA-Z0-9._-]*)?"
    return re.findall(pattern, text)
Cybersecurity context: Malicious URL detection w phishing emails.

Zadanie 4.2: Find Dates in Text (1.5 pkt)
Znajdź daty w dwóch formatach:

Polski: DD.MM.YYYY
ISO: YYYY-MM-DD
Pattern z alternacją:

r"\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2}"
Wyjaśnienie:

\d{2}\.\d{2}\.\d{4} - format polski (25.12.2024)
| - OR operator (alternacja)
\d{4}-\d{2}-\d{2} - format ISO (2024-12-25)
Przykładowy input:

Event scheduled on 25.12.2024 or 2024-12-25 (both dates valid).
Przykładowy output:

['25.12.2024', '2024-12-25']
Wymagania:

import re

def find_dates(text):
    pattern = r"\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2}"
    return re.findall(pattern, text)
Cybersecurity context: Timeline extraction z security logs - ważne dla incident response.

Zadanie 4.3: Extract Hashtags (1.0 pkt)
Wyciągnij hashtagi z tekstu social media.

Pattern: #[a-zA-Z0-9_]+

Wyjaśnienie:

# - literal hashtag
[a-zA-Z0-9_]+ - litery, cyfry, underscore (1 lub więcej)
Input:

Check #cybersecurity and #InfoSec trends! #2024_trends are interesting.
Output:

['#cybersecurity', '#InfoSec', '#2024_trends']
Wymagania:

import re

def extract_hashtags(text):
    pattern = r"#[a-zA-Z0-9_]+"
    return re.findall(pattern, text)
Cybersecurity context: OSINT - social media monitoring, threat intelligence.

Zadanie 4.4: Validate Hex Color Code (1.5 pkt)
Sprawdź czy string to prawidłowy hex color code.

Formaty:

#RRGGBB - pełny (np. #FF5733)
#RGB - skrócony (np. #F57)
Pattern:

r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
Wyjaśnienie pattern:

^ - początek stringa (exact match!)
# - literal hashtag
[A-Fa-f0-9]{6} - dokładnie 6 hex digits (RRGGBB)
| - LUB
[A-Fa-f0-9]{3} - dokładnie 3 hex digits (RGB)
$ - koniec stringa (exact match!)
Przykłady:

#FF5733 → Valid (pełny format)
#F57 → Valid (skrócony format)
#GG0000 → Invalid (G nie jest hex)
FF5733 → Invalid (brak #)
#FF57 → Invalid (4 znaki - ani 3 ani 6)
Wymagania:

import re

def validate_hex_color(color):
    pattern = r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
    return bool(re.match(pattern, color))
Cybersecurity context: XSS prevention - walidacja user input w CSS, zapobieganie CSS injection.

SEKCJA 5: Regular Expressions - Advanced
Cel: Production-grade techniki: groups, lookaheads
Czas: ~23 minut
Punkty: 6.0 (min do zaliczenia: 3.0)

Zadanie 5.1: URL Parser with Capturing Groups (2.0 pkt)
Wyciągnij i rozdziel części URL używając capturing groups.

Pattern:

r"(https?)://([a-zA-Z0-9.-]+)(/[a-zA-Z0-9._/-]*)?"
Wyjaśnienie capturing groups:

(https?) - group 1: protokół (http lub https)
([a-zA-Z0-9.-]+) - group 2: domena
(/[a-zA-Z0-9._/-]*)? - group 3: ścieżka (opcjonalna)
Przykładowy input:

Visit https://example.com/path/to/page for details.
Przykładowy output:

Protocol: https
Domain: example.com
Path: /path/to/page
Wymagania:

import re

def parse_url(text):
    pattern = r"(https?)://([a-zA-Z0-9.-]+)(/[a-zA-Z0-9._/-]*)?"
    match = re.search(pattern, text)
    
    if match:
        protocol = match.group(1)  # lub match.groups()[0]
        domain = match.group(2)    # lub match.groups()[1]
        path = match.group(3) if match.group(3) else "/"  # default
        
        print(f"Protocol: {protocol}")
        print(f"Domain: {domain}")
        print(f"Path: {path}")
    else:
        print("No URL found")
Hint:

match.group(0) - cały match
match.group(1) - pierwsza grupa
match.groups() - tuple wszystkich grup
Cybersecurity context: Malicious URL analysis - rozbijanie URL na komponenty dla głębszej analizy (domain reputation, suspicious paths).

Zadanie 5.2: Password Validator with Lookaheads (2.0 pkt)
⚠️ ZAAWANSOWANE ZADANIE - Production-grade technique!

Zwaliduj hasło używając JEDNEGO regex z lookahead assertions.

Wymagania dla hasła:

Minimum 8 znaków
Co najmniej 1 mała litera (a-z)
Co najmniej 1 wielka litera (A-Z)
Co najmniej 1 cyfra (0-9)
Co najmniej 1 znak specjalny (@$!%*?&)
Pattern:

r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
Wyjaśnienie lookahead (?=...):

Lookahead to "spojrzenie w przód" - sprawdza warunek BEZ konsumowania znaków.

Rozbijmy pattern:

^                    # Początek stringa
(?=.*[a-z])         # Lookahead: gdzieś dalej musi być mała litera
(?=.*[A-Z])         # Lookahead: gdzieś dalej musi być wielka litera
(?=.*\d)            # Lookahead: gdzieś dalej musi być cyfra
(?=.*[@$!%*?&])     # Lookahead: gdzieś dalej musi być znak specjalny
.{8,}               # Właściwy match: minimum 8 dowolnych znaków
$                    # Koniec stringa
Kluczowa różnica: Wszystkie lookaheady sprawdzają od TEGO SAMEGO miejsca (początku), więc wszystkie warunki muszą się zgodzić!

Przykłady:

SecureP@ss1 → Valid (8 znaków, wszystkie wymagania spełnione)
Password1! → Valid (10 znaków, wszystkie wymagania)
weakpass → Invalid (brak wielkich, cyfr, specjalnych)
WEAK123! → Invalid (brak małych liter)
Pass1! → Invalid (tylko 6 znaków, minimum to 8)
Wymagania:

import re

def validate_strong_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
    return bool(re.match(pattern, password))

# Test cases
print(validate_strong_password("SecureP@ss1"))   # True
print(validate_strong_password("weakpass"))      # False
Dlaczego to jest trudne?

Lookaheads są koncepcyjnie skomplikowane
Ale pattern jest BARDZO potężny - jedna linia zamiast wielu ifów!
Cybersecurity context: Password policy enforcement - ten DOKŁADNY pattern jest używany w produkcji przez banki, portale rządowe, systemy enterprise. To jest real-world security!

Zadanie 5.3: Log Parser with Named Groups (2.0 pkt)
Parsuj Apache access log używając named capturing groups.

Format logu:

IP - METHOD ENDPOINT - STATUS
Pattern z named groups:

r"(?P<ip>\d+\.\d+\.\d+\.\d+) - (?P<method>\w+) (?P<endpoint>/\S+) - (?P<status>\d{3})"
Wyjaśnienie named groups (?P<name>...):

Named groups to capturing groups z nazwą zamiast numeru:

(?P<ip>...) - grupa o nazwie "ip"
(?P<method>...) - grupa o nazwie "method"
itd.
Zalety:

Czytelniejszy kod: match.group('ip') zamiast match.group(1)
Łatwiejsze utrzymanie - nie musisz pamiętać numerów
Production-grade - używane w SIEM systems, fail2ban, security tools
Przykładowy input:

192.168.1.1 - GET /admin - 403
10.0.0.5 - POST /login - 401
Przykładowy output (dla pierwszej linii):

IP: 192.168.1.1
Method: GET
Endpoint: /admin
Status: 403
Wymagania:

import re

def parse_log_line(log_line):
    pattern = r"(?P<ip>\d+\.\d+\.\d+\.\d+) - (?P<method>\w+) (?P<endpoint>/\S+) - (?P<status>\d{3})"
    match = re.search(pattern, log_line)
    
    if match:
        print(f"IP: {match.group('ip')}")
        print(f"Method: {match.group('method')}")
        print(f"Endpoint: {match.group('endpoint')}")
        print(f"Status: {match.group('status')}")
    else:
        print("Invalid log format")

# Test
parse_log_line("192.168.1.1 - GET /admin - 403")
Alternatywny sposób (dict):

match = re.search(pattern, log_line)
if match:
    log_data = match.groupdict()  # Zwraca dict z nazwami grup
    print(log_data)
    # {'ip': '192.168.1.1', 'method': 'GET', 'endpoint': '/admin', 'status': '403'}
Cybersecurity context: Security log parsing - SIEM systems (Splunk, ELK) używają tej techniki do strukturyzacji logów. fail2ban używa named groups do wykrywania failed login attempts.

SEKCJA 6: AI Text Detection - Bonus Challenge
Cel: Praktyczne zastosowanie regex + string processing
Czas: ~15 minut (opcjonalnie)
Punkty: 3.0 BONUS (nieobowiązkowe!)

Zadanie 6.1: AI Buzzword Detector with Regex (1.5 pkt)
Użyj regex do znalezienia typowych "AI phrases" (case-insensitive).

Lista AI buzzwords:

"warto zauważyć"
"należy podkreślić"
"w kontekście"
"mam nadzieję"
"z przyjemnością"
"podsumowując"
Pattern:

r"(warto zauważyć|należy podkreślić|w kontekście|mam nadzieję|z przyjemnością|podsumowując)"
Input:

Warto zauważyć, że w kontekście AI należy podkreślić znaczenie tego tematu.
Output:

3 AI phrases found: ['Warto zauważyć', 'w kontekście', 'należy podkreślić']
Wymagania:

import re

def detect_ai_buzzwords(text):
    pattern = r"(warto zauważyć|należy podkreślić|w kontekście|mam nadzieję|z przyjemnością|podsumowując)"
    matches = re.findall(pattern, text, re.IGNORECASE)
    
    print(f"{len(matches)} AI phrases found: {matches}")
    return len(matches)
Cybersecurity context: Bot detection w social media - automated accounts często używają tych fraz.

Zadanie 6.2: AI Text Analyzer - Literatura Klasyczna (1.5 pkt)
🏆 COMPREHENSIVE CHALLENGE - Połączenie wszystkich umiejętności!

Dostaniesz plik Lab07_Dataset_Literatura.txt z 10 tekstami:
https://share.note.sx/yogneodm#Z9Whwk/lZoV6ROch+bldgKfFD62wansQfRaYmjrfGew

Teksty 1-5: Fragmenty autentycznej literatury polskiej (Mickiewicz, Prus, Sienkiewicz, Lem, Szymborska)
Teksty 6-10: AI próbujące naśladować klasykę (z charakterystycznymi błędami)
Twoje zadanie: Napisz detektor który sklasyfikuje które teksty są AI-generated.

Red flags do wykrycia:
1. Title Case Pattern (30 pts)

Pattern: \b[A-ZŁĆŚŹŻ][a-złćęńóśźż]+ (każde słowo z wielkiej)
Policz % słów rozpoczynających się wielką literą
Jeśli >60% → +30 pts
2. AI Buzzwords (30 pts)

Użyj pattern z Zadania 6.1
Jeśli >2 buzzwords → +30 pts
3. Numbered Lists (20 pts)

Pattern: ^\d+\. (cyfra + kropka na początku linii)
Jeśli wykryto → +20 pts
4. Słowo "Podsumowując" (20 pts)

Jeśli występuje → +20 pts
Scoring:
< 40 pts: HUMAN
≥ 40 pts: AI-GENERATED
Przykładowy output:
========================================
AI TEXT DETECTION REPORT
========================================
Text 1 (Pan Tadeusz):     10% - HUMAN ✓
Text 2 (Lalka):           5% - HUMAN ✓
Text 3 (Quo Vadis):       15% - HUMAN ✓
Text 4 (Solaris):         20% - HUMAN ✓
Text 5 (Szymborska):      8% - HUMAN ✓

Text 6 (Fake Tadeusz):    90% - AI-GENERATED ✓
Text 7 (Fake Lalka):      95% - AI-GENERATED ✓
Text 8 (Fake Quo Vadis):  85% - AI-GENERATED ✓
Text 9 (Fake Solaris):    88% - AI-GENERATED ✓
Text 10 (Fake Szymborska): 100% - AI-GENERATED ✓
========================================
ACCURACY: 10/10 (100%)
========================================
Szablon kodu:
import re

def detect_title_case(text):
    """Wykryj % słów z Title Case"""
    words = text.split()
    capitalized = sum(1 for word in words if word and word[0].isupper())
    ratio = capitalized / len(words) if words else 0
    return 30 if ratio > 0.6 else 0

def detect_ai_buzzwords(text):
    """Policz AI buzzwords"""
    pattern = r"(warto zauważyć|należy podkreślić|w kontekście|mam nadzieję|z przyjemnością|podsumowując)"
    matches = re.findall(pattern, text, re.IGNORECASE)
    return 30 if len(matches) > 2 else 0

def detect_numbered_list(text):
    """Wykryj listy numerowane"""
    pattern = r"^\d+\."
    if re.search(pattern, text, re.MULTILINE):
        return 20
    return 0

def detect_podsumowujac(text):
    """Wykryj słowo 'podsumowując'"""
    return 20 if "podsumowując" in text.lower() else 0

def analyze_text(text, text_name):
    """Główna funkcja analizy"""
    score = 0
    score += detect_title_case(text)
    score += detect_ai_buzzwords(text)
    score += detect_numbered_list(text)
    score += detect_podsumowujac(text)
    
    classification = "AI-GENERATED" if score >= 40 else "HUMAN"
    print(f"{text_name}: {score}% - {classification}")
    
    return classification

# Wczytaj dataset i przeanalizuj wszystkie teksty
# (implementacja wczytywania pliku - do studenta)
Wymagania:

Wczytaj plik Lab07_Dataset_Literatura.txt
Przeanalizuj każdy z 10 tekstów
Oblicz AI score dla każdego
Sklasyfikuj: HUMAN lub AI-GENERATED
Wyświetl raport z accuracy
Cybersecurity context: Real-world AI detection pipelines używają podobnych technik - pattern matching + scoring. To jest fundament systemów takich jak GPTZero, Copyleaks.

📊 Podsumowanie punktacji
Punkty możliwe do zdobycia:
Sekcja	Zadań	Punktów	Minimum (50%)
1. Rozgrzewka	3	3.0	1.5
2. String Processing	3	3.0	1.5
3. Regex Basics	5	5.0	2.5
4. Regex Intermediate	4	5.0	2.5
5. Regex Advanced	3	6.0	3.0
PODSTAWA	18	22.0	11.0
6. AI Detection (BONUS)	2	3.0	-
RAZEM	20	25.0	-
Progi ocen (z podstawy 22.0 pkt):
3.0: 11.0 pkt (50%)
3.5: 13.0 pkt (59%)
4.0: 15.0 pkt (68%)
4.5: 17.0 pkt (77%)
5.0: 19.0 pkt (86%)
Bonus: Sekcja 6 może poprawić ocenę o 0.5

💡 Wskazówki finalne
Strategia rozwiązywania:
Zacznij od Sekcji 1-2 (rozgrzewka, łatwe punkty)
Sekcja 3 (Regex Basics) - fundamenty, MUSISZ to zrozumieć
Sekcja 4 (Intermediate) - więcej praktyki z patterns
Sekcja 5 (Advanced) - trudne, ale dają dużo punktów
Sekcja 6 (Bonus) - jeśli starczy czasu, fun challenge!
Debugging regex:
regex101.com - wklej pattern i tekst, zobacz live matching
Python REPL - testuj patterns interaktywnie:
import rere.search(r"pattern", "test text")
Print intermediate results - debuguj krok po kroku
Najczęstsze błędy:
❌ Zapominanie o r"" (raw string)
❌ Nie escapowanie znaków specjalnych (. → \.)
❌ Używanie match() zamiast search()
❌ Greedy matching (.* zamiast .*?)

Jeśli utkniesz:
Przeczytaj Regex Cheatsheet
Testuj na regex101.com
Zapytaj prowadzącego
Skip zadanie i wróć później
🚀 Powodzenia!
Pamiętaj:

Regex wygląda strasznie, ale jest logiczny
Masz cheatsheet - używaj go!
50% to minimum - totally doable
Pytaj jeśli coś niejasne
Good luck and happy coding! 💪