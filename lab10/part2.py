import threading
import time

# === Zadanie 2.1: "Bank Account Chaos" ===
print("=== Zadanie 2.1 ===")

balance = 1000

def deposit_no_sync(amount):
    """Funkcja dodająca do balance - BEZ synchronizacji!"""
    global balance
    temp = balance      # READ
    time.sleep(0.0001)  # Małe opóźnienie wymuszające przełączenie kontekstu
    temp += amount      # ADD  
    balance = temp      # WRITE

def run_simulation():
    global balance
    balance = 1000
    threads = []
    
    # 100 wątków deposit(10)
    for _ in range(100):
        t = threading.Thread(target=deposit_no_sync, args=(10,))
        threads.append(t)
        t.start()
        
    # 100 wątków deposit(20)
    for _ in range(100):
        t = threading.Thread(target=deposit_no_sync, args=(20,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
    
    return balance

print("Running simulation 5 times (No Synchronization):")
results = []
for i in range(1, 6):
    final_balance = run_simulation()
    results.append(final_balance)
    print(f"Run {i}: {final_balance} PLN")

print(f"Expected: 4000 PLN")

"""
DOKUMENTACJA PROBLEMU:
Dlaczego wynik jest losowy?
Wynik jest losowy z powodu zjawiska 'race condition' (wyścigu). Operacja 'balance += amount' 
nie jest atomowa. Składa się z odczytu (READ), dodawania (ADD) i zapisu (WRITE).

Co się dzieje na poziomie READ-ADD-WRITE?
Gdy wiele wątków wykonuje te kroki jednocześnie:
1. Wątek A odczytuje saldo (np. 1000).
2. Zanim Wątek A zapisze wynik, Wątek B również odczytuje saldo (nadal 1000).
3. Wątek A dodaje 10 i zapisuje 1010.
4. Wątek B dodaje 20 do swojej lokalnej kopii (1000) i zapisuje 1020.
Wynik zapisu Wątku A zostaje nadpisany przez Wątek B (lub na odwrót), 
przez co jedna z operacji "ginie".
"""

# === Zadanie 2.2: "Fix It with Mutex" ===
print("\n=== Zadanie 2.2 ===")

balance_sync = 1000
mutex = threading.Semaphore(1)

def deposit_sync(amount):
    """Funkcja dodająca do balance - Z SYNCHRONIZACJĄ!"""
    global balance_sync
    
    mutex.acquire()
    try:
        temp = balance_sync
        temp += amount
        balance_sync = temp
    finally:
        mutex.release()

def run_simulation_sync():
    global balance_sync
    balance_sync = 1000
    threads = []
    
    for _ in range(100):
        t = threading.Thread(target=deposit_sync, args=(10,))
        threads.append(t)
        t.start()
        
    for _ in range(100):
        t = threading.Thread(target=deposit_sync, args=(20,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
    
    return balance_sync

print("Running simulation 3 times (With Mutex):")
for i in range(1, 4):
    final_balance = run_simulation_sync()
    print(f"Run {i}: {final_balance} PLN ✅")

"""
WYJAŚNIENIE:
Jak mutex rozwiązał problem?
Mutex działa jak klucz do pokoju (sekcji krytycznej). Tylko jeden wątek może 
posiadać ten klucz (wykonać 'acquire()') naraz. Inne wątki muszą czekać, 
aż klucz zostanie zwrócony ('release()'). Dzięki temu operacja odczyt-dodaj-zapis 
jest wykonywana nieprzerwanie przez jeden wątek.

Co się stanie jeśli zapomnisz .release()?
Wszystkie pozostałe wątki będą w nieskończoność czekać na możliwość wejścia do sekcji krytycznej, 
a program przestanie reagować.
"""
