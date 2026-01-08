import time
import random

# Laboratorium 8: Złożoność obliczeniowa
# Cześć 2: Zadania podstawowe

# Zadanie 4: Rozpoznaj złożoność
def task_4_answers():
    """
    Kod A (find_max): O(n)
    Kod B (bubble_sort): O(n²)
    Kod C (binary_search): O(log n)
    """
    print("Zadanie 4: Rozpoznawanie złożoności")
    print("Kod A (find_max) -> O(n)")
    print("Kod B (bubble_sort) -> O(n²)")
    print("Kod C (binary_search) -> O(log n)")

# Zadanie 5: Selection Sort - zliczanie porównań
def selection_sort_count_comparisons(lista):
    n = len(lista)
    comparisons = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparisons += 1
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return comparisons

# Zadanie 6: Heap vs Selection Sort
def task_6_table():
    """
    Dla n = 10,000:
    Selection Sort (n²/2) = 10,000² / 2 = 50,000,000
    Heapsort (2n log2(n)) = 2 * 10,000 * log2(10,000) ≈ 2 * 10,000 * 13.29 ≈ 265,754
    """
    import math
    n = 10000
    sel_sort_ops = (n**2) // 2
    heap_sort_ops = int(2 * n * math.log2(n))
    
    print("\nZadanie 6: Porównanie liczby operacji dla n=10,000")
    print(f"Selection Sort: ~{sel_sort_ops:,}")
    print(f"Heapsort:      ~{heap_sort_ops:,}")

# Zadanie 7: Praktyczny pomiar czasu
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

def measure_time():
    n = 1000
    test_list = [random.randint(1, 10000) for _ in range(n)]
    
    # Kopia listy dla drugiego sortowania
    list_for_selection = test_list.copy()
    list_for_sorted = test_list.copy()
    
    print(f"\nZadanie 7: Pomiar czasu dla n={n}")
    
    # Pomiar Selection Sort
    start = time.time()
    selection_sort(list_for_selection)
    end = time.time()
    print(f"Selection Sort: {end - start:.6f} sekund")
    
    # Pomiar wbudowanego sorted()
    start = time.time()
    _ = sorted(list_for_sorted)
    end = time.time()
    print(f"Wbudowane sorted(): {end - start:.6f} sekund")

# Zadanie 8: Big O - definicja
def task_8_explanation():
    """
    Która z funkcji jest O(n²)? 
    Odpowiedź: A) f(n) = 5n² + 3n + 100
    
    Dlaczego w Big O pomijamy stałe współczynniki i niższe rzędy?
    Bo interesuje nas tempo wzrostu przy n dążącym do nieskończoności.
    Dla bardzo dużych n, składnik n² rośnie znacznie szybciej niż n czy stała 100,
    więc to on dominuje i wyznacza trend wzrostu.
    """
    print("\nZadanie 8: Big O")
    print("Funkcja O(n²) to: f(n) = 5n² + 3n + 100")

# Wywołanie przykładów
if __name__ == "__main__":
    task_4_answers()
    
    n_5 = [5, 4, 3, 2, 1]
    comps = selection_sort_count_comparisons(n_5.copy())
    print(f"\nZadanie 5: Porównania dla n=5: {comps}")
    
    task_6_table()
    measure_time()
    task_8_explanation()
