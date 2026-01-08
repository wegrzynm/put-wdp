# Lab 9: Zadania rozszerzone

def zadanie_9_knapsack_dp():
    print("Zadanie 9: Knapsack - Dynamic Programming")
    # Capacity C=7
    # A: weight 3, value 5
    # B: weight 4, value 6
    # C: weight 2, value 3
    
    capacity = 7
    items = [
        ("A", 3, 5),
        ("B", 4, 6),
        ("C", 2, 3)
    ]
    
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name, weight, value = items[i-1]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(value + dp[i-1][w-weight], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
                
    print(f"Maksymalna wartość dla C={capacity} to: {dp[n][capacity]}")
    
    # Traceback to find items
    w = capacity
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            name, weight, value = items[i-1]
            selected.append(name)
            w -= weight
            
    print(f"Wybrane przedmioty: {selected}")
    print("Złożoność: O(n*C)")
    print("-" * 30)

def zadanie_10_halting_problem():
    print("Zadanie 10: Halting Problem - Proof by Contradiction")
    print("Analiza logiczna dowodu Turinga:")
    print("1. Zakładamy, że istnieje funkcja WillHalt(program, input) -> bool.")
    print("2. Tworzymy przekorny program 'prog' (jak w treści zadania).")
    print("3. Jeśli WillHalt(prog) mówi 'zatrzyma się', prog wchodzi w nieskończoną pętlę.")
    print("4. Jeśli WillHalt(prog) mówi 'nie zatrzyma się', prog kończy działanie.")
    print("\nWniosek: WillHalt zawsze się myli dla takiego programu, więc nie może istnieć!")
    
    print("\nOdpowiedzi na pytania:")
    print("- Dlaczego dowód działa przez sprzeczność? Bo wykazuje, że założenie o istnieniu WillHalt prowadzi do logicznego absurdu (1=0).")
    print("- Co to oznacza dla automatic code analysis? Nigdy nie będziemy mieli narzędzia, które bezbłędnie wykryje każdy błąd/pętlę w dowolnym kodzie.")
    print("- Czy można stworzyć idealny antywirus? NIE, bo wykrywanie złośliwego zachowania w ogólnym przypadku sprowadza się do Halting Problem.")
    print("-" * 30)

def zadanie_11_rsa_factorization():
    print("Zadanie 11: Cybersecurity - Why Encryption Works")
    n = 12091
    print(f"Zadanie: Znajdź p i q takie, że p * q = {n}")
    
    import math
    p = -1
    q = -1
    iterations = 0
    # Checking up to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        iterations += 1
        if n % i == 0:
            p = i
            q = n // i
            break
            
    print(f"Wynik: p = {p}, q = {q} (sprawdzenie: {p} * {q} = {p*q})")
    print(f"Liczba iteracji: {iterations}")
    print(f"Dla 2048 bitów liczba operacji jest rzędu 2^1024, co przy obecnej technologii jest nieobliczalne.")
    print("-" * 30)

if __name__ == "__main__":
    zadanie_9_knapsack_dp()
    zadanie_10_halting_problem()
    zadanie_11_rsa_factorization()
