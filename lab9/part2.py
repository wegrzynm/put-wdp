# Lab 9: Zadania podstawowe

def zadanie_4():
    print("Zadanie 4: Knapsack Problem - Wprowadzenie")
    capacity = 10
    items = {
        'A': {'weight': 2, 'value': 3},
        'B': {'weight': 3, 'value': 5},
        'C': {'weight': 5, 'value': 9},
        'D': {'weight': 7, 'value': 14}
    }
    
    # Options check
    options = {
        'a': (['A', 'B', 'C'], 10, 17),
        'b': (['B', 'D'], 10, 19),
        'c': (['A', 'C'], 7, 12),
        'd': (['D'], 7, 14)
    }
    
    print(f"Pojemność: {capacity}kg")
    for opt, (names, weight, value) in options.items():
        print(f"{opt}) {names} (waga {weight}kg, wartość ${value})")
    
    print("\nPoprawna odpowiedź: b) B + D ($19)")
    print(f"Pytanie dodatkowe: Ile jest możliwych kombinacji dla 4 przedmiotów? 2^4 = {2**4}")
    print("-" * 30)

def zadanie_5():
    print("Zadanie 5: Brute Force Explosion")
    
    # 2^20
    combinations_20 = 2**20
    
    # 2^30
    combinations_30 = 2**30

    print(f"Dla 20 przedmiotów: 2^20 = {combinations_20:,} kombinacji")
    
    print(f"\nDla 30 przedmiotów: 2^30 = {combinations_30:,} kombinacji")
    
    print("\nCzy dla 30 przedmiotów brute force jest realistyczny? Tak, ale dla 50 (2^50 ≈ 10^15) już nie.")
    print("-" * 30)

def zadanie_6():
    print("Zadanie 6: P vs NP - Quiz")
    
    p_problems = ["A) Sortowanie listy liczb", "B) Najkrótsza ścieżka w grafie (Dijkstra)", "D) Sprawdzenie czy liczba jest pierwsza (AKS test)"]
    np_complete_problems = ["C) Traveling Salesman Problem (TSP)", "E) Knapsack Problem", "F) Boolean Satisfiability (SAT)"]
    
    print("Kategoria P (Polynomial):")
    for p in p_problems: 
        print(f"  - {p}")
    
    print("\nKategoria NP-complete:")
    for np in np_complete_problems: 
        print(f"  - {np}")
    print("-" * 30)

def zadanie_7():
    print("Zadanie 7: Verifier vs Solver")
    
    table = [
        ["Problem", "Solving", "Verifying"],
        ["Sortowanie", "Łatwy (O(n log n))", "O(n)"],
        ["Sudoku 9x9", "Trudny (NP-complete)", "O(1) lub O(n²) dla NxN"],
        ["TSP (100 miast)", "Bardzo Trudny", "O(n)"],
        ["Liczba pierwsza", "Łatwy (P)", "Łatwy (zależy od dowodu)"]
    ]
    
    for row in table:
        print(f"{row[0]:<20} | {row[1]:<20} | {row[2]}")
    print("-" * 30)

def zadanie_8():
    print("Zadanie 8: Problem Reduction")
    print("Które redukcje są poprawne?")
    
    reductions = {
        "a) Sortowanie → Binary search": "Nie (na odwrót)",
        "b) Knapsack → Partition problem": "Tak (Partition to szczególny przypadek Knapsack)",
        "c) Password cracking → SAT problem": "Tak (każdy NP problem redukuje się do SAT - Tw. Cooka)",
        "d) Sudoku → Graph coloring": "Tak (Sudoku można przedstawić jako kolorowanie grafu)"
    }
    
    for red, status in reductions.items():
        print(f"{red}: {status}")
    print("-" * 30)

if __name__ == "__main__":
    zadanie_4()
    zadanie_5()
    zadanie_6()
    zadanie_7()
    zadanie_8()
