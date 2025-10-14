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
def czy_poprawny_pesel(pesel):
    if len(pesel) != 11:
        return False

    if not pesel.isdigit():
        return False

    # Sprawdź sumę kontrolną
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    i = 0
    suma_kontrolna = 0
    for i in range(10):
        suma_kontrolna += int(pesel[i]) * wagi[i]
    reszta = suma_kontrolna % 10
    obliczona_kontrolna = (10 - reszta) % 10
    return obliczona_kontrolna == int(pesel[10])

pesel = "44051401458"
print(f"Czy poprawny PESEL: {pesel}?, {czy_poprawny_pesel(pesel=pesel)}")
