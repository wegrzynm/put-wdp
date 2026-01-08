
Lab8 cwiczenia
Laboratorium 8: Złożoność obliczeniowa
Kurs: Introduction to Programming
Kierunek: Cybersecurity, rok 1
Czas: 90 minut
Prowadzący: Bartosz Lewandowski

🎯 Cele laboratorium
Po tym laboratorium będziesz potrafić:

Rozpoznać podstawowe klasy złożoności: O(1), O(n), O(n²), O(log n), O(n log n)
Policzyć liczbę operacji w prostych algorytmach
Zrozumieć, dlaczego niektóre algorytmy są szybsze od innych
Zastosować notację Big O do analizy własnego kodu
📊 System oceniania
Minimum (3.0): 8 punktów - zadania 1-8
Dobra ocena (4.0): 10 punktów - zadania 1-10
Bardzo dobra ocena (5.0): 12+ punktów - wszystkie zadania + rozszerzone
Maksymalna liczba punktów: 15

🔥 Rozgrzewka - Zliczanie operacji (1 pkt każde)
Zadanie 1: Stała złożoność
def get_first(lista):
    return lista[0]
Pytanie: Ile operacji wykonuje ta funkcja dla listy o długości n?

A) 1
B) n
C) n²
D) Zależy od n
Zadanie 2: Liniowa złożoność
def sum_all(lista):
    suma = 0
    for x in lista:
        suma += x
    return suma
Pytanie: Ile operacji dodawania wykonuje ta funkcja dla listy o długości n?

Zadanie 3: Kwadratowa złożoność
def print_pairs(lista):
    for i in lista:
        for j in lista:
            print(i, j)
Pytanie: Ile par wypisze ten kod dla listy o długości n?

🎯 Zadania podstawowe (1 pkt każde)
Zadanie 4: Rozpoznaj złożoność
Dopasuj fragmenty kodu do ich złożoności czasowej:

Kod A:

def find_max(lista):
    max_val = lista[0]
    for x in lista:
        if x > max_val:
            max_val = x
    return max_val
Kod B:

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
Kod C:

def binary_search(lista, x):
    left, right = 0, len(lista)-1
    while left <= right:
        mid = (left + right) // 2
        if lista[mid] == x:
            return mid
        elif lista[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
Złożoności:

O(n)
O(n²)
O(log n)
Zadanie 5: Selection Sort - zliczanie porównań
def selection_sort(lista):
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
Pytanie: Ile porównań wykona ten algorytm dla listy o długości n=5?

Wskazówka: Policz iteracje pętli zagnieżdżonej:

Gdy i=0: j biegnie od 1 do 4 → 4 porównania
Gdy i=1: j biegnie od 2 do 4 → 3 porównania
...
Zadanie 6: Heap vs Selection Sort
Uzupełnij tabelę z liczbą operacji:

n (rozmiar)	Selection Sort O(?)	Heapsort O(?)
10	~100	~33
100	~10,000	~664
1,000	~1,000,000	~9,966
10,000	?	?
Wzory:

Selection Sort: ≈ n²/2
Heapsort: ≈ 2n log₂(n)
Zadanie 7: Praktyczny pomiar czasu
Napisz program, który:

Wygeneruje losową listę 1000 liczb
Zmierzy czas sortowania (użyj time.time())
Porówna selection sort z wbudowanym sorted()
import time
import random

# Twój kod tutaj
Zadanie 8: Big O - definicja
Która z funkcji jest O(n²)?

A) f(n) = 5n² + 3n + 100
B) f(n) = 2n³ + n²
C) f(n) = n log n
D) f(n) = 2ⁿ

Pytanie dodatkowe: Dlaczego w Big O pomijamy stałe współczynniki i niższe rzędy?

💪 Zadania rozszerzone (2 pkt każde)
Zadanie 9: Analiza kodu z Challenges
Przeanalizuj złożoność Challenge 7.C (liczenie liter w miastach):

for i in range(len(cities)-1, -1, -1):  # n iteracji
    for c in range(len(cities[i])):      # m iteracji (średnia długość miasta)
        if cities[i][c] == SYMBOL:
            counter += 1
Pytania:

Jaka jest złożoność tego kodu jako funkcja n (liczba miast) i m (średnia długość nazwy)?
Jeśli n=100 i m=10, ile operacji porównania wykonamy?
Czy możesz zaproponować szybszy algorytm?
Zadanie 10: Heap - analiza wysokości
Uzupełnij tabelę pokazującą zależność wysokości kopca od liczby węzłów:

Liczba węzłów (n)	Wysokość kopca (h)
1	0
2-3	1
4-7	2
8-15	?
16-31	?
1024-2047	?
Wzór: h = ⌊log₂(n)⌋

Pytanie: Dlaczego insert() w heap ma złożoność O(log n)?

Zadanie 11: Cybersecurity - Password cracking
Załóżmy, że hasło składa się z małych liter (26 znaków).

Brute force attack:

Hasło 4-znakowe: 26⁴ = 456,976 prób
Hasło 6-znakowe: 26⁶ = 308,915,776 prób
Hasło 8-znakowe: 26⁸ = ?
Pytania:

Oblicz liczbę prób dla hasła 8-znakowego
Jeśli komputer sprawdza 1 milion haseł/sekundę, ile czasu zajmie złamanie hasła 8-znakowego?
Jaka jest złożoność czasowa tego ataku jako funkcja długości hasła n?
Fun fact: Dlatego hasła powinny być długie i zawierać różne znaki!

🚀 Zadania MEGA rozszerzone (3 pkt)
Zadanie 12: Implementacja Simple Heap
Zaimplementuj prostą kolejkę priorytetową używając listy jako kopca binarnego:

class SimpleHeap:
    def __init__(self):
        self.heap = [None]  # Indeks 0 pusty dla wygody
        
    def insert(self, value):
        """Wstaw element do kopca"""
        # Twoja implementacja
        # Wskazówka: Father(x) = x // 2
        pass
        
    def take_max(self):
        """Usuń i zwróć największy element"""
        # Twoja implementacja
        pass
Testy:

h = SimpleHeap()
h.insert(10)
h.insert(30)
h.insert(20)
print(h.take_max())  # Powinno wypisać: 30
print(h.take_max())  # Powinno wypisać: 20
🎓 Wskazówki i przydatne informacje
Podstawowe klasy złożoności (od najszybszej):
O(1) - stała: array[0], dict[key]
O(log n) - logarytmiczna: binary search, operacje na heap
O(n) - liniowa: przejście przez listę, sum()
O(n log n) - liniowo-logarytmiczna: merge sort, heap sort
O(n²) - kwadratowa: bubble sort, selection sort, zagnieżdżone pętle
O(2ⁿ) - wykładnicza: wszystkie podzbiory zbioru
Praktyczne porównanie (n = 1,000,000):
Złożoność	Liczba operacji	Czas (1 op = 1ns)
O(1)	1	1 ns
O(log n)	~20	20 ns
O(n)	1,000,000	1 ms
O(n log n)	~20,000,000	20 ms
O(n²)	1,000,000,000,000	11.5 dni
Mierzenie czasu w Pythonie:
import time

start = time.time()
# Twój kod
end = time.time()
print(f"Czas wykonania: {end - start:.4f} sekund")
Powodzenia! Pamiętaj: Big O to nie straszne, to tylko matematyczny sposób na powiedzenie "jak wolno rośnie twój algorytm" 🚀