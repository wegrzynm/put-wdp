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
n = 5
for i in range(n):
    print(i+1)



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
n = 10
suma = 0
i = 1
while (i <= n):
    suma += i
    i += 1
print(suma)


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
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in lista:
    if i % 2 == 0:
        print(i)


