# ===========================================================
# BLOK E: FUNKCJE + TABLICE (3 zadania × 4 pkt = 12 pkt)
# ===========================================================

print("\n--- BLOK E: FUNKCJE + TABLICE ---\n")

# [2.7] 4 pkt - Filtruj liczby większe niż X
print("[2.7] 4 pkt - Funkcja filtrująca liczby")
print("""
Zadanie:
  Napisz funkcję filtruj_wieksze(lista, prog)
  Funkcja zwraca nową listę zawierającą tylko elementy > prog
  
Szablon:
  def filtruj_wieksze(lista, prog):
      wynik = []
      # Iteruj przez listę
      # Jeśli element > prog:
      #     Dodaj do wyniku
      return wynik
  
Test:
  print(filtruj_wieksze([1, 5, 3, 8, 2], 4))
  → [5, 8]
  
  print(filtruj_wieksze([10, 20, 5, 30], 15))
  → [20, 30]
  
  print(filtruj_wieksze([1, 2, 3], 10))
  → []
""")
# Twój kod:
def filtruj_wieksze(lista, prog):
    wynik = []
    for i in lista:
        if i > prog:
            wynik.append(i)
    return wynik

print(filtruj_wieksze([1, 5, 3, 8, 2], 4))
print(filtruj_wieksze([10, 20, 5, 30], 15))
print(filtruj_wieksze([1, 2, 3], 10))

# [2.8] 4 pkt - Średnia z listy z walidacją
print("\n[2.8] 4 pkt - Funkcja obliczająca średnią")
print("""
Zadanie:
  Napisz funkcję srednia(lista)
  Funkcja oblicza średnią arytmetyczną z listy
  WAŻNE: Jeśli lista jest pusta, zwróć None
  
Szablon:
  def srednia(lista):
      if len(lista) == 0:
          return None
      # Oblicz sumę
      # Podziel przez długość
      return ...
  
Algorytm:
  1. Sprawdź czy lista pusta → zwróć None
  2. Oblicz suma = sum(lista) LUB pętlą
  3. Oblicz srednia = suma / len(lista)
  4. Zwróć średnią
  
Test:
  print(srednia([10, 20, 30]))     → 20.0
  print(srednia([5, 5, 5, 5]))     → 5.0
  print(srednia([]))               → None
  print(srednia([100]))            → 100.0
""")
# Twój kod:
def srednia(lista):
    if len(lista) == 0:
        return None
    n = len(lista)
    suma = sum(lista)
    srednia = suma/n
    return srednia

print(srednia([10, 20, 30]))
print(srednia([5, 5, 5, 5]))
print(srednia([]))
print(srednia([100]))  

# [2.9] 4 pkt - Usuń duplikaty
print("\n[2.9] 4 pkt - Funkcja usuwająca duplikaty")
print("""
Zadanie:
  Napisz funkcję bez_duplikatow(lista)
  Funkcja zwraca nową listę bez powtórzeń (zachowaj kolejność pierwszych wystąpień)
  
Algorytm:
  1. Stwórz pustą listę: wynik = []
  2. Iteruj przez listę:
     - Jeśli element NIE jest w wynik:
       - Dodaj do wynik
  3. Zwróć wynik
  
Szablon:
  def bez_duplikatow(lista):
      wynik = []
      for element in lista:
          if element not in wynik:
              wynik.append(element)
      return wynik
  
Test:
  print(bez_duplikatow([1, 2, 2, 3, 1, 4]))
  → [1, 2, 3, 4]
  
  print(bez_duplikatow([5, 5, 5]))
  → [5]
  
  print(bez_duplikatow([1, 2, 3]))
  → [1, 2, 3]
""")
# Twój kod:
def bez_duplikatow(lista):
    wynik = []
    for element in lista:
        if element not in wynik:
            wynik.append(element)
    return wynik

print(bez_duplikatow([1, 2, 2, 3, 1, 4]))
print(bez_duplikatow([5, 5, 5]))
print(bez_duplikatow([1, 2, 3]))