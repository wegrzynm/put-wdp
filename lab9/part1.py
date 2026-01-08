# Lab 9: Rozgrzewka

def zadanie_1():
    print("Zadanie 1: Quick Review")
    print("Dopasuj złożoność do algorytmu:")
    
    mapping = {
        "A) Binary search": "O(log n)",
        "B) Bubble sort": "O(n²)",
        "C) Array access lista[0]": "O(1)",
        "D) Heapsort": "O(n log n)"
    }
    
    for alg, compl in mapping.items():
        print(f"{alg} -> {compl}")
    print("-" * 30)

def zadanie_2():
    print("Zadanie 2: Co jest szybsze?")
    n = 10_000
    comp_a = n**2
    print(f"Dla n = {n}:")
    print(f"Algorytm A: O(n²) = {comp_a:,} operacji")
    print(f"Algorytm B: O(2ⁿ) = 2^{n} (liczba większa niż atomów we wszechświecie)")
    
    poprawna_odp = "D) Algorytm B nigdy się nie skończy w rozsądnym czasie"
    print(f"Poprawna odpowiedź: {poprawna_odp}")
    print("-" * 30)

def zadanie_3():
    print("Zadanie 3: Real-world Impact")
    print("Dlaczego Google używa algorytmów O(n log n) zamiast O(n²)?")
    
    poprawna_odp = "B) Bo dla miliardów rekordów różnica to sekundy vs lata"
    
    print(f"Poprawna odpowiedź: {poprawna_odp}")
    print("-" * 30)

if __name__ == "__main__":
    zadanie_1()
    zadanie_2()
    zadanie_3()
