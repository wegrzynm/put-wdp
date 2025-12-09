🔥 Część 1: Rozgrzewka (3 zadania = 3 punkty)
Krótkie zadania na rozgrzewkę - przypomnienie pętli i funkcji.

Zadanie 1: Suma liczb (1 pkt)
Napisz funkcję suma_liczb(n), która zwraca sumę liczb od 1 do n (włącznie).

Przykład:

print(suma_liczb(5))   # 15 (bo 1+2+3+4+5)
print(suma_liczb(10))  # 55
print(suma_liczb(100)) # 5050
Wskazówka: Użyj pętli for z range().

Zadanie 2: Maksimum z listy (1 pkt)
Napisz funkcję znajdz_max(lista), która zwraca największą wartość z listy.

⚠️ WAŻNE: NIE używaj wbudowanej funkcji max() - napisz własną!

Przykład:

print(znajdz_max([3, 7, 2, 9, 1]))      # 9
print(znajdz_max([-5, -2, -10, -1]))    # -1
print(znajdz_max([42]))                  # 42
Wskazówka: Rozpocznij od maks = lista[0], potem pętla.

Zadanie 3: Suma do zera (1 pkt)
Napisz program, który:

Czyta liczby od użytkownika (po jednej w linii)
Sumuje je
Kończy, gdy użytkownik wpisze 0
Wypisuje sumę (bez dodawania zera!)
Przykład:

Podaj liczbę: 5
Podaj liczbę: 10
Podaj liczbę: 3
Podaj liczbę: 0
Suma: 18
Wskazówka: Użyj pętli while True i break.

💡 Część 2: Float vs Int - podstawy (7 zadań = 13 punktów)
🎯 MINIMUM DO ZALICZENIA: Zadania 1-9 (łącznie 8-10 punktów wystarczy na 3.0)

Zadanie 4: Dzielenie - float vs int (1 pkt)
Napisz funkcję porownaj_dzielenie(a, b), która:

Oblicza a / b (dzielenie float)
Oblicza a // b (dzielenie całkowite)
Wypisuje oba wyniki z opisem
Przykład:

porownaj_dzielenie(10, 4)
# Wynik:
# Float: 10 / 4 = 2.5
# Int: 10 // 4 = 2

porownaj_dzielenie(7, 3)
# Wynik:
# Float: 7 / 3 = 2.3333333333333335
# Int: 7 // 3 = 2
Zadanie 5: Pułapka 0.3 (2 pkt)
Napisz program, który:

Oblicza wynik = 0.1 + 0.2
Sprawdza, czy wynik == 0.3 (używając ==)
Wypisuje wynik z dużą precyzją (20 miejsc po przecinku)
Wypisuje, czy test == dał True czy False
Wyjaśnia w komentarzu, dlaczego tak się stało
Przykład wyjścia:

0.1 + 0.2 = 0.30000000000000004441
Czy równe 0.3? False
W kodzie dodaj komentarz:

# WYJAŚNIENIE:
# Wynik jest False, ponieważ... [TWOJE WYJAŚNIENIE]
Wskazówka: Użyj print(f"{wynik:.20f}") do wypisania z precyzją.

Zadanie 6: Funkcja is_close (2 pkt)
Zaimplementuj funkcję is_close(a, b, epsilon=1e-10), która:

Zwraca True jeśli |a - b| < epsilon
Zwraca False w przeciwnym razie
Następnie przetestuj ją na przykładach:

print(is_close(0.1 + 0.2, 0.3))           # True
print(is_close(0.1 + 0.2, 0.3, 1e-20))    # False (zbyt mały epsilon)
print(is_close(1.0, 1.0000001, 1e-5))     # True
print(is_close(1.0, 1.1, 1e-5))           # False
Pytanie do przemyślenia: Dlaczego dla epsilon=1e-20 wynik jest False?

Zadanie 7: Notacja naukowa - kalkulator (2 pkt)
Napisz funkcję oblicz_naukowa(a_mantissa, a_exp, b_mantissa, b_exp, operacja), która:

Przyjmuje dwie liczby w notacji naukowej: a = a_mantissa × 10^a_exp
Wykonuje operację: "*" (mnożenie) lub "/" (dzielenie)
Zwraca wynik jako krotkę (mantissa, exponent)
Przykład:

# (3 × 10^4) * (2 × 10^3) = 6 × 10^7
print(oblicz_naukowa(3, 4, 2, 3, "*"))  # (6, 7) lub (6.0, 7)

# (8 × 10^6) / (2 × 10^3) = 4 × 10^3
print(oblicz_naukowa(8, 6, 2, 3, "/"))  # (4, 3) lub (4.0, 3)
Wskazówka:

Mnożenie: (a × 10^x) * (b × 10^y) = (a*b) × 10^(x+y)
Dzielenie: (a × 10^x) / (b × 10^y) = (a/b) × 10^(x-y)
Zadanie 8: Hipotenuza - metoda zła (1 pkt)
Zaimplementuj funkcję hipotenuza_zla(a, b, c), która oblicza:

wynik = c × √(a² + b²)
Dokładnie w tej kolejności (najpierw a², potem b², potem suma, potem √, na końcu × c).

Przykład:

import math

# Test 1 - normalne liczby
print(hipotenuza_zla(3, 4, 1))  # Powinno: 5.0

# Test 2 - skrajne liczby (z wykładu!)
print(hipotenuza_zla(3e-200, 4e-200, 1e200))  # Co dostaniesz?
Zapisz wyniki testów w komentarzu!

Zadanie 9: Hipotenuza - metoda dobra (2 pkt)
Zaimplementuj funkcję hipotenuza_dobra(a, b, c), która oblicza:

wynik = c × a × √(1 + (b/a)²)
⚠️ UWAGA: Bardzo ważne są nawiasy! (b/a)*(b/a) nie b/a*b/a!

Przykład:

import math

# Test 1 - normalne liczby
print(hipotenuza_dobra(3, 4, 1))  # Powinno: 5.0

# Test 2 - skrajne liczby
print(hipotenuza_dobra(3e-200, 4e-200, 1e200))  # Co dostaniesz?
Pytanie: Porównaj wyniki z Zadaniem 8. Która metoda dała poprawny wynik dla skrajnych liczb?

Zadanie 10: Porównanie metod (2 pkt)
Napisz funkcję testuj_metody(), która:

Testuje obie metody (złą i dobrą) dla różnych zestawów danych
Oblicza błąd bezwzględny: |wynik - oczekiwany|
Wypisuje wyniki w czytelnej tabeli
Zestawy testowe:

# (a, b, c, oczekiwany_wynik)
testy = [
    (3, 4, 1, 5.0),                      # Normalne
    (5, 12, 1, 13.0),                    # Normalne
    (3e-200, 4e-200, 1e200, 5.0),       # Skrajne - małe a,b
    (3e-100, 4e-100, 1e100, 5.0),       # Skrajne - średnie
]
Przykładowe wyjście:

Test | a       | b       | c     | Oczekiwane | Zła    | Błąd  | Dobra  | Błąd
-----|---------|---------|-------|------------|--------|-------|--------|-------
1    | 3       | 4       | 1     | 5.0        | 5.0    | 0.0   | 5.0    | 0.0
2    | 5       | 12      | 1     | 13.0       | 13.0   | 0.0   | 13.0   | 0.0
3    | 3e-200  | 4e-200  | 1e200 | 5.0        | 0.0    | 5.0   | 5.0    | 0.0
4    | 3e-100  | 4e-100  | 1e100 | 5.0        | 0.0    | 5.0   | 5.0    | 0.0
⭐ Część 3: Metody numeryczne - ROZSZERZONE (5 zadań = 11 punktów)
Zadania dla ambitnych - wyższa ocena!

Zadanie 11: √2 metodą Newtona (2 pkt)
Metoda Newtona to iteracyjny sposób znajdowania pierwiastka.

Dla √x:

początkowe_zgadnięcie = x / 2
dopóki |zgadnięcie² - x| > epsilon:
    zgadnięcie = (zgadnięcie + x/zgadnięcie) / 2
Zaimplementuj funkcję sqrt_newton(x, epsilon=1e-6), która:

Oblicza √x metodą Newtona
Kończy, gdy dokładność jest lepsza niż epsilon
Zwraca wynik i liczbę wykonanych iteracji
Przykład:

wynik, iteracje = sqrt_newton(2, 1e-6)
print(f"√2 ≈ {wynik}, iteracji: {iteracje}")
# Powinno: √2 ≈ 1.41421356..., iteracji: 4-5

wynik, iteracje = sqrt_newton(2, 1e-12)
print(f"√2 ≈ {wynik}, iteracji: {iteracje}")
# Większa dokładność = więcej iteracji
Porównaj z wbudowanym math.sqrt(2) - jaki masz błąd?

Zadanie 12: Szereg geometryczny (2 pkt)
Chcemy obliczyć sumę nieskończonego szeregu geometrycznego:

S = 1 + 1/2 + 1/4 + 1/8 + 1/16 + ...
S = Σ(1/2^n) dla n=0,1,2,...
Matematycznie: S = 2

Napisz funkcję szereg_geometryczny(epsilon=1e-6), która:

Sumuje wyrazy szeregu, dopóki kolejny wyraz > epsilon
Zwraca sumę i liczbę zsumowanych wyrazów
Przykład:

suma, wyrazy = szereg_geometryczny(1e-6)
print(f"Suma ≈ {suma}, wyrazów: {wyrazy}")
# Powinno: Suma ≈ 1.999999..., wyrazów: ~20

suma, wyrazy = szereg_geometryczny(1e-10)
print(f"Suma ≈ {suma}, wyrazów: {wyrazy}")
# Większa dokładność = więcej wyrazów
Pytanie: Jak zmienia się liczba wyrazów w zależności od epsilon?

Zadanie 13: Machine epsilon (3 pkt)
Machine epsilon to najmniejsza liczba eps, dla której 1.0 + eps > 1.0 (na komputerze!).

Napisz funkcję znajdz_machine_epsilon(), która:

Zaczyna od eps = 1.0
W pętli dzieli eps przez 2
Sprawdza, czy 1.0 + eps > 1.0
Kończy, gdy warunek przestaje być spełniony
Zwraca ostatnie eps, dla którego warunek był True
Przykład:

eps = znajdz_machine_epsilon()
print(f"Machine epsilon: {eps}")
print(f"1.0 + eps = {1.0 + eps}")
print(f"1.0 + eps/2 = {1.0 + eps/2}")
Pytanie do przemyślenia:

Dlaczego 1.0 + bardzo_mała_liczba może dać 1.0?
Jaki jest machine epsilon w Pythonie (float64)?
Wskazówka: Powinno wyjść około 2.22e-16 (dla float64).

Zadanie 14: Problem modulo (2 pkt)
Z wykładu profesora Nawrockiego:

"Jaka jest reszta z dzielenia liczby 20-cyfrowej
20202020202020202020 przez 808?"

Napisz funkcję wielkie_modulo(), która:

Oblicza 20202020202020202020 % 808 w Pythonie
Wypisuje wynik
Bonus (+1 pkt): Wyjaśnij w komentarzu, jak by to zrobić w C (gdzie int ma 32/64 bity)?
Przykład:

wynik = wielkie_modulo()
print(f"Reszta z dzielenia: {wynik}")
Hint z wykładu:

W Pythonie: po prostu użyj % (Python ma arbitrary precision integers!)
W C: trzeba rozbić na części i użyć właściwości: (a*b) mod n = ((a mod n) * (b mod n)) mod n
Zadanie 15: Obliczanie π - CHALLENGE (2 pkt)
Oblicz π używając szeregu Leibniza:

π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...
π/4 = Σ((-1)^n / (2n+1)) dla n=0,1,2,...
Napisz funkcję oblicz_pi(epsilon=1e-6), która:

Sumuje wyrazy szeregu, dopóki |kolejny_wyraz| > epsilon
Zwraca obliczone π i liczbę wyrazów
Bonus (+0.5 pkt): Oblicza błąd względem math.pi
Przykład:

pi_approx, wyrazy = oblicz_pi(1e-6)
print(f"π ≈ {pi_approx}, wyrazów: {wyrazy}")
print(f"math.pi = {math.pi}")
print(f"Błąd: {abs(pi_approx - math.pi)}")
Uwaga: Ten szereg zbiega bardzo wolno! Dla epsilon=1e-6 może potrzeba ~miliona wyrazów.

Pytanie bonusowe (+0.5 pkt): Czy da się to przyspieszyć? (Google: "Machin's formula")

📊 System punktowy
Punktacja:
Grupa	Zadania	Punkty
Rozgrzewka	1-3	3
Podstawowe	4-10	13
Rozszerzone	11-15	11
SUMA		27
Skala ocen:
Punkty	Ocena
8-10	3.0
11-13	3.5
14-16	4.0
17-20	4.5
21-27	5.0
✅ Minimum do zaliczenia (3.0): 8-10 punktów
Realistyczny plan na 3.0:

Zadania 1-3 (rozgrzewka): 3 pkt
Zadania 4-6 (float basics): 5 pkt
Zadanie 8 lub 9 (hipotenuza): 1-2 pkt
Razem: 9-10 punktów = 3.0 ✅

💡 Wskazówki
Ogólne:
Testuj skrajne przypadki - bardzo małe i bardzo duże liczby
Używaj epsilon do porównywania floatów, nigdy ==
Notacja naukowa to Twój przyjaciel dla ekstremalnych wartości
Komentuj kod - wyjaśniaj, dlaczego coś robisz
Debugowanie:
# Jeśli nie działa, wypisuj pośrednie kroki:
print(f"Debug: a={a}, b={b}, a*a={a*a}, b*b={b*b}")
print(f"Debug: suma={a*a + b*b}, sqrt={math.sqrt(a*a + b*b)}")
Typowe błędy:
❌ Używanie == dla floatów
❌ Zapomnienie import math
❌ Dzielenie przez zero
❌ Złe nawiasy w wzorach matematycznych: b/a*b/a zamiast (b/a)*(b/a)
Jeśli coś nie wychodzi:
Sprawdź na prostym przykładzie (np. a=3, b=4, c=1)
Wypisz wszystkie pośrednie kroki
Porównaj z wzorem matematycznym
Zapytaj prowadzącego! (podnieś rękę)
📝 Oddawanie zadań
Format: Jeden plik .py z wszystkimi rozwiązaniami, nazwany:

lab6_imie_nazwisko.py
Struktura pliku:

"""
Laboratorium 6: Metody numeryczne
Autor: Jan Kowalski
Grupa: 1
"""

import math

# ==== ZADANIE 1 ====
def suma_liczb(n):
    # TODO
    pass

# ==== ZADANIE 2 ====
def znajdz_max(lista):
    # TODO
    pass

# ... itd ...
Deadline: [Data do ustalenia przez prowadzącego]

Gdzie oddać: [Metoda oddania - email? USB? Moodle?]