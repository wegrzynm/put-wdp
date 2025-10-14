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
kwota = 10000
okres = 12 # w msc
oprocentowanie = 0.0
odsetki = 0.0
if kwota >= 10000:
    if okres >= 12:
        oprocentowanie = 0.04
    elif okres >= 6 and okres < 12:
        oprocentowanie = 0.03
    else:
        oprocentowanie = 0.02
else:
    if okres >= 12:
        oprocentowanie = 0.03
    elif okres >= 6 and okres < 12:
        oprocentowanie = 0.02
    else:
        oprocentowanie = 0.01
odsetki = kwota * oprocentowanie
k_koncowy = kwota + odsetki
print(f"Kapitał końcowy: {format(k_koncowy, ".2f")}")

# [11] 4 pkt - System oceny ryzyka kredytowego
print("\n[11] 4 pkt - System oceny ryzyka kredytowego")
# Wejście: dochod, kwota_kredytu, okres, ma_inne_kredyty
# Złożona logika oceny zdolności kredytowej
# Twój kod:
dochod = float(input("Podaj swoj dochod: "))
kwota_kredytu = float(input("Podaj kwote kredytu: "))
okres = float(input("Podaj okres trwania kredytu: "))
ma_inne_kredyty_str = input("Czy masz inne kredyty: ").lower()
ma_inne_kredyty = False
if ma_inne_kredyty_str not in ["tak", "nie"]:
    print("Błąd: Niepoprawna odpowiedz!")
else:
    if ma_inne_kredyty_str == "tak":
        ma_inne_kredyty = True
    else:
        ma_inne_kredyty = False

rata_miesieczna = kwota_kredytu / okres
if rata_miesieczna > 0.3 * dochod:
    decyzja = "Odmówiono: Rata przekracza 30% dochodu"
elif ma_inne_kredyty:
    decyzja = "Odmówiono: Posiada inne kredyty"
else:
    decyzja = "Zaakceptowano"
print(decyzja)


# [12] 4 pkt - Inteligentny termostat
print("\n[12] 4 pkt - Inteligentny termostat")
# Wejście: temp_aktualna, temp_zadana, pora_dnia, w_domu, tryb_eco
# Określ tolerancję i decyzję (ogrzewanie/chłodzenie/standby)
# Twój kod:
temp_aktualna = float(input("Podaj aktualną temperaturę: "))
temp_zadana = float(input("Podaj zadaną temperaturę: "))
pora_dnia = input("Pora dnia (dzień/noc): ").lower()
w_domu_str = input("Czy jesteś w domu (tak/nie): ").lower()
tryb_eco_str = input("Tryb eco (tak/nie): ").lower()
w_domu = w_domu_str == "tak"
tryb_eco = tryb_eco_str == "tak"
tolerancja = 5 if tryb_eco else 2
if temp_aktualna < temp_zadana - tolerancja:
    decyzja = "ogrzewanie"
elif temp_aktualna > temp_zadana + tolerancja:
    decyzja = "chłodzenie"
else:
    decyzja = "standby"
print(f"Decyzja: {decyzja}")




# [13] 4 pkt - System parkingowy
print("\n[13] 4 pkt - System parkingowy")
# Wejście: czas, typ_pojazdu, abonament, strefa
# Złożona logika: stawki, modyfikatory, pierwsze 15 min gratis
# Twój kod:
czas = float(input("Podaj czas parkowania w minutach: "))
typ_pojazdu = input("Typ pojazdu (samochód/motocykl): ").lower()
abonament_str = input("Czy masz abonament (tak/nie): ").lower()
strefa = input("Strefa (A/B/C): ").lower()
abonament = abonament_str == "tak"
stawka_podstawowa = 5  # zł/godz
if strefa == "A":
    stawka_podstawowa *= 1.5
elif strefa == "B":
    stawka_podstawowa *= 2
if typ_pojazdu == "motocykl":
    stawka_podstawowa *= 0.5
godziny = max(0, (czas - 15) / 60)  # pierwsze 15 min gratis
koszt = godziny * stawka_podstawowa
if abonament:
    koszt *= 0.8  # rabat 20%
print(f"Koszt parkowania: {format(koszt, '.2f')} zł")




# [14] 4 pkt - Kalkulator składek ubezpieczenia
print("\n[14] 4 pkt - Kalkulator składek ubezpieczenia")
# Wejście: wiek, lata_prawa_jazdy, wypadki, typ_auta, przebieg
# Składka bazowa × mnożniki (wiele warunków)
# Twój kod:
wiek = int(input("Podaj wiek: "))
lata_prawa_jazdy = int(input("Podaj lata posiadania prawa jazdy: "))
wypadki = int(input("Podaj liczbę wypadków: "))
typ_auta = input("Typ auta (osobowy/dostawczy): ").lower()
przebieg = int(input("Podaj przebieg w km: "))
skladka = 1000
if wiek < 25:
    skladka *= 1.5
elif wiek > 60:
    skladka *= 1.2
if lata_prawa_jazdy < 2:
    skladka *= 1.5
elif lata_prawa_jazdy > 10:
    skladka *= 0.8
if wypadki == 1:
    skladka *= 1.2
elif wypadki > 1:
    skladka *= 1.5
if typ_auta == "dostawczy":
    skladka *= 1.3
if przebieg > 100000:
    skladka *= 1.2
print(f"Składka ubezpieczenia: {format(skladka, '.2f')} zł")
