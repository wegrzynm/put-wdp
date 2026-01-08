
Lab9 cwiczenia
Laboratorium 9: Złożoność obliczeniowa - Część 2 (Zaawansowana)
Kurs: Introduction to Programming
Kierunek: Cybersecurity, rok 1
Czas: 90 minut
Prowadzący: Bartosz Lewandowski

🎯 Cele laboratorium
Po tym laboratorium będziesz potrafić:

Rozpoznać problemy NP-complete
Zrozumieć dlaczego niektóre problemy są "trudne"
Zastosować problem reduction w praktyce
Zrozumieć granice obliczalności (halting problem)
Wyjaśnić dlaczego kryptografia działa (P ≠ NP)
📊 System oceniania
Minimum (3.0): 8 punktów - zadania 1-8
Dobra ocena (4.0): 10 punktów - zadania 1-10
Bardzo dobra ocena (5.0): 12+ punktów - wszystkie zadania + rozszerzone
Maksymalna liczba punktów: 15

🔥 Rozgrzewka - Przypomnienie Lab 8 (1 pkt każde)
Zadanie 1: Quick Review
Dopasuj złożoność do algorytmu:

Algorytmy:

A) Binary search
B) Bubble sort
C) Array access lista[0]
D) Heapsort
Złożoności:

O(1)
O(log n)
O(n log n)
O(n²)
Zadanie 2: Co jest szybsze?
Dla n = 10,000:

Algorytm A: O(n²) = 100,000,000 operacji
Algorytm B: O(2ⁿ) = ?

Która odpowiedź jest poprawna?

A) Algorytm A jest szybszy
B) Algorytm B jest szybszy
C) Są podobnie szybkie
D) Algorytm B nigdy się nie skończy w rozsądnym czasie
Zadanie 3: Real-world Impact
Dlaczego Google używa algorytmów O(n log n) zamiast O(n²)?

A) Bo O(n log n) są prostsze do implementacji
B) Bo dla miliardów rekordów różnica to sekundy vs lata
C) Bo tak powiedział Larry Page
D) Bo O(n²) wymaga więcej pamięci
🎯 Zadania podstawowe (1 pkt każde)
Zadanie 4: Knapsack Problem - Wprowadzenie
Problem plecakowy (Knapsack):

Plecak o pojemności C = 10 kg
Przedmioty:
A: waga 2kg, wartość $3
B: waga 3kg, wartość $5
C: waga 5kg, wartość $9
D: waga 7kg, wartość $14
Pytanie: Które przedmioty wybrać żeby zmaksymalizować wartość?

Opcje:

a) A + B + C (waga 10kg, wartość $17)
b) B + D (waga 10kg, wartość $19)
c) A + C (waga 7kg, wartość $12)
d) Tylko D (waga 7kg, wartość $14)
Pytanie dodatkowe: Ile jest możliwych kombinacji dla 4 przedmiotów?

Zadanie 5: Brute Force Explosion
Załóżmy że masz 20 przedmiotów i plecak.

Brute force approach: Sprawdź wszystkie kombinacje.

Pytania:

Ile jest możliwych kombinacji? (2²⁰ = ?)
Jeśli sprawdzenie jednej kombinacji zajmuje 1 mikrosekundę, ile czasu zajmie sprawdzenie wszystkich?
Czy dla 30 przedmiotów brute force jest realistyczny?
Wskazówka:

2¹⁰ = 1,024 ≈ 1 tysiąc
2²⁰ = ?
2³⁰ = ?
Zadanie 6: P vs NP - Quiz
Dopasuj problemy do kategorii:

Problemy:

A) Sortowanie listy liczb
B) Znajdowanie najkrótszej ścieżki w grafie
C) Traveling Salesman Problem
D) Sprawdzenie czy liczba jest pierwsza
E) Knapsack Problem
F) Boolean Satisfiability (SAT)
Kategorie:

P: Problemy rozwiązywalne w czasie wielomianowym (O(nᵏ))
NP-complete: Najtrudniejsze problemy w NP (prawdopodobnie nie P)
Zadanie 7: Verifier vs Solver
Kluczowa różnica NP:

Solving: Znalezienie rozwiązania (trudne!)
Verifying: Sprawdzenie czy rozwiązanie jest poprawne (łatwe!)
Przykład - Sudoku:

Solving: Wypełnij pustą siatkę Sudoku
  → Trudne! (backtracking, trial and error)

Verifying: Sprawdź czy wypełniona siatka jest poprawna  
  → Łatwe! (sprawdź każdy wiersz/kolumnę/kwadrat)
Pytanie: Dla każdego problemu określ czy solving jest łatwy czy trudny:

Problem	Solving	Verifying
Sortowanie	?	O(n)
Sudoku 9×9	?	O(1)
TSP dla 100 miast	?	O(n)
Czy liczba pierwsza?	?	?
Zadanie 8: Problem Reduction
Problem reduction: Sprowadzenie problemu A do problemu B.

Przykład:

Problem A: Czy w grafie jest cykl Hamiltona?
  ↓ (redukcja)
Problem B: Traveling Salesman Problem (TSP)

Jeśli potrafię rozwiązać TSP, to potrafię rozwiązać Hamiltonian Cycle!
Pytanie: Które redukcje są poprawne?

a) Sortowanie → Binary search (posortowana lista potrzebna)
b) Knapsack → Partition problem
c) Password cracking → SAT problem
d) Sudoku → Graph coloring
💪 Zadania rozszerzone (2 pkt każde)
Zadanie 9: Knapsack - Dynamic Programming Intro
Problem: Plecak C=7, przedmioty:

A: waga 3, wartość 5
B: waga 4, wartość 6
C: waga 2, wartość 3
Podejście naiwne: O(2³) = 8 kombinacji

Dynamic Programming: Zbuduj tabelę wartości dla pojemności 0-7

Pytania:

Jaka jest maksymalna wartość dla C=7?
Które przedmioty wybrać?
Czy to nadal O(2ⁿ)? (Odpowiedź: Nie! To O(n·C))
Zadanie 10: Halting Problem - Proof by Contradiction
prog = '''
while WillHalt(prog):
    pass
print(13)
'''

def WillHalt(p):
    # Magiczny kod który sprawdza czy program p się zatrzyma
    # Czy to możliwe do napisania?
    ???
Analiza:

CASE 1: WillHalt(prog) zwraca True

"Program się zatrzyma" - predykcja
ALE: pętla while True: działa w nieskończoność!
Czyli program NIE zatrzymuje się!
SPRZECZNOŚĆ! ❌
CASE 2: WillHalt(prog) zwraca False

"Program NIE zatrzyma się" - predykcja
ALE: pętla while False: się kończy natychmiast!
Potem print(13) i koniec
Czyli program ZATRZYMUJE się!
SPRZECZNOŚĆ! ❌
Wniosek: Funkcja WillHalt() nie może istnieć! (Halting problem is undecidable)

Pytania:

Dlaczego dowód działa przez sprzeczność?
Co to oznacza dla automatic code analysis?
Czy można stworzyć idealny antywirus? (Odpowiedź: NIE!)
Zadanie 11: Cybersecurity - Why Encryption Works
RSA Encryption bazuje na założeniu P ≠ NP:

Public Key Cryptography:
- Mnożenie: 61 × 53 = 3233 (ŁATWE - O(n²))
- Faktoryzacja: 3233 = ? × ? (TRUDNE - brak znanych algorytmów O(nᵏ))

Dla liczb 2048-bitowych:
- Mnożenie: milisekundy
- Faktoryzacja: miliardy lat (brute force)
Problem: Masz n = 12091 (public key). Znajdź p i q takie że p × q = n.

Pytania:

Ile iteracji dla n=12091? (√12091 ≈ 110)
Dla n=2048 bitów (617 cyfr), ile operacji?
Dlaczego quantum computing jest zagrożeniem? (Shor's algorithm!)
Fun fact:

RSA-250 (829 bitów): złamany w 2020 po 2700 CPU-years
RSA-2048: Szacowany czas > wiek wszechświata!
🚀 Zadania MEGA rozszerzone (3 pkt)
Zadanie 12: Simple SAT Solver
Boolean Satisfiability (SAT): Masz formułę logiczną. Czy istnieje przypisanie zmiennych które ją spełnia?

Przykład:

(A ∨ B) ∧ (¬A ∨ C) ∧ (¬B ∨ ¬C)

gdzie:
∨ = OR
∧ = AND  
¬ = NOT
Zadanie: Napisz prosty SAT solver brute force

Wskazówki:

Sprawdź wszystkie 2ⁿ kombinacji
Dla każdej kombinacji: sprawdź czy spełnia wszystkie klauzule
Złożoność: O(2ⁿ · m) gdzie m = liczba klauzul
🎓 Wskazówki i przydatne informacje
P vs NP - Quick Reference
P (Polynomial time):

Problemy rozwiązywalne w czasie O(nᵏ)
Przykłady: sorting, shortest path, prime testing
"Łatwe" dla komputerów
NP (Nondeterministic Polynomial time):

Rozwiązanie trudne, ale weryfikacja łatwa (O(nᵏ))
Przykłady: Sudoku, Knapsack, TSP
Zawiera P (bo jeśli solving jest łatwe, to verifying też)
NP-complete:

Najtrudniejsze problemy w NP
Jeśli znajdziesz algorytm O(nᵏ) dla JEDNEGO NP-complete → rozwiązujesz WSZYSTKIE!
P = NP? → $1,000,000 nagroda (Millennium Prize)
Halting Problem - Implikacje
Nie można automatycznie:

✗ Sprawdzić czy program ma bug
✗ Sprawdzić czy program jest bezpieczny
✗ Stworzyć idealny antywirus
✗ Guarantee że kod jest wolny od deadlock
Dlatego:

Testing > Proving (nie możemy udowodnić poprawności)
Heuristics > Perfect algorithms (dla wielu problemów)
Defense in depth (wiele warstw zabezpieczeń)
🎭 Suchar na koniec
Q: Dlaczego programiści nie mają problemów z NP-complete?
A: Bo zawsze mogą użyć O(scary)! 😄

(O(scary) = aproksymacja, heurystyki, "good enough" solutions)

Powodzenia! Pamiętaj:

P = NP? Nobody knows!
NP ≠ impossible, just "probably hard"
Real-world: approximation algorithms FTW! 🚀