import threading
import time
import hashlib

# === Zadanie 4.1: "Deadlock Demonstration" ===
print("=== Zadanie 4.1 ===")

X = 0
Y = 0
mutexX = threading.Semaphore(1)
mutexY = threading.Semaphore(1)

def funcA_deadlock():
    global X, Y
    print("Thread A: Trying to acquire mutexX")
    mutexX.acquire()
    print("Thread A: Acquired mutexX")
    time.sleep(0.1)
    print("Thread A: Waiting for mutexY... 💀")
    mutexY.acquire()
    X += 1
    Y += 1
    mutexY.release()
    mutexX.release()
    print("Thread A: Done")

def funcB_deadlock():
    global X, Y
    print("Thread B: Trying to acquire mutexY")
    mutexY.acquire()
    print("Thread B: Acquired mutexY")
    time.sleep(0.1)
    print("Thread B: Waiting for mutexX... 💀")
    mutexX.acquire()
    X *= 2
    Y *= 2
    mutexX.release()
    mutexY.release()
    print("Thread B: Done")

def funcA_fixed():
    global X, Y
    mutexX.acquire()
    time.sleep(0.1)
    mutexY.acquire()
    X += 1
    Y += 1
    mutexY.release()
    mutexX.release()
    print("Thread A: Done (Fixed)")

def funcB_fixed():
    global X, Y
    mutexX.acquire()
    time.sleep(0.1)
    mutexY.acquire()
    X *= 2
    Y *= 2
    mutexY.release()
    mutexX.release()
    print("Thread B: Done (Fixed)")

print("Runnning fixed version to avoid hanging the script:")
t1 = threading.Thread(target=funcA_fixed)
t2 = threading.Thread(target=funcB_fixed)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Final X={X}, Y={Y} ✅")

"""
DOKUMENTACJA DEADLOCKA:
Dlaczego nastąpił deadlock?
Deadlock wystąpił z powodu 'circular wait' (cyklicznego oczekiwania). Wątek A zajął zasób X 
i czekał na Y. Jednocześnie Wątek B zajął zasób Y i czekał na X. Żaden wątek nie mógł ruszyć dalej.

Jak resource ordering to rozwiązał?
Wprowadzenie stałej kolejności blokowania (zawsze X przed Y) sprawia, że drugi wątek 
nie może zająć zasobu Y, dopóki nie uzyska dostępu do X. Jeśli Wątek A zajął X, 
Wątek B będzie czekał już na etapie próby zajęcia X, nie zajmując w tym czasie Y.

Warunki Coffmana (które zostały spełnione przy deadlocku):
1. Mutual Exclusion (wzajemne wykluczanie - tylko jeden wątek naraz ma dostęp do mutexa).
2. Hold and Wait (trzymanie zasobu i oczekiwanie na inny).
3. No Preemption (brak wywłaszczania - zasoby nie mogą być odebrane siłą).
4. Circular Wait (cykliczne oczekiwanie).
"""

# === Zadanie 4.2: "Speedup Analysis" ===
print("\n=== Zadanie 4.2 ===")

def speedup_analysis():
    target = hashlib.md5("secret".encode()).hexdigest()
    large_passwords = [f"pass{i}" for i in range(10000)]
    large_passwords[9999] = "secret"
    
    def crack(pswd_list, target_h):
        for p in pswd_list:
            if hashlib.md5(p.encode()).hexdigest() == target_h:
                return True
        return False

    def crack_thread(start, end, pswd_list, target_h, event):
        for i in range(start, end):
            if event.is_set(): return
            if hashlib.md5(pswd_list[i].encode()).hexdigest() == target_h:
                event.set()
                return

    # T_sequential
    start_t = time.time()
    crack(large_passwords, target)
    t_seq = time.time() - start_t
    
    print(f"Password Cracker - Speedup Analysis")
    print(f"Słownik: {len(large_passwords)} haseł\n")
    print(f"{'N threads':<10} | {'Time (s)':<10} | {'Speedup':<10} | {'Efficiency':<10}")
    print("-" * 50)
    
    n_list = [1, 2, 4, 8, 16, 32]
    for n in n_list:
        start_t = time.time()
        chunk = len(large_passwords) // n
        threads = []
        ev = threading.Event()
        for i in range(n):
            s = i * chunk
            e = (i + 1) * chunk if i < n - 1 else len(large_passwords)
            t = threading.Thread(target=crack_thread, args=(s, e, large_passwords, target, ev))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        t_par = time.time() - start_t
        
        speedup = t_seq / t_par
        efficiency = (speedup / n) * 100
        print(f"{n:<10} | {t_par:<10.4f} | {speedup:<10.2f}x | {efficiency:<10.1f}%")

    print("\nAnaliza:")
    print("- Speedup nie jest liniowy z powodu GIL (Global Interpreter Lock) w Pythonie.")
    print("- Operacje hashlib.md5 uwalniają GIL (wykonywane w C), dlatego widać pewien zysk.")
    print("- Tworzenie zbyt dużej liczby wątków wprowadza narzut (overhead) związany z przełączaniem kontekstu.")

speedup_analysis()
