# ===========================================================
# SEKCJA 2: ROZSZERZONY (wybór)
# ===========================================================

print("\n" + "="*60)
print("### SEKCJA 2: POZIOM ROZSZERZONY ###")
print("Zadania 2.1-2.12 (opcjonalne - wybierz według strategii)")
print("="*60 + "\n")

# ===========================================================
# BLOK C: TABLICE + PĘTLE (3 zadania × 3 pkt = 9 pkt)
# ===========================================================

print("--- BLOK C: TABLICE + PĘTLE ---\n")

# [2.1] 3 pkt - Znajdź maksimum w liście
print("[2.1] 3 pkt - Znajdź maksimum w liście")
print("""
Zadanie:
  Dano lista = [3, 7, 2, 9, 1, 5]
  Znajdź i wyświetl największą liczbę (bez użycia funkcji max())
  
Algorytm:
  1. Ustaw maksimum = lista[0] (pierwszy element)
  2. Iteruj przez resztę listy:
     - Jeśli element > maksimum:
       - maksimum = element
  3. Wyświetl maksimum
  
Oczekiwane wyjście:
  Maksimum = 9
  
Wskazówka:
  for liczba in lista:
      if liczba > maksimum:
          maksimum = liczba
""")
# Twój kod:
lista = [3, 7, 2, 9, 1, 5]
max = 0
for i in lista:
    if i > max:
        max = i

print(f"Max to: {max}")


# [2.2] 3 pkt - Odwróć listę
print("\n[2.2] 3 pkt - Odwróć listę")
print("""
Zadanie:
  Dano lista = [1, 2, 3, 4, 5]
  Odwróć kolejność elementów (bez użycia reverse() lub [::-1])
  Wyświetl odwróconą listę
  
Algorytm - metoda 1 (nowa lista):
  1. Stwórz pustą listę: odwrocona = []
  2. Iteruj przez listę od końca:
     for i in range(len(lista)-1, -1, -1):
         odwrocona.append(lista[i])
  
Algorytm - metoda 2 (swap w miejscu):
  1. Użyj dwóch wskaźników: lewy=0, prawy=len(lista)-1
  2. Dopóki lewy < prawy:
     - Zamień elementy: lista[lewy], lista[prawy] = lista[prawy], lista[lewy]
     - lewy += 1, prawy -= 1
  
Oczekiwane wyjście:
  [5, 4, 3, 2, 1]
""")
# Twój kod:
lista = [1, 2, 3, 4, 5]
reversed = []
for i in range(len(lista)-1, -1, -1):
    reversed.append(lista[i])

print(reversed)

# [2.3] 3 pkt - Policz wystąpienia elementu
print("\n[2.3] 3 pkt - Policz wystąpienia elementu")
print("""
Zadanie:
  Dano lista = [1, 2, 3, 2, 2, 4, 2, 5]
  Dano x = 2
  Policz ile razy element x występuje w liście (bez użycia count())
  
Algorytm:
  1. Ustaw licznik = 0
  2. Iteruj przez listę:
     - Jeśli element == x:
       - Zwiększ licznik o 1
  3. Wyświetl wynik
  
Oczekiwane wyjście dla x=2:
  Element 2 występuje 4 razy
""")
# Twój kod:
lista = [1, 2, 3, 2, 2, 4, 2, 5]
x = 2
counter = 0
for i in lista:
    if i == x:
        counter += 1

print(f"Liczba wystąpień {x} wynosi: {counter}")