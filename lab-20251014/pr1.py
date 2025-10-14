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
password = "1tS02DF5*6-["
if len(password) >= 10:
    print("bezpieczne")
elif len(password) > 5 and len(password) < 10:
    print("średnio bezpieczne")
else:
    print("niebezpieczne")



# [5] 3 pkt - Kalkulator opłaty za prąd
print("\n[5] 3 pkt - Kalkulator opłaty za prąd")
# Wejście: zuzycie_kwh
# Stawki: <=100 kWh: 0.50 zł/kWh, >100: 0.70 zł/kWh
# Twój kod:
zuzycie_kwh = int(input("Podaj swoje zuzycie kWh: ",))
if zuzycie_kwh > 100:
    print(f"{zuzycie_kwh * 0.7}")
else:
    print(f"{zuzycie_kwh * 0.5}")



# [6] 3 pkt - Kalkulator podatku
print("\n[6] 3 pkt - Kalkulator podatku")
# Wejście: roczny_dochod
# Progi: <=20k: 0%, 20-50k: 15%, >50k: 30%
# Wyświetl: brutto, podatek, netto
# Twój kod:
roczny_dochod = float(input("Podaj swój roczny dochód: ",))
brutto = 0.0
netto = 0.0
podatek = 0.0
if roczny_dochod <= 20000:
    brutto = roczny_dochod
    netto = roczny_dochod
elif roczny_dochod > 20000 and roczny_dochod <= 50000:
    brutto = roczny_dochod
    netto = roczny_dochod/1.15
    podatek = brutto - netto
else:
    brutto = roczny_dochod
    netto = roczny_dochod/1.3
    podatek = brutto - netto
print(f"Netto: {format(netto, '.2f')}, Brutto: {format(brutto, '.2f')}, Podatek: {format(podatek, '.2f')}")



# [7] 3 pkt - Sprawdzanie trójkąta
print("\n[7] 3 pkt - Sprawdzanie trójkąta")
# Wejście: a, b, c (długości boków)
# Sprawdź: czy może być trójkąt + jaki typ (równoboczny/równoramienny/różnoboczny)
# Twój kod:
a = int(input())
b = int(input())
c = int(input())

# Sprawdzenie czy może być trójkąt (nierówność trójkąta)
if a + b > c and a + c > b and b + c > a:
    print("To może być trójkąt")
    
    # Sprawdzenie typu trójkąta
    if a == b == c:
        print("Typ: równoboczny")
    elif a == b or b == c or a == c:
        print("Typ: równoramienny")
    else:
        print("Typ: różnoboczny")
else:
    print("To nie może być trójkąt")



# [8] 3 pkt - Konwerter temperatur z walidacją
print("\n[8] 3 pkt - Konwerter temperatur")
# Wejście: temperatura, kierunek ("C->F" lub "F->C")
# Walidacja: zero absolutne, poprawny kierunek
# Twój kod:
temperatura = int(input("Podaj temperature: ",))
kierunek = input("Podaj kierunek: ",)

if kierunek not in ["C->F", "F->C"]:
    print("Błąd: Niepoprawny kierunek konwersji!")
else:
    if kierunek == "C->F":
        if temperatura < -273.15:
            print("Błąd: Temperatura poniżej zera absolutnego!")
        else:
            fahrenheit = (temperatura * 9/5) + 32
            print(f"{temperatura}°C = {format(fahrenheit, ".2f")}°F")
    
    elif kierunek == "F->C":
        if temperatura < -459.67:
            print("Błąd: Temperatura poniżej zera absolutnego!")
        else:
            celsius = (temperatura - 32) * 5/9
            print(f"{temperatura}°F = {format(celsius, ".2f")}°C")




# [9] 3 pkt - System zniżek lojalnościowych
print("\n[9] 3 pkt - System zniżek lojalnościowych")
# Wejście: kwota_zakupow, typ_karty
# Zniżki: brak/brazowa/srebrna/zlota/platynowa
# Dodatkowe 5% jeśli kwota >1000
# Twój kod:
kwota_zakupow = float(input("Podaj kwote zakupow: ",))
typ_karty = input("Podaj swoj typ karty: ")
rabat = 0.0
if typ_karty == "brazowa":
    rabat = 0.05
elif typ_karty == "srebrna":
    rabat = 0.1
elif typ_karty == "zlota":
    rabat = 0.15
elif typ_karty == "platynowa":
    rabat = 0.2
else:
    rabat = 0.0

if kwota_zakupow > 1000:
    rabat += 0.05

print(f"Kwota początkowa: {kwota_zakupow}, Kwota koncowa: {format(kwota_zakupow * (1-rabat), ".2f")}")