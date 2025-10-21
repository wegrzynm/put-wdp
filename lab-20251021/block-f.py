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

print(liczby_pierwsze(20))
print(liczby_pierwsze(10))
print(liczby_pierwsze(2))

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
def fizzbuzz(n):
    strList = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            strList.append('FizzBuzz')
        elif i % 3 == 0:
            strList.append('Fizz')
        elif i % 5 == 0:
            strList.append('Buzz')
        else:
            strList.append(str(i))
    return strList
print(fizzbuzz(15))


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
def czy_palindrom(n):
    s = str(n)
    return s == s[::-1]
def czy_palindrom_normal(n):
    oryginalna = n
    odwrocona = 0
    while n > 0:
        cyfra = n % 10
        odwrocona = odwrocona * 10 + cyfra
        n = n // 10
    return oryginalna == odwrocona

print(czy_palindrom_normal(121))
print(czy_palindrom_normal(1331))
print(czy_palindrom_normal(12321))
print(czy_palindrom_normal(123))
print(czy_palindrom_normal(10))
print(czy_palindrom_normal(5))