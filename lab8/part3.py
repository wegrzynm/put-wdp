import math

# Laboratorium 8: Złożoność obliczeniowa
# Cześć 3: Zadania rozszerzone

# Zadanie 9: Analiza kodu z Challenges
def task_9_analysis():
    """
    1. Złożoność: O(n * m)
       Gdzie n to liczba miast, a m to średnia długość nazwy miasta.
    2. Dla n=100 i m=10:
       Liczba operacji = 100 * 10 = 1 000 porównań.
    3. Szybszy algorytm?
       Złożoność asymptotyczna nie ulegnie poprawie (musimy sprawdzić każdy znak),
       ale w Pythonie można użyć metody .count():
       suma = sum(city.count(SYMBOL) for city in cities)
       Jest to szybsze dzięki optymalizacji na poziomie interpreterera (C).
    """
    print("Zadanie 9: Analiza złożoności zliczania liter")
    print("Złożoność: O(n * m)")
    print(f"Dla n=100, m=10: {100 * 10} operacji")

# Zadanie 10: Heap - analiza wysokości
def task_10_heap_height():
    """
    Wzór: h = floor(log2(n))
    
    Tabela:
    8-15 węzłów   -> Wysokość 3
    16-31 węzłów  -> Wysokość 4
    1024-2047 węzłów -> Wysokość 10
    
    Dlaczego insert() w heap ma złożoność O(log n)?
    Bo w najgorszym przypadku element wstawiony na koniec musi "powędrować" 
    aż do korzenia. Ścieżka ta jest równa wysokości drzewa, która wynosi log2(n).
    """
    print("\nZadanie 10: Wysokość kopca")
    nodes = [10, 20, 1024]
    for n in nodes:
        h = int(math.log2(n))
        print(f"Dla n={n}, wysokość h = {h}")

# Zadanie 11: Cybersecurity - Password cracking
def task_11_passwords():
    """
    Alphabet = 26 małych liter.
    
    1. Liczba prób dla hasła 8-znakowego:
       26^8 = 208,827,064,576
       
    2. Czas przy 1 mln haseł/sekundę:
       sekund = 208,827,064,576 / 1,000,000 ≈ 208,827 s
       godzin = 208,827 / 3600 ≈ 58 h
       dni = 58 / 24 ≈ 2.42 dni
       
    3. Złożoność czasowa:
       O(A^n), gdzie A to wielkość alfabetu (stała), n to długość hasła.
       Jest to złożoność wykładnicza względem długości hasła.
    """
    alphabet_size = 26
    length = 8
    total_combinations = alphabet_size ** length
    
    speed = 1_000_000 # na sekundę
    seconds = total_combinations / speed
    hours = seconds / 3600
    days = hours / 24
    
    print("\nZadanie 11: Password cracking (Brute Force)")
    print(f"Liczba kombinacji dla 8 znaków: {total_combinations:,}")
    print(f"Przy prędkości 1 mln/s, zajmie to około: {days:.2f} dni")

if __name__ == "__main__":
    task_9_analysis()
    task_10_heap_height()
    task_11_passwords()
