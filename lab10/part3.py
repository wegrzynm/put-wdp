import threading
import hashlib
import time
import socket

# === Zadanie 3.1: "Multi-threaded Password Cracker" ===
print("=== Zadanie 3.1 ===")

target_hash = "5f4dcc3b5aa765d61d8327deb882cf99"  # MD5("password")
passwords = [
    "password", "123456", "123456789", "12345678", "12345",
    "qwerty", "abc123", "monkey", "1234567", "letmein",
    "trustno1", "dragon", "baseball", "111111", "iloveyou",
    "master", "sunshine", "ashley", "bailey", "passw0rd",
    "shadow", "123123", "654321", "superman", "qazwsx"
] * 4 

def crack_sequential(target):
    for i, pwd in enumerate(passwords):
        h = hashlib.md5(pwd.encode()).hexdigest()
        if h == target:
            print(f"✅ PASSWORD FOUND (Sequential): {pwd}")
            return pwd
    return None

def crack_part(start, end, target, thread_id, found_event, result_container):
    print(f"Thread-{thread_id} checking {start}-{end-1}")
    for i in range(start, end):
        if found_event.is_set():
            return
        pwd = passwords[i]
        h = hashlib.md5(pwd.encode()).hexdigest()
        if h == target:
            print(f"✅ PASSWORD FOUND: {pwd} (by Thread-{thread_id})")
            result_container.append(pwd)
            found_event.set()
            return

# --- Wariant A: Sekwencyjny ---
print("=== Sequential Cracking ===")
start_time = time.time()
crack_sequential(target_hash)
seq_time = time.time() - start_time
print(f"Sequential time: {seq_time:.4f}s\n")

# --- Wariant B: Równoległy ---
print("=== Parallel Cracking (4 threads) ===")
start_time = time.time()
n_threads = 4
chunk_size = len(passwords) // n_threads
threads_3_1 = []
found_event = threading.Event()
result_container = []

for i in range(n_threads):
    start_idx = i * chunk_size
    end_idx = start_idx + chunk_size if i < n_threads - 1 else len(passwords)
    t = threading.Thread(target=crack_part, args=(start_idx, end_idx, target_hash, i, found_event, result_container))
    threads_3_1.append(t)
    t.start()

for t in threads_3_1:
    t.join()

par_time = time.time() - start_time
print(f"Parallel time: {par_time:.4f}s")
if seq_time > 0 and par_time > 0:
    print(f"Speedup: {seq_time/par_time:.2f}x\n")


# === Zadanie 3.2: "Parallel Port Scanner" ===
print("=== Zadanie 3.2 ===")

def scan_port(host, port):
    """Sprawdź czy port jest otwarty"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception:
        return False

def scan_sequential(host, start_port, end_port):
    print(f"Scanning ports {start_port}-{end_port} on {host}...")
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            open_ports.append(port)
    return open_ports

def scan_range(host, start_port, end_port, results, mutex, thread_id):
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            mutex.acquire()
            results.append(port)
            mutex.release()

host = '127.0.0.1'

# --- Wariant A: Sekwencyjny ---
print("=== Sequential Scan ===")
start_time = time.time()
open_ports_seq = scan_sequential(host, 1, 100)
seq_time_scan = time.time() - start_time
print(f"Open ports (Partial 1-100): {open_ports_seq}")
print(f"Sequential time (1-100): {seq_time_scan:.2f}s\n")

# Estymacja dla 1-1000
est_seq_time = seq_time_scan * 10 

# --- Wariant B: Równoległy ---
print("=== Parallel Scan (50 threads) ===")
results_scan = []
mutex_scan = threading.Semaphore(1)
start_time = time.time()

num_threads = 50
ports_to_scan = 1000
chunk_size = ports_to_scan // num_threads

threads_3_2 = []
for i in range(num_threads):
    start_p = i * chunk_size + 1
    end_p = (i + 1) * chunk_size if i < num_threads - 1 else ports_to_scan
    t = threading.Thread(target=scan_range, args=(host, start_p, end_p, results_scan, mutex_scan, i))
    threads_3_2.append(t)
    t.start()

for t in threads_3_2:
    t.join()

par_time_scan = time.time() - start_time
print(f"Open ports (1-1000): {sorted(results_scan)}")
print(f"Parallel time: {par_time_scan:.2f}s")
print(f"Speedup vs Estimated Sequential: {est_seq_time/par_time_scan:.2f}x")
