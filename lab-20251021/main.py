# ===========================================================
# ĆWICZENIA LAB 2: PĘTLE, FUNKCJE, TABLICE, CASE
# System oceniania: PUNKTOWY
# ===========================================================
# 
# Czas: 90 minut
# Zakres: Pętle (for/while), funkcje, tablice/listy, case/match
#
# ===========================================================
# SYSTEM PUNKTOWY - ZASADY OCENIANIA
# ===========================================================
#
# Każde zadanie ma przypisaną WAGĘ PUNKTOWĄ:
#
# 📗 MINIMUM - PĘTLE (1.1-1.3):        2 pkt każde
# 📗 MINIMUM - FUNKCJE (1.4-1.5):      2 pkt każde
# 📙 TABLICE + PĘTLE (2.1-2.3):        3 pkt każde
# 📙 CASE/MATCH (2.4-2.6):             3 pkt każde
# 📕 FUNKCJE + TABLICE (2.7-2.9):      4 pkt każde
# 🔥 ALGORYTMICZNE (2.10-2.12):        6 pkt każde
#
# MINIMUM DO ZALICZENIA (3.0) = 10 punktów:
#   Zadania 1.1-1.5 (5×2=10 pkt)
#
# SKALA OCEN:
#   10-14 pkt  → 3.0
#   15-19 pkt  → 3.5
#   20-25 pkt  → 4.0
#   26-31 pkt  → 4.5
#   32+ pkt    → 5.0
#
# STRATEGIE (przykłady):
#   • 3.5: minimum + 2 tablice (10+6=16)
#   • 4.0: minimum + 3 tablice + 1 case (10+9+3=22)
#   • 4.5: minimum + 1 algorytmiczne + 2 tablice (10+6+6=22... lepiej 26+)
#   • 4.5: minimum + 3 funkcje+tablice (10+12=22... lepiej 26+)
#   • 5.0: minimum + 2 algorytmiczne (10+12=22... lepiej 32+)
#   • 5.0: minimum + wszystkie algorytmiczne (10+18=28... lepiej 32+)
#
# NIE MUSISZ ROBIĆ WSZYSTKIEGO!
# Wybierz strategię pod swój poziom i cele.
#
# ===========================================================

print("="*60)
print("ĆWICZENIA LAB 2: PĘTLE, FUNKCJE, TABLICE, CASE")
print("System punktowy")
print("="*60)

# ===========================================================
# SEKCJA 1: MINIMUM (5 zadań × 2 pkt = 10 pkt) - OBOWIĄZKOWE
# ===========================================================

print("\n" + "="*60)
print("### SEKCJA 1: MINIMUM - OBOWIĄZKOWE ###")
print("Zadania 1.1-1.5 (wymagane do zaliczenia)")
print("Waga: 2 pkt każde | Razem: 10 pkt")
print("="*60 + "\n")

# ===========================================================
# BLOK A: PĘTLE PODSTAWOWE (3 zadania × 2 pkt = 6 pkt)
# ===========================================================

print("--- BLOK A: PĘTLE PODSTAWOWE ---\n")

# [1.1] 2 pkt - ZADANIE: Wyświetl liczby od 1 do N
print("[1.1] 2 pkt - Wyświetl liczby od 1 do N")
print("""
Zadanie:
  Zdefiniuj zmienną n = 5
  Użyj pętli for i range() aby wyświetlić liczby od 1 do n (włącznie)
  
Oczekiwane wyjście dla n=5:
  1 2 3 4 5
  
Wskazówka:
  for i in range(1, n+1):
      print(i, end=" ")
""")
# Twój kod:




# [1.2] 2 pkt - ZADANIE: Suma liczb od 1 do N
print("\n[1.2] 2 pkt - Suma liczb od 1 do N")
print("""
Zadanie:
  Zdefiniuj zmienną n = 10
  Użyj pętli while aby obliczyć sumę liczb od 1 do n
  Wyświetl wynik w formacie: "Suma = 55"
  
Algorytm:
  1. Zdefiniuj suma = 0
  2. Zdefiniuj i = 1
  3. Dopóki i <= n:
     - Dodaj i do sumy
     - Zwiększ i o 1
  4. Wyświetl wynik
  
Oczekiwane wyjście dla n=10:
  Suma = 55
""")
# Twój kod:




# [1.3] 2 pkt - ZADANIE: Liczby parzyste z listy
print("\n[1.3] 2 pkt - Liczby parzyste z listy")
print("""
Zadanie:
  Dano lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  Wyświetl tylko liczby parzyste (podzielne przez 2)
  
Algorytm:
  1. Iteruj przez listę (for liczba in lista)
  2. Jeśli liczba % 2 == 0:
     - Wyświetl liczbę
  
Oczekiwane wyjście:
  2 4 6 8 10
""")
# Twój kod:




# ===========================================================
# BLOK B: FUNKCJE PODSTAWOWE (2 zadania × 2 pkt = 4 pkt)
# ===========================================================

print("\n--- BLOK B: FUNKCJE PODSTAWOWE ---\n")

# [1.4] 2 pkt - ZADANIE: Funkcja obliczająca pole prostokąta
print("[1.4] 2 pkt - Funkcja obliczająca pole prostokąta")
print("""
Zadanie:
  Zdefiniuj funkcję pole_prostokata(a, b)
  Funkcja powinna zwracać pole prostokąta (a * b)
  
Szablon:
  def pole_prostokata(a, b):
      # Twój kod
      return ...
  
Test:
  print(pole_prostokata(5, 3))   # → 15
  print(pole_prostokata(10, 2))  # → 20
""")
# Twój kod:




# [1.5] 2 pkt - ZADANIE: Funkcja sprawdzająca parzystość
print("\n[1.5] 2 pkt - Funkcja sprawdzająca parzystość")
print("""
Zadanie:
  Zdefiniuj funkcję czy_parzysta(n)
  Funkcja powinna zwracać True jeśli liczba jest parzysta, False w przeciwnym razie
  
Szablon:
  def czy_parzysta(n):
      # Twój kod
      return ...
  
Test:
  print(czy_parzysta(4))   # → True
  print(czy_parzysta(7))   # → False
  print(czy_parzysta(0))   # → True
""")
# Twój kod:




print("\n" + "="*60)
print("✅ MINIMUM ZALICZONE!")
print("Jeśli zrobiłeś/aś 1.1-1.5, masz 10 punktów = 3.0")
print("")
print("Chcesz wyższej oceny? Wybierz zadania poniżej! ⬇️")
print("="*60)


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




# ===========================================================
# BLOK D: CASE/MATCH (3 zadania × 3 pkt = 9 pkt)
# ===========================================================

print("\n--- BLOK D: CASE/MATCH (lub if-elif) ---\n")

# [2.4] 3 pkt - Kalkulator
print("[2.4] 3 pkt - Prosty kalkulator")
print("""
Zadanie:
  Stwórz kalkulator dla 4 działań: +, -, *, /
  Wejście: a = 10, b = 5, operator = '+'
  Wyświetl wynik w formacie: "10 + 5 = 15"
  
Metoda 1 - if-elif-else:
  if operator == '+':
      wynik = a + b
  elif operator == '-':
      wynik = a - b
  ...
  
Metoda 2 - match/case (Python 3.10+):
  match operator:
      case '+':
          wynik = a + b
      case '-':
          wynik = a - b
      ...
  
Test:
  a, b = 10, 5
  operator = '+'  → 10 + 5 = 15
  operator = '-'  → 10 - 5 = 5
  operator = '*'  → 10 * 5 = 50
  operator = '/'  → 10 / 5 = 2.0
""")
# Twój kod:




# [2.5] 3 pkt - Konwerter jednostek
print("\n[2.5] 3 pkt - Konwerter jednostek odległości")
print("""
Zadanie:
  Konwertuj odległości: km ↔ m ↔ cm
  Wejście: wartosc, jednostka_z, jednostka_na
  
Przeliczniki:
  1 km = 1000 m
  1 m = 100 cm
  1 km = 100000 cm
  
Przykłady:
  5 km → m: 5 * 1000 = 5000 m
  5000 m → km: 5000 / 1000 = 5 km
  2 m → cm: 2 * 100 = 200 cm
  
Algorytm (najprostszy):
  1. Sprawdź parę jednostka_z → jednostka_na
  2. Zastosuj odpowiedni przelicznik
  3. Wyświetl wynik
  
Test:
  wartosc, z, na = 5, 'km', 'm'
  → "5 km = 5000 m"
  
  wartosc, z, na = 200, 'cm', 'm'
  → "200 cm = 2.0 m"
""")
# Twój kod:




# [2.6] 3 pkt - Ocena na słowo
print("\n[2.6] 3 pkt - Ocena liczbowa na opis słowny")
print("""
Zadanie:
  Zamień ocenę liczbową (2.0-5.0) na opis słowny
  
Mapowanie:
  5.0 → "Celujący"
  4.5 → "Bardzo dobry plus"
  4.0 → "Bardzo dobry"
  3.5 → "Dobry plus"
  3.0 → "Dobry"
  2.0 → "Dostateczny"
  Inne → "Niepoprawna ocena"
  
Metoda - match/case lub if-elif:
  match ocena:
      case 5.0:
          opis = "Celujący"
      case 4.5:
          opis = "Bardzo dobry plus"
      ...
  
Test:
  ocena = 5.0 → "Ocena 5.0: Celujący"
  ocena = 3.5 → "Ocena 3.5: Dobry plus"
  ocena = 1.0 → "Ocena 1.0: Niepoprawna ocena"
""")
# Twój kod:




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




# ===========================================================
# BLOK F: ALGORYTMICZNE - WYZWANIE! (3 zadania × 6 pkt = 18 pkt)
# ===========================================================

print("\n" + "="*60)
print("### 🔥 BLOK F: ZADANIA ALGORYTMICZNE - WYZWANIE! ###")
print("Zadania 2.10-2.12 (opcjonalne)")
print("Waga: 6 pkt każde | Max: 18 pkt")
print("Wymagają wymyślenia algorytmu + implementacji")
print("="*60 + "\n")

# [2.10] 6 pkt - Liczby pierwsze do N
print("[2.10] 6 pkt - Znajdź liczby pierwsze do N")
print("""
Zadanie:
  Napisz funkcję liczby_pierwsze(n)
  Funkcja zwraca listę wszystkich liczb pierwszych od 2 do n (włącznie)
  
Liczba pierwsza = podzielna tylko przez 1 i przez siebie
Przykłady: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29...

Algorytm (naiwny):
  1. Stwórz pustą listę: pierwsze = []
  2. Dla każdej liczby od 2 do n:
     a) Załóż że jest pierwsza: jest_pierwsza = True
     b) Sprawdź dzielniki od 2 do liczba-1:
        - Jeśli liczba % dzielnik == 0:
          - jest_pierwsza = False
          - Przerwij pętlę (break)
     c) Jeśli jest_pierwsza:
        - Dodaj do listy pierwsze
  3. Zwróć listę

Optymalizacja (opcjonalnie):
  - Wystarczy sprawdzać dzielniki do sqrt(liczba)
  - Pomiń liczby parzyste (poza 2)

Szablon:
  def liczby_pierwsze(n):
      pierwsze = []
      for liczba in range(2, n+1):
          jest_pierwsza = True
          for dzielnik in range(2, liczba):
              if liczba % dzielnik == 0:
                  jest_pierwsza = False
                  break
          if jest_pierwsza:
              pierwsze.append(liczba)
      return pierwsze

Test:
  print(liczby_pierwsze(20))
  → [2, 3, 5, 7, 11, 13, 17, 19]
  
  print(liczby_pierwsze(10))
  → [2, 3, 5, 7]
  
  print(liczby_pierwsze(2))
  → [2]
""")
# Twój kod:




# [2.11] 6 pkt - FizzBuzz
print("\n[2.11] 6 pkt - FizzBuzz")
print("""
Zadanie:
  Napisz funkcję fizzbuzz(n)
  Dla liczb od 1 do n:
    - Jeśli podzielna przez 3 i 5 → wyświetl "FizzBuzz"
    - Jeśli podzielna przez 3 → wyświetl "Fizz"
    - Jeśli podzielna przez 5 → wyświetl "Buzz"
    - W przeciwnym razie → wyświetl liczbę
  
WAŻNE: Kolejność warunków ma znaczenie!
  Najpierw sprawdź 3 i 5, potem 3, potem 5, potem liczbę

Algorytm:
  def fizzbuzz(n):
      for i in range(1, n+1):
          if i % 3 == 0 and i % 5 == 0:
              print("FizzBuzz")
          elif i % 3 == 0:
              print("Fizz")
          elif i % 5 == 0:
              print("Buzz")
          else:
              print(i)

Test fizzbuzz(15):
  1
  2
  Fizz      (3)
  4
  Buzz      (5)
  Fizz      (6)
  7
  8
  Fizz      (9)
  Buzz      (10)
  11
  Fizz      (12)
  13
  14
  FizzBuzz  (15)

ROZSZERZENIE (dla ambitnych):
  Zamiast wyświetlać, zwróć listę stringów
""")
# Twój kod:




# [2.12] 6 pkt - Palindrom liczbowy
print("\n[2.12] 6 pkt - Czy liczba jest palindromem?")
print("""
Zadanie:
  Napisz funkcję czy_palindrom(n)
  Funkcja sprawdza czy liczba jest palindromem (czyta się tak samo od przodu i tyłu)
  Zwraca True lub False
  
Przykłady palindromów:
  121 → True (1-2-1)
  1331 → True (1-3-3-1)
  12321 → True (1-2-3-2-1)
  123 → False (1-2-3 vs 3-2-1)

Algorytm - metoda 1 (string):
  1. Zamień liczbę na string: s = str(n)
  2. Odwróć string: odwrocony = s[::-1]
  3. Porównaj: return s == odwrocony

Algorytm - metoda 2 (matematyczna):
  1. Zapisz oryginalną liczbę: oryginalna = n
  2. Zbuduj odwróconą liczbę:
     odwrocona = 0
     while n > 0:
         cyfra = n % 10
         odwrocona = odwrocona * 10 + cyfra
         n = n // 10
  3. Porównaj: return oryginalna == odwrocona

Przykład dla 121:
  Iteracja 1: cyfra=1, odwrocona=1, n=12
  Iteracja 2: cyfra=2, odwrocona=12, n=1
  Iteracja 3: cyfra=1, odwrocona=121, n=0
  121 == 121 → True

Szablon (metoda 1 - prostsza):
  def czy_palindrom(n):
      s = str(n)
      return s == s[::-1]

Test:
  print(czy_palindrom(121))    → True
  print(czy_palindrom(1331))   → True
  print(czy_palindrom(12321))  → True
  print(czy_palindrom(123))    → False
  print(czy_palindrom(10))     → False
  print(czy_palindrom(5))      → True (jednocyfrowe to palindromy)
""")
# Twój kod:




# ===========================================================
# KONIEC ĆWICZEŃ
# ===========================================================

print("\n" + "="*60)
print("KONIEC ĆWICZEŃ LAB 2")
print("="*60)

print("\n💾 PAMIĘTAJ:")
print("  1. Zapisz swój kod (Ctrl+A, Ctrl+C)")
print("  2. Wklej do pliku .py")
print("  3. Wyślij na: bartekel@gmail.com")
print("  4. Temat: '[Grupa] Lab2 - Imię Nazwisko'")
print("  5. Deadline: [WPISZ DATĘ]")

print("\n📊 PODSUMOWANIE PUNKTOWE:")
print("  Policz swoje punkty i sprawdź ocenę:")
print("  • 10-14 pkt → 3.0")
print("  • 15-19 pkt → 3.5")
print("  • 20-25 pkt → 4.0")
print("  • 26-31 pkt → 4.5")
print("  • 32+ pkt   → 5.0")

print("\n✨ Świetna robota!")

# ===========================================================
# WSKAZÓWKI - PRZYPOMNIENIE
# ===========================================================
#
# PĘTLE:
# for i in range(1, 11):      # 1 do 10
#     print(i)
#
# for element in lista:       # każdy element
#     print(element)
#
# while warunek:              # dopóki prawda
#     # kod
#     # pamiętaj zmienić warunek!
#
# FUNKCJE:
# def nazwa_funkcji(parametr1, parametr2):
#     # kod
#     return wynik
#
# TABLICE/LISTY:
# lista = [1, 2, 3, 4, 5]
# lista.append(6)             # dodaj na koniec
# len(lista)                  # długość
# lista[0]                    # pierwszy element
# lista[-1]                   # ostatni element
# element in lista            # sprawdź czy jest
#
# CASE/MATCH (Python 3.10+):
# match zmienna:
#     case 'a':
#         # kod
#     case 'b':
#         # kod
#     case _:
#         # default
#
# LUB if-elif-else:
# if zmienna == 'a':
#     # kod
# elif zmienna == 'b':
#     # kod
# else:
#     # kod
#
# ===========================================================