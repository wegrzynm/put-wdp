
Lab10 zadania
🧵 LAB 10: PARALLEL PROCESSING - ZADANIA
Kurs: Introduction to Programming (Cybersecurity)
Prowadzący: Bartosz Lewandowski
Czas: 90 minut (15 min wykład + 75 min zadania)
Punkty: 10 (minimum) - 20 (rozszerzony)

📋 INFORMACJE WSTĘPNE
System punktowy:
MINIMUM (10 pkt = 3.0): Zadania 1.1, 1.2, 2.1, 2.2
ROZSZERZONY (do 20 pkt): + Zadania 3.1, 3.2, bonusy
Skala ocen:
10-11 pkt → 3.0
12-13 pkt → 3.5
14-15 pkt → 4.0
16-17 pkt → 4.5
18-20 pkt → 5.0
Narzędzia:
Python 3.x (moduł threading wbudowany)
Programiz / OneCompiler (online) LUB Python lokalnie
Dozwolone: Google, dokumentacja, AI (ale zrozumcie kod!)
⚠️ Uwaga: Jeśli w Zadaniu 2.1 ZAWSZE dostajesz poprawny wynik (2500/4000), platforma może mieć ograniczenia. Kod został zoptymalizowany aby race condition była widoczna na większości platform, ale jeśli problem się powtarza - spróbuj Python lokalnie lub innej platformy online (Repl.it, OnlineGDB).

Oddawanie:
Format: Pojedynczy plik .py z wszystkimi zadaniami
Naming: lab10_imie_nazwisko.py
Deadline: [data - uzupełni prowadzący]
🎯 CELE LABORATORIUM
Po tym laboratorium będziesz potrafić:

✅ Tworzyć i uruchamiać wątki w Pythonie (threading.Thread)
✅ Rozpoznawać i naprawiać race conditions
✅ Używać semaforów do synchronizacji (threading.Semaphore)
✅ Stosować wielowątkowość w praktycznych zadaniach cybersecurity
✅ Rozumieć ograniczenia (GIL, Prawo Amdahla, deadlock)
💡 PRZYPOMNIENIE Z WYKŁADU
Threading basics:
import threading

def funkcja():
    print("Hello from thread!")

watek = threading.Thread(target=funkcja)
watek.start()  # Uruchom asynchronicznie
watek.join()   # Poczekaj na zakończenie
Race condition:
# counter += 1 to NIE jedna operacja!
# To faktycznie:
temp = counter  # READ
temp = temp + 1 # ADD
counter = temp  # WRITE
# ← Tutaj inne wątki mogą "wejść" między te linie!
Mutex (semaphore):
mutex = threading.Semaphore(1)  # Binary semaphore

mutex.acquire()  # Zamknij sekcję krytyczną
# ... kod który tylko 1 wątek może wykonywać naraz ...
mutex.release()  # Odblokuj
⚠️ WAŻNE OSTRZEŻENIA
1. GIL (Global Interpreter Lock)
Python ma globalny zamek - tylko 1 wątek wykonuje kod Pythona naraz.

CPU-bound (obliczenia): threading NIE przyspiesza! ❌
I/O-bound (czekanie): threading DZIAŁA! ✅
Dzisiejsze zadania to I/O-bound (sieć, hashowanie w C) - threading będzie działał!

2. Legalność (Port Scanning)
⚠️ Skanowanie portów jest LEGALNE tylko na własnym komputerze (localhost)!

✅ OK: 127.0.0.1, localhost
❌ NIELEGALNE: Skanowanie obcych serwerów bez zgody
Nie łamcie prawa! Skanujcie tylko swoje maszyny.

3. Common mistakes
Używanie .run() zamiast .start() → kod się wykona sekwencyjnie
Brak .join() → program kończy się przed wątkami
Zapomnienie global przy modyfikacji zmiennych globalnych
Brak mutex przy współdzielonych danych → race condition
📝 ZADANIA
CZĘŚĆ 1: PODSTAWY THREADINGU (5 pkt)
Zadanie 1.1: "Hello from Threads" (2 pkt)
Opis:
Utwórz 5 wątków. Każdy wątek wypisuje swoje ID i aktualny timestamp.

Wymagania:

Funkcja worker(thread_id) wypisuje: Thread-{id}: {timestamp}
Uruchom 5 wątków (ID: 0-4)
Poczekaj na zakończenie wszystkich wątków (.join())
Wypiszesz "All threads finished"
Przykładowy output:

Thread-0: 14:23:45
Thread-2: 14:23:45  ← Kolejność może być losowa!
Thread-1: 14:23:45
Thread-4: 14:23:45
Thread-3: 14:23:46
All threads finished
Wskazówka:
Użyj time.strftime("%H:%M:%S") do pobrania czasu.

Kod startowy:

import threading
import time

def worker(thread_id):
    # TODO: Wypisz ID i timestamp
    pass

# TODO: Stwórz 5 wątków
# TODO: Uruchom wszystkie (.start())
# TODO: Poczekaj na wszystkie (.join())
print("All threads finished")
Zadanie 1.2: "Speedup Demo" (3 pkt)
Opis:
Symulacja pobierania 10 plików. Porównaj czas sekwencyjny vs równoległy.

Wymagania:

Funkcja download_file(file_id):
Symuluje pobieranie przez time.sleep(random.uniform(0.5, 2.0))
Wypisuje: "Downloaded file {file_id}"
Wariant A (sekwencyjny): Pobierz 10 plików jeden po drugim
Wariant B (równoległy): 10 wątków pobiera równocześnie
Zmierz i wypisz czasy: time.time() przed i po
Przykładowy output:

=== Sequential Download ===
Downloaded file 0
Downloaded file 1
...
Downloaded file 9
Sequential time: 12.34 seconds

=== Parallel Download ===
Downloaded file 0
Downloaded file 3
Downloaded file 1  ← Losowa kolejność!
...
Downloaded file 9
Parallel time: 1.87 seconds

Speedup: 6.60x
Wskazówka:
Sequential: pętla for wywołująca download_file().
Parallel: lista wątków, wszystkie .start(), potem wszystkie .join().

Kod startowy:

import threading
import time
import random

def download_file(file_id):
    # TODO: sleep(random), wypisz info
    pass

# === SEQUENTIAL ===
start = time.time()
# TODO: Pętla for wywołująca download_file(i)
end = time.time()
seq_time = end - start
print(f"Sequential time: {seq_time:.2f} seconds\n")

# === PARALLEL ===
start = time.time()
# TODO: Stwórz listę 10 wątków
# TODO: Uruchom wszystkie
# TODO: join() wszystkich
end = time.time()
par_time = end - start
print(f"Parallel time: {par_time:.2f} seconds")

# TODO: Policz i wypisz speedup
CZĘŚĆ 2: RACE CONDITIONS I SYNCHRONIZACJA (5 pkt)
Zadanie 2.1: "Bank Account Chaos" (2 pkt)
Opis:
Problem z wykładu Prof. Nawrockiego - konto bankowe bez synchronizacji.

Wymagania:

Zmienna globalna balance = 1000 (PLN)
Funkcja deposit(amount) dodaje do balance
Uruchom 200 wątków:
100 wątków: deposit(10)
100 wątków: deposit(20)
Wypisz końcowe balance
URUCHOM 5 RAZY - zauważ różne wyniki!
Oczekiwany wynik (teoretyczny):

1000 + (100*10) + (100*20) = 1000 + 1000 + 2000 = 4000 PLN
Rzeczywisty wynik (bez mutexa):

Run 1: 3642 PLN ❌
Run 2: 3789 PLN ❌
Run 3: 3521 PLN ❌
Run 4: 3856 PLN ❌
Run 5: 3697 PLN ❌
Zadanie:
Zaimplementuj i UDOKUMENTUJ problem w komentarzach:

Dlaczego wynik jest losowy?
Co się dzieje na poziomie READ-ADD-WRITE?
Kod startowy:

import threading

balance = 1000

def deposit(amount):
    """Funkcja dodająca do balance - BEZ synchronizacji!"""
    global balance
    # TODO: Rozłóż operację na 3 kroki (bardziej widoczne)
    # temp = balance      # READ
    # temp += amount      # ADD  
    # balance = temp      # WRITE
    # ← Tutaj inne wątki mogą "wejść" między te linie!
    pass

# Zwiększony stress test dla lepszej widoczności race condition
threads = []

# TODO: 100 wątków deposit(10)
# TODO: 100 wątków deposit(20)
# TODO: join() wszystkich

print(f"Final balance: {balance} PLN")
print(f"Expected: 4000 PLN")

# TODO: Uruchom 5 razy, pokaż różne wyniki w komentarzu:
# Run 1: ??? PLN
# Run 2: ??? PLN
# Run 3: ??? PLN
# Run 4: ??? PLN
# Run 5: ??? PLN
Zadanie 2.2: "Fix It with Mutex" (3 pkt)
Opis:
Napraw zadanie 2.1 używając threading.Semaphore().

Wymagania:

Skopiuj kod z 2.1
Dodaj mutex = threading.Semaphore(1)
W deposit(): użyj mutex.acquire() i mutex.release()
Uruchom ponownie - ZAWSZE powinno być 4000 PLN
Przykładowy output:

Final balance: 4000 PLN ✅
Expected: 4000 PLN

Run 1: 4000 PLN ✅
Run 2: 4000 PLN ✅
Run 3: 4000 PLN ✅
Wyjaśnienie w komentarzach:

Jak mutex rozwiązał problem?
Co się stanie jeśli zapomnisz .release()? (deadlock!)
Kod startowy:

import threading

balance = 1000
mutex = threading.Semaphore(1)  # Binary semaphore

def deposit(amount):
    global balance
    # TODO: mutex.acquire()
    # TODO: temp = balance
    # TODO: temp += amount
    # TODO: balance = temp
    # TODO: mutex.release()
    pass

# (reszta kodu jak w 2.1 - 100+100 wątków)
CZĘŚĆ 3: ZASTOSOWANIA W CYBERSECURITY (10 pkt - ROZSZERZONE)
Zadanie 3.1: "Multi-threaded Password Cracker" (5 pkt) ⭐
Opis:
Mini-wersja Hashcat - łamanie hasła MD5 z użyciem słownika.

Wymagania:

Hash do złamania: 5f4dcc3b5aa765d61d8327deb882cf99 (to jest MD5 z "password")
Słownik: 100 najpopularniejszych haseł (lista w kodzie poniżej)
Wariant A (sekwencyjny): Sprawdź wszystkie hasła po kolei
Wariant B (równoległy): Podziel słownik na 4 części, 4 wątki
Każdy wątek:
Hashuje hasła z swojej części (hashlib.md5)
Porównuje z target hash
Jeśli znalazł - wypisuje i kończy
Zmierz czasy obu wariantów
Przykładowy output:

=== Sequential Cracking ===
Checking password 1/100...
Checking password 2/100...
...
✅ PASSWORD FOUND: password
Sequential time: 0.023 seconds

=== Parallel Cracking (4 threads) ===
Thread-0 checking 0-24
Thread-1 checking 25-49
Thread-2 checking 50-74
Thread-3 checking 75-99
✅ PASSWORD FOUND: password (by Thread-0)
Parallel time: 0.008 seconds

Speedup: 2.88x
Słownik (top 100 passwords):

passwords = [
    "password", "123456", "123456789", "12345678", "12345",
    "qwerty", "abc123", "monkey", "1234567", "letmein",
    "trustno1", "dragon", "baseball", "111111", "iloveyou",
    "master", "sunshine", "ashley", "bailey", "passw0rd",
    "shadow", "123123", "654321", "superman", "qazwsx",
    # ... (dodaj więcej lub użyj tych 25)
]
Wskazówki:

import hashlib
hashlib.md5(password.encode()).hexdigest() → zwraca hash jako string
Podziel listę: passwords[0:25], passwords[25:50], etc.
Użyj threading.Thread(target=crack_part, args=(start, end, target))
Kod startowy:

import threading
import hashlib
import time

target_hash = "5f4dcc3b5aa765d61d8327deb882cf99"  # MD5("password")
passwords = ["password", "123456", ...]  # Top 100

def crack_sequential(target):
    # TODO: Loop przez passwords, hashuj, porównaj
    pass

def crack_part(start, end, target, thread_id):
    # TODO: Loop przez passwords[start:end]
    # Jeśli znalazł - wypisz
    pass

# === SEQUENTIAL ===
start = time.time()
crack_sequential(target_hash)
seq_time = time.time() - start
print(f"Sequential time: {seq_time:.4f}s\n")

# === PARALLEL ===
start = time.time()
# TODO: 4 wątki, każdy z częścią słownika
par_time = time.time() - start
print(f"Parallel time: {par_time:.4f}s")
print(f"Speedup: {seq_time/par_time:.2f}x")
Zadanie 3.2: "Parallel Port Scanner" (5 pkt) ⭐
Opis:
Mini-wersja Nmap - skanowanie portów na localhost.

Wymagania:

Skanuj porty 1-1000 na 127.0.0.1 (localhost)
Wariant A (sekwencyjny): Sprawdzaj porty po kolei
Wariant B (równoległy): 50 wątków skanujących równocześnie
Dla każdego portu:
Spróbuj połączyć socket.socket().connect(('127.0.0.1', port))
Timeout: 0.5 sekundy
Jeśli się udało → port OPEN
Jeśli ConnectionRefusedError → port CLOSED
Wypisz tylko OTWARTE porty
Zmierz czasy
⚠️ LEGALNOŚĆ: Tylko localhost! Skanowanie innych IP bez zgody = NIELEGALNE!

Przykładowy output:

=== Sequential Scan ===
Scanning ports 1-1000 on 127.0.0.1...
Open ports: [22, 80, 443, 3306, 8080]
Sequential time: 487.23 seconds (8 minut!)

=== Parallel Scan (50 threads) ===
Scanning ports 1-1000 on 127.0.0.1...
Open ports: [22, 80, 443, 3306, 8080]
Parallel time: 12.45 seconds
Speedup: 39.13x 🚀
Wskazówki:

import socket
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
.settimeout(0.5) - ważne, inaczej czekasz 60s na każdy port!
.connect(('127.0.0.1', port)) - jeśli sukces = OPEN
Użyj try-except - ConnectionRefusedError, socket.timeout
Dla parallel: podziel 1-1000 na 50 części (~20 portów/wątek)
Kod startowy:

import socket
import threading
import time

def scan_port(host, port):
    """Sprawdź czy port jest otwarty"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect((host, port))
        sock.close()
        return True  # Port OPEN
    except (ConnectionRefusedError, socket.timeout):
        return False  # Port CLOSED

def scan_sequential(host, start_port, end_port):
    # TODO: Loop 1-1000, sprawdź każdy port
    open_ports = []
    # ...
    return open_ports

def scan_range(host, start_port, end_port, results, thread_id):
    # TODO: Skanuj zakres portów, dodaj otwarte do results (lista współdzielona!)
    # UWAGA: Potrzebujesz mutexa dla results.append()!
    pass

# === SEQUENTIAL ===
print("=== Sequential Scan ===")
start = time.time()
open_ports = scan_sequential('127.0.0.1', 1, 1000)
seq_time = time.time() - start
print(f"Open ports: {open_ports}")
print(f"Time: {seq_time:.2f}s\n")

# === PARALLEL ===
print("=== Parallel Scan (50 threads) ===")
results = []  # Współdzielona lista
mutex = threading.Semaphore(1)
start = time.time()
# TODO: 50 wątków, każdy skanuje ~20 portów
par_time = time.time() - start
print(f"Open ports: {sorted(results)}")
print(f"Time: {par_time:.2f}s")
print(f"Speedup: {seq_time/par_time:.2f}x")
UWAGA:
Współdzielona lista results → potrzebujesz mutex przy .append()!
Inaczej race condition.

CZĘŚĆ 4: BONUSY (5 pkt - OPCJONALNE)
Zadanie 4.1: "Deadlock Demonstration" (3 pkt)
Opis:
Stwórz program który celowo wpada w deadlock, potem go napraw.

Wymagania:

Dwie zmienne globalne: X = 0, Y = 0
Dwa mutexy: mutexX, mutexY
Funkcja funcA():
Zajmuje mutexX
Sleep 0.1s
Zajmuje mutexY
X += 1, Y += 1
Zwalnia oba
Funkcja funcB():
Zajmuje mutexY
Sleep 0.1s
Zajmuje mutexX
X *= 2, Y *= 2
Zwalnia oba
Uruchom 2 wątki (A i B) → DEADLOCK!
Napraw: Resource ordering (obydwie funkcje: najpierw X, potem Y)
Przykładowy output (przed fix):

Thread A: Acquired mutexX
Thread B: Acquired mutexY
Thread A: Waiting for mutexY... 💀
Thread B: Waiting for mutexX... 💀
(program zawiesza się na zawsze)
Po fix:

Thread A: Acquired mutexX
Thread A: Acquired mutexY
Thread A: Done
Thread B: Acquired mutexX
Thread B: Acquired mutexY
Thread B: Done
Final X=2, Y=2 ✅
Wyjaśnienie w komentarzach:

Dlaczego nastąpił deadlock?
Jak resource ordering to rozwiązał?
Warunki Coffmana (które zostały spełnione?)
Zadanie 4.2: "Speedup Analysis" (2 pkt)
Opis:
Zmierz speedup dla różnej liczby wątków w zadaniu 3.1 lub 3.2.

Wymagania:

Wybierz zadanie 3.1 lub 3.2
Uruchom z N = 1, 2, 4, 8, 16, 32 wątkami
Zmierz czas dla każdego N
Policz speedup: S = T_sequential / T_parallel
Wypisz tabelę wyników
Analiza: Czy speedup jest liniowy? Dlaczego nie?
Przykładowy output:

Password Cracker - Speedup Analysis
Słownik: 1000 haseł

N threads | Time (s) | Speedup | Efficiency
----------|----------|---------|------------
    1     |  0.245   |  1.00x  |   100%
    2     |  0.134   |  1.83x  |   91%
    4     |  0.078   |  3.14x  |   79%
    8     |  0.052   |  4.71x  |   59%
   16     |  0.048   |  5.10x  |   32%
   32     |  0.047   |  5.21x  |   16%

Analiza:
- Speedup nie jest liniowy (4 wątki ≠ 4x)
- Po 8 wątkach: diminishing returns
- Overhead (tworzenie wątków, synchronizacja) zjada zysk
- GIL limitation (Python może wykonywać tylko 1 wątek naraz)
Wskazówki:

Efficiency = Speedup / N * 100%
Prawo Amdahla: teoretyczny limit speedup
Użyj większego słownika (1000-10000 haseł) dla lepszej mierzalności
💭 WSKAZÓWKI (na końcu pliku)
Kliknij aby rozwinąć wskazówki
Threading basics:
Problem: Program kończy się przed wątkami.

# ❌ ŹLE - bez join()
thread.start()
print("Done")  # To się wykona PRZED thread!

# ✅ DOBRZE - z join()
thread.start()
thread.join()  # Czekaj aż thread skończy
print("Done")  # Teraz to się wykona PO thread
Problem: Wątki nie działają równolegle.

# ❌ ŹLE - .run() wykonuje synchronicznie
thread.run()  # To jest jak zwykłe wywołanie funkcji!

# ✅ DOBRZE - .start() uruchamia równolegle
thread.start()
Race conditions:
Problem: counter ma losową wartość.

# ❌ ŹLE - brak synchronizacji
def increment():
    global counter
    counter += 1  # To NIE jest atomowe!

# ✅ DOBRZE - z mutexem
mutex = threading.Semaphore(1)
def increment():
    global counter
    mutex.acquire()
    counter += 1  # Teraz tylko 1 wątek naraz
    mutex.release()
Czemu counter += 1 nie jest atomowe?

# CPU wykonuje to jako:
temp = counter      # READ
temp = temp + 1     # ADD
counter = temp      # WRITE
# Inne wątki mogą "wejść" między te linie!
Zwiększanie widoczności race condition:

# Rozłóż operację na 3 linie (bardziej widoczne)
def deposit(amount):
    global balance
    temp = balance      # READ
    temp += amount      # ADD
    balance = temp      # WRITE
    # ← Tutaj następuje interleaving!
Mutex patterns:
Pattern 1: Prosty mutex

mutex.acquire()
try:
    # Sekcja krytyczna
    shared_variable += 1
finally:
    mutex.release()  # ZAWSZE zwolnij, nawet jeśli błąd!
Pattern 2: Współdzielona lista

results = []
mutex = threading.Semaphore(1)

def worker(data):
    result = process(data)
    mutex.acquire()
    results.append(result)  # Lista jest shared!
    mutex.release()
Socket programming (Zadanie 3.2):
Podstawy:

import socket

# Stwórz socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(0.5)  # WAŻNE! Inaczej czeka 60s

# Spróbuj połączyć
try:
    sock.connect(('127.0.0.1', port))
    print(f"Port {port} OPEN")
    sock.close()
except ConnectionRefusedError:
    print(f"Port {port} CLOSED")
except socket.timeout:
    print(f"Port {port} TIMEOUT")
Dlaczego timeout jest ważny?

Bez timeout: każdy zamknięty port = 60 sekund czekania!
1000 portów × 60s = 16 godzin! 😱
Z timeout 0.5s: 1000 portów × 0.5s = 8 minut (sekwencyjnie)
Hashowanie (Zadanie 3.1):
import hashlib

password = "test123"
hash_md5 = hashlib.md5(password.encode()).hexdigest()
print(hash_md5)  # cc03e747a6afbbcbf8be7668acfebee5

# Porównanie
if hash_md5 == target_hash:
    print("PASSWORD FOUND!")
Dlaczego .encode()?

MD5 potrzebuje bytes, nie string
"password" → b"password"
Dzielenie listy na części:
passwords = ["a", "b", "c", "d", "e", "f", "g", "h"]
n_threads = 4
chunk_size = len(passwords) // n_threads  # 8 // 4 = 2

# Thread 0: passwords[0:2]   = ["a", "b"]
# Thread 1: passwords[2:4]   = ["c", "d"]
# Thread 2: passwords[4:6]   = ["e", "f"]
# Thread 3: passwords[6:8]   = ["g", "h"]

threads = []
for i in range(n_threads):
    start = i * chunk_size
    end = start + chunk_size
    t = threading.Thread(target=crack, args=(start, end))
    threads.append(t)
    t.start()
Timing:
import time

start = time.time()
# ... kod do zmierzenia ...
end = time.time()

elapsed = end - start
print(f"Time: {elapsed:.2f} seconds")
Debugging tips:
Problem: Program zawiesza się.

Sprawdź czy wszystkie .acquire() mają .release()
Sprawdź czy nie ma circular wait (deadlock)
Dodaj print() przed/po acquire/release aby zobaczyć flow
Problem: Wyniki są dziwne.

Sprawdź czy używasz global dla zmiennych globalnych
Sprawdź czy współdzielone dane mają mutex
Dodaj print() aby zobaczyć co każdy wątek robi
Problem: Threading nie przyspiesza.

Sprawdź czy zadanie jest I/O-bound (powinno być!)
Sprawdź timeout w socket (za długi = mało speedup)
Spróbuj więcej wątków (np. 50 zamiast 4)
Common errors:
# ❌ Zapomnienie global
def increment():
    counter += 1  # UnboundLocalError!
# ✅
def increment():
    global counter
    counter += 1

# ❌ .run() zamiast .start()
thread.run()  # Synchroniczne!
# ✅
thread.start()  # Asynchroniczne!

# ❌ Brak join()
thread.start()
print(counter)  # Counter jeszcze się nie zmienił!
# ✅
thread.start()
thread.join()
print(counter)  # Teraz jest poprawna wartość

# ❌ Deadlock - czekanie w kółko
mutexA.acquire()
mutexB.acquire()  # Thread B czeka...
# ✅ Resource ordering
# ZAWSZE: mutexA, potem mutexB (w KAŻDEJ funkcji!)
GIL reminder:
# CPU-bound (obliczenia) - threading NIE pomoże!
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)
# 4 wątki = tak samo wolno jak 1 wątek 😢

# I/O-bound (czekanie) - threading DZIAŁA!
def download(url):
    response = requests.get(url)  # Czeka na sieć
    return response.text
# 4 wątki = ~4x szybciej! 🚀
Dzisiejsze zadania = I/O-bound, więc threading będzie działał!

📚 DODATKOWE MATERIAŁY (opcjonalne)
Dokumentacja:
Python threading: https://docs.python.org/3/library/threading.html
Socket programming: https://docs.python.org/3/library/socket.html
Hashlib: https://docs.python.org/3/library/hashlib.html
Artykuły:
"Understanding the GIL": https://realpython.com/python-gil/
"Amdahl's Law": https://en.wikipedia.org/wiki/Amdahl%27s_law
"Deadlock conditions": https://en.wikipedia.org/wiki/Deadlock
Narzędzia:
Hashcat: https://hashcat.net/hashcat/
Nmap: https://nmap.org/
John the Ripper: https://www.openwall.com/john/
❓ PYTANIA?
Jeśli masz pytania:

Podnieś rękę podczas laboratorium
Email: bartekel@gmail.com
Office hours: [prowadzący uzupełni]
🎯 CHECKLIST PRZED ODDANIEM
Wszystkie zadania mają komentarze wyjaśniające
Kod działa (przetestowany!)
Brak błędów składni
Użyto threading.Thread, nie multiprocessing
Zadanie 3.2: skanowanie TYLKO localhost (legalność!)
Plik nazwany: lab10_imie_nazwisko.py
Powodzenia! 🚀

Bartosz Lewandowski
bartekel@gmail.com
Poznan University of Technology