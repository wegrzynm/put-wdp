# ===========================================================
# ĆWICZENIA: ZMIENNE, OPERACJE I INSTRUKCJE WARUNKOWE
# System oceniania: PUNKTOWY
# ===========================================================
# 
# Czas: 90 minut
# Zakres: Zmienne, typy danych, operacje, if-elif-else
# Narzędzie: https://programiz.com/python-programming/online-compiler  
#
# ===========================================================
# SYSTEM PUNKTOWY - ZASADY OCENIANIA
# ===========================================================
#
# Każde zadanie ma przypisaną WAGĘ PUNKTOWĄ:
#
# 📗 ROZGRZEWKA (R1-R5):           1 pkt każde
# 📘 PODSTAWOWE (1-3):              2 pkt każde
# 📙 STANDARDOWE ŚREDNIE (4-9):     3 pkt każde
# 📕 STANDARDOWE TRUDNE (10-14):    4 pkt każde
# 📓 STANDARDOWE B.TRUDNE (15-19):  5 pkt każde
# 🔥 ALGORYTMICZNE (A1-A5):         8 pkt każde
#
# MINIMUM DO ZALICZENIA (3.0) = 11 punktów:
#   R1-R5 (5×1=5) + zadania 1-3 (3×2=6) = 11 pkt
#
# SKALA OCEN:
#   11-15 pkt  → 3.0
#   16-20 pkt  → 3.5
#   21-27 pkt  → 4.0
#   28-35 pkt  → 4.5
#   36+ pkt    → 5.0
#
# STRATEGIE (przykłady):
#   • 3.5: minimum + 2 średnie (11+6=17)
#   • 4.0: minimum + 4 średnie (11+12=23)
#   • 4.0: minimum + 1 algorytmiczne + 1 średnie (11+8+3=22)
#   • 4.5: minimum + 2 algorytmiczne (11+16=27)
#   • 5.0: minimum + 3 algorytmiczne (11+24=35)
#
# NIE MUSISZ ROBIĆ WSZYSTKIEGO!
# Wybierz strategię pod swój poziom i cele.
#
# ===========================================================

print("="*60)
print("ĆWICZENIA: ZMIENNE, OPERACJE I IF-ELSE")
print("System punktowy")
print("="*60)

# ===========================================================
# POZIOM MINIMUM - ROZGRZEWKA (5 zadań × 1 pkt = 5 pkt)
# ===========================================================

print("\n" + "="*60)
print("### POZIOM MINIMUM - ROZGRZEWKA ###")
print("Zadania R1-R5 (wymagane do zaliczenia)")
print("Waga: 1 pkt każde | Razem: 5 pkt")
print("="*60 + "\n")

# [R1] 1 pkt - ZADANIE: Zmienne podstawowe
print("[R1] 1 pkt - Zmienne podstawowe")
# Zdefiniuj zmienne: imie (string), wiek (int), wzrost (float)
# Wyświetl je w formacie: "Imię: ..., Wiek: ..., Wzrost: ... cm"
# Twój kod:




# [R2] 1 pkt - ZADANIE: Proste obliczenia
print("\n[R2] 1 pkt - Proste obliczenia")
# Zdefiniuj cena = 19.99 i ilosc = 3
# Oblicz i wyświetl całkowitą wartość zakupu
# Twój kod:




# [R3] 1 pkt - ZADANIE: Sprawdzanie typu
print("\n[R3] 1 pkt - Sprawdzanie typu")
# Zdefiniuj zmienną x = "123"
# Wyświetl jej typ (type(x))
# Przekonwertuj na int i wyświetl ponownie typ
# Twój kod:




# [R4] 1 pkt - ZADANIE: Pierwszy if
print("\n[R4] 1 pkt - Pierwszy if")
# Zdefiniuj temperatura = 25
# Jeśli temperatura > 20, wyświetl "Ciepło"
# W przeciwnym razie wyświetl "Zimno"
# Twój kod:




# [R5] 1 pkt - ZADANIE: Prosty kalkulator
print("\n[R5] 1 pkt - Prosty kalkulator")
# Zdefiniuj a = 10, b = 3
# Oblicz i wyświetl: sumę, różnicę, iloczyn, iloraz
# Twój kod:





# ===========================================================
# POZIOM MINIMUM - PODSTAWOWE (3 zadania × 2 pkt = 6 pkt)
# ===========================================================

print("\n" + "="*60)
print("### POZIOM MINIMUM - PODSTAWOWE ###")
print("Zadania 1-3 (wymagane do zaliczenia)")
print("Waga: 2 pkt każde | Razem: 6 pkt")
print("="*60 + "\n")

# [1] 2 pkt - ZADANIE: Sprawdzanie pełnoletności
print("[1] 2 pkt - Sprawdzanie pełnoletności")
# Wejście: wiek (zdefiniuj zmienną)
# Warunki: wiek >= 18: "Pełnoletni", wiek < 18: "Niepełnoletni"
# Twój kod:




# [2] 2 pkt - ZADANIE: Rabat w sklepie
print("\n[2] 2 pkt - Rabat w sklepie")
# Sklep daje 10% rabatu jeśli zakupy > 100 zł
# Wejście: kwota_zakupow
# Wyświetl końcową kwotę (z rabatem lub bez)
# Twój kod:




# [3] 2 pkt - ZADANIE: Kalkulator BMI z oceną
print("\n[3] 2 pkt - Kalkulator BMI")
# Wejście: waga (kg), wzrost (m)
# Wzór: BMI = waga / (wzrost ** 2)
# Kategorie: <18.5: Niedowaga, 18.5-25: Prawidłowa, >=25: Nadwaga
# Twój kod:




print("\n" + "="*60)
print("✅ MINIMUM ZALICZONE!")
print("Jeśli zrobiłeś/aś R1-R5 i 1-3, masz 11 punktów = 3.0")
print("")
print("Chcesz wyższej oceny? Wybierz zadania poniżej! ⬇️")
print("="*60)


# ===========================================================
# POZIOM ROZSZERZONY - STANDARDOWE ŚREDNIE (6 zadań × 3 pkt)
# ===========================================================

print("\n" + "="*60)
print("### POZIOM ROZSZERZONY - STANDARDOWE ŚREDNIE ###")
print("Zadania 4-9 (opcjonalne)")
print("Waga: 3 pkt każde | Max: 18 pkt")
print("="*60 + "\n")

# [4] 3 pkt - Sprawdzanie hasła
print("[4] 3 pkt - Sprawdzanie hasła")
# Wejście: dlugosc_hasla
# <6: niebezpieczne, 6-9: średnio bezpieczne, >=10: bezpieczne
# Twój kod:




# [5] 3 pkt - Kalkulator opłaty za prąd
print("\n[5] 3 pkt - Kalkulator opłaty za prąd")
# Wejście: zuzycie_kwh
# Stawki: <=100 kWh: 0.50 zł/kWh, >100: 0.70 zł/kWh
# Twój kod:




# [6] 3 pkt - Kalkulator podatku
print("\n[6] 3 pkt - Kalkulator podatku")
# Wejście: roczny_dochod
# Progi: <=20k: 0%, 20-50k: 15%, >50k: 30%
# Wyświetl: brutto, podatek, netto
# Twój kod:




# [7] 3 pkt - Sprawdzanie trójkąta
print("\n[7] 3 pkt - Sprawdzanie trójkąta")
# Wejście: a, b, c (długości boków)
# Sprawdź: czy może być trójkąt + jaki typ (równoboczny/równoramienny/różnoboczny)
# Twój kod:




# [8] 3 pkt - Konwerter temperatur z walidacją
print("\n[8] 3 pkt - Konwerter temperatur")
# Wejście: temperatura, kierunek ("C->F" lub "F->C")
# Walidacja: zero absolutne, poprawny kierunek
# Twój kod:




# [9] 3 pkt - System zniżek lojalnościowych
print("\n[9] 3 pkt - System zniżek lojalnościowych")
# Wejście: kwota_zakupow, typ_karty
# Zniżki: brak/brazowa/srebrna/zlota/platynowa
# Dodatkowe 5% jeśli kwota >1000
# Twój kod:




# ===========================================================
# POZIOM ROZSZERZONY - STANDARDOWE TRUDNE (5 zadań × 4 pkt)
# ===========================================================

print("\n" + "="*60)
print("### POZIOM ROZSZERZONY - STANDARDOWE TRUDNE ###")
print("Zadania 10-14 (opcjonalne)")
print("Waga: 4 pkt każde | Max: 20 pkt")
print("="*60 + "\n")

# [10] 4 pkt - Kalkulator odsetek bankowych
print("[10] 4 pkt - Kalkulator odsetek bankowych")
# Zagnieżdżone if'y: kwota + okres → oprocentowanie
# Oblicz kapitał końcowy
# Twój kod:




# [11] 4 pkt - System oceny ryzyka kredytowego
print("\n[11] 4 pkt - System oceny ryzyka kredytowego")
# Wejście: dochod, kwota_kredytu, okres, ma_inne_kredyty
# Złożona logika oceny zdolności kredytowej
# Twój kod:




# [12] 4 pkt - Inteligentny termostat
print("\n[12] 4 pkt - Inteligentny termostat")
# Wejście: temp_aktualna, temp_zadana, pora_dnia, w_domu, tryb_eco
# Określ tolerancję i decyzję (ogrzewanie/chłodzenie/standby)
# Twój kod:




# [13] 4 pkt - System parkingowy
print("\n[13] 4 pkt - System parkingowy")
# Wejście: czas, typ_pojazdu, abonament, strefa
# Złożona logika: stawki, modyfikatory, pierwsze 15 min gratis
# Twój kod:




# [14] 4 pkt - Kalkulator składek ubezpieczenia
print("\n[14] 4 pkt - Kalkulator składek ubezpieczenia")
# Wejście: wiek, lata_prawa_jazdy, wypadki, typ_auta, przebieg
# Składka bazowa × mnożniki (wiele warunków)
# Twój kod:




# ===========================================================
# POZIOM ROZSZERZONY - BARDZO TRUDNE (5 zadań × 5 pkt)
# ===========================================================

print("\n" + "="*60)
print("### POZIOM ROZSZERZONY - BARDZO TRUDNE ###")
print("Zadania 15-19 (opcjonalne)")
print("Waga: 5 pkt każde | Max: 25 pkt")
print("="*60 + "\n")

# [15] 5 pkt - Symulator automatu biletowego
print("[15] 5 pkt - Symulator automatu biletowego")
# Wejście: typ_biletu, typ_pasazera, strefa, weekend
# Bardzo złożona logika cen i modyfikatorów
# Twój kod:




# [16] 5 pkt - System rekomendacji ubrań
print("\n[16] 5 pkt - System rekomendacji ubrań")
# Wejście: temperatura, pada, wietrznie, okazja, pora_roku
# Budowanie rekomendacji tekst + modyfikatory
# Twój kod:




# [17] 5 pkt - Kalkulator kalorii i makro
print("\n[17] 5 pkt - Kalkulator kalorii i makroskładników")
# Wejście: waga, wzrost, wiek, plec, aktywnosc, cel
# BMR, TDEE, rozkład makro
# Twój kod:




# [18] 5 pkt - System diagnostyki samochodu
print("\n[18] 5 pkt - System diagnostyki samochodu")
# Wejście: wiele parametrów (paliwo, temp, ciśnienie, itd)
# Priorytetyzacja ostrzeżeń: KRYTYCZNE/PILNE/OSTRZEŻENIE
# Twój kod:




# [19] 5 pkt - Symulator sklepu online
print("\n[19] 5 pkt - Symulator sklepu online")
# Wejście: cena, kod_rabatowy, dostawa, waga, prime, kraj
# Bardzo złożona logika rabatów i dostawy
# Twój kod:




# ===========================================================
# 🔥 ZADANIA ALGORYTMICZNE - WYZWANIE! (5 zadań × 8 pkt)
# ===========================================================

print("\n" + "="*60)
print("### 🔥 ZADANIA ALGORYTMICZNE - WYZWANIE! ###")
print("Zadania A1-A5 (opcjonalne)")
print("Waga: 8 pkt każde | Max: 40 pkt")
print("Wymagają wymyślenia algorytmu + implementacji")
print("="*60 + "\n")

# [A1] 8 pkt - Walidator numeru PESEL
print("[A1] 8 pkt - Walidator numeru PESEL")
print("""
Algorytm:
1. Wczytaj PESEL jako string (11 znaków)
2. Sprawdź czy tylko cyfry
3. Wagi: [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
4. Pomnóż każdą z pierwszych 10 cyfr przez odpowiednią wagę
5. Zsumuj wyniki
6. Reszta z dzielenia przez 10
7. Cyfra kontrolna = 10 - reszta (jeśli =10 to 0)
8. Porównaj z 11. cyfrą PESEL
9. Wyświetl: "PESEL poprawny" lub "PESEL niepoprawny"

Przykład: 44051401458
Wagi:      1,3,7,9,1,3,7,9,1,3
Mnożenie:  4,12,0,45,1,12,0,36,5,24
Suma:      139
Reszta:    139 % 10 = 9
Kontrolna: 10 - 9 = 1... ale nie 8! → NIEPOPRAWNY
""")
# Twój kod:




# [A2] 8 pkt - Problem wydawania reszty
print("\n[A2] 8 pkt - Problem wydawania reszty (algorytm zachłanny)")
print("""
Algorytm zachłanny:
1. Wczytaj kwotę reszty (int)
2. Nominały: [200, 100, 50, 20, 10, 5, 2, 1]
3. Dla każdego nominału (od największego):
   a) Oblicz ile sztuk: reszta // nominal
   b) Jeśli > 0: wyświetl "nominal zł: sztuk szt."
   c) Zaktualizuj resztę: reszta % nominal
4. Kontynuuj aż reszta = 0

Przykład: 138 zł
100 zł: 1 szt. (zostaje 38)
20 zł: 1 szt. (zostaje 18)
10 zł: 1 szt. (zostaje 8)
5 zł: 1 szt. (zostaje 3)
2 zł: 1 szt. (zostaje 1)
1 zł: 1 szt. (zostaje 0)
""")
# Twój kod:




# [A3] 8 pkt - Przecinanie się odcinków czasu
print("\n[A3] 8 pkt - Przecinanie się odcinków czasu")
print("""
Problem: Czy dwa spotkania kolidują?
Wejście: start1, koniec1, start2, koniec2 (godziny)

Trik: Łatwiej sprawdzić kiedy NIE ma kolizji!
Brak kolizji TYLKO gdy:
  (koniec1 <= start2) OR (koniec2 <= start1)
  
Jeśli NOT(brak kolizji) → jest kolizja

Przykład:
Spotkanie 1: 10-12
Spotkanie 2: 11-13
Czy koniec1 <= start2? 12 <= 11? NIE
Czy koniec2 <= start1? 13 <= 10? NIE
→ JEST KOLIZJA ✓

Spotkanie 1: 10-11
Spotkanie 2: 12-13
Czy koniec1 <= start2? 11 <= 12? TAK
→ BRAK KOLIZJI ✓
""")
# Twój kod:




# [A4] 8 pkt - Trójkąt w układzie współrzędnych
print("\n[A4] 8 pkt - Trójkąt w układzie współrzędnych")
print("""
Problem: Czy można zbudować trójkąt? Czy prostokątny?

Wejście: x_a, y_a, x_b, y_b, x_c, y_c

Krok 1: Sprawdź współliniowość
  Punkty NIE są współliniowe gdy:
  (y_b - y_a) * (x_c - x_b) != (y_c - y_b) * (x_b - x_a)
  
Krok 2: Jeśli współliniowe → "nie można zbudować trójkąta"

Krok 3: Oblicz kwadraty długości boków
  d_ab² = (x_b - x_a)² + (y_b - y_a)²
  d_bc² = (x_c - x_b)² + (y_c - y_b)²
  d_ac² = (x_c - x_a)² + (y_c - y_a)²
  
Krok 4: Sprawdź twierdzenie Pitagorasa
  Posortuj kwadraty: [a, b, c] gdzie a <= b <= c
  Jeśli a + b == c → prostokątny
  
Przykład:
A(0,0), B(3,0), C(0,4)
d_ab² = 9, d_bc² = 25, d_ac² = 16
9 + 16 = 25 ✓ → PROSTOKĄTNY
""")
# Twój kod:




# [A5] 8 pkt - Liczby Armstronga
print("\n[A5] 8 pkt - Liczby Armstronga (narcystyczne)")
print("""
Definicja: Liczba = suma cyfr podniesiona do potęgi = liczba cyfr

Dla 3-cyfrowych: n = c1³ + c2³ + c3³
Przykład: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✓

Algorytm:
1. Wczytaj liczbę
2. Sprawdź czy trzycyfrowa (100-999)
3. Wyodrębnij cyfry:
   cyfra_jednosci = liczba % 10
   cyfra_dziesiatek = (liczba // 10) % 10
   cyfra_setek = liczba // 100
4. Oblicz sumę sześcianów
5. Porównaj z oryginalną liczbą

Przykład: 370
Cyfry: 3, 7, 0
Suma: 3³ + 7³ + 0³ = 27 + 343 + 0 = 370 ✓
→ ARMSTRONG

Przykład: 123
Cyfry: 1, 2, 3
Suma: 1³ + 2³ + 3³ = 1 + 8 + 27 = 36 ≠ 123
→ NIE ARMSTRONG
""")
# Twój kod:




# ===========================================================
# KONIEC ĆWICZEŃ
# ===========================================================

print("\n" + "="*60)
print("KONIEC ĆWICZEŃ")
print("="*60)

print("\n💾 PAMIĘTAJ:")
print("  1. Zapisz swój kod (Ctrl+A, Ctrl+C)")
print("  2. Wklej do pliku .py")
print("  3. Wyślij na: bartekel@gmail.com")
print("  4. Temat: '[Grupa] Lab1 - Imię Nazwisko'")
print("  5. Deadline: [WPISZ DATĘ]")

print("\n📊 PODSUMOWANIE PUNKTOWE:")
print("  Policz swoje punkty i sprawdź ocenę:")
print("  • 11-15 pkt → 3.0")
print("  • 16-20 pkt → 3.5")
print("  • 21-27 pkt → 4.0")
print("  • 28-35 pkt → 4.5")
print("  • 36+ pkt   → 5.0")

print("\n✨ Świetna robota!")

# ===========================================================
# WSKAZÓWKI
# ===========================================================
#
# IF-ELIF-ELSE:
# if warunek1:
#     kod
# elif warunek2:
#     kod
# else:
#     kod
#
# OPERATORY:
# == != < > <= >=    (porównania)
# and or not         (logiczne)
# + - * / // % **    (matematyczne)
#
# KONWERSJE:
# int("123")   # string → int
# str(123)     # int → string
# float("3.14") # string → float
#
# WYODRĘBNIANIE CYFR:
# liczba = 153
# jednosci = liczba % 10        # 3
# dziesiatki = (liczba // 10) % 10  # 5
# setki = liczba // 100          # 1
#
# ===========================================================