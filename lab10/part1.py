import threading
import time
import random

# === Zadanie 1.1: "Hello from Threads" ===
print("=== Zadanie 1.1 ===")

def worker(thread_id):
    """Funkcja wypisująca ID wątku i aktualny timestamp."""
    timestamp = time.strftime("%H:%M:%S")
    print(f"Thread-{thread_id}: {timestamp}")

threads_1_1 = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads_1_1.append(t)
    t.start()

for t in threads_1_1:
    t.join()

print("All threads finished\n")


# === Zadanie 1.2: "Speedup Demo" ===
print("=== Zadanie 1.2 ===")

def download_file(file_id):
    """Symulacja pobierania pliku."""
    wait_time = random.uniform(0.5, 2.0)
    time.sleep(wait_time)
    print(f"Downloaded file {file_id}")

# --- Wariant A: Sekwencyjny ---
print("=== Sequential Download ===")
start_seq = time.time()
for i in range(10):
    download_file(i)
end_seq = time.time()
seq_time = end_seq - start_seq
print(f"Sequential time: {seq_time:.2f} seconds\n")

# --- Wariant B: Równoległy ---
print("=== Parallel Download ===")
start_par = time.time()
threads_1_2 = []
for i in range(10):
    t = threading.Thread(target=download_file, args=(i,))
    threads_1_2.append(t)
    t.start()

for t in threads_1_2:
    t.join()

end_par = time.time()
par_time = end_par - start_par
print(f"Parallel time: {par_time:.2f} seconds\n")

# Speedup
speedup = seq_time / par_time
print(f"Speedup: {speedup:.2f}x")
