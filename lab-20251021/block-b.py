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
def pole_prostokata(a,b):
    return a*b

print(pole_prostokata(5, 3))   # → 15
print(pole_prostokata(10, 2))  # → 20


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
def czy_parzysta(n):
    return n % 2 == 0

print(czy_parzysta(4))   # → True
print(czy_parzysta(7))   # → False
print(czy_parzysta(0))   # → True