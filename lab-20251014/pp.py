
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
wiek = 20 

if wiek >= 18:
    print("Pełnoletni")
else:
    print("Niepełnoletni")

# [2] 2 pkt - ZADANIE: Rabat w sklepie
print("\n[2] 2 pkt - Rabat w sklepie")
# Sklep daje 10% rabatu jeśli zakupy > 100 zł
# Wejście: kwota_zakupow
# Wyświetl końcową kwotę (z rabatem lub bez)
# Twój kod:
kwota_zakupow = 150  # przykładowa kwota

if kwota_zakupow > 100:
    rabat = kwota_zakupow * 0.1
    kwota_finalna = kwota_zakupow - rabat
    print(f"Kwota z rabatem 10%: {kwota_finalna} zł")
else:
    print(f"Kwota bez rabatu: {kwota_zakupow} zł")




# [3] 2 pkt - ZADANIE: Kalkulator BMI z oceną
print("\n[3] 2 pkt - Kalkulator BMI")
# Wejście: waga (kg), wzrost (m)
# Wzór: BMI = waga / (wzrost ** 2)
# Kategorie: <18.5: Niedowaga, 18.5-25: Prawidłowa, >=25: Nadwaga
# Twój kod:
waga = 70
wzrost = 1.75 

bmi = waga / (wzrost ** 2)
print(f"BMI: {bmi:.2f}")

if bmi < 18.5:
    print("Kategoria: Niedowaga")
elif bmi >= 18.5 and bmi < 25:
    print("Kategoria: Prawidłowa")
else:
    print("Kategoria: Nadwaga")




print("\n" + "="*60)
print("✅ MINIMUM ZALICZONE!")
print("Jeśli zrobiłeś/aś R1-R5 i 1-3, masz 11 punktów = 3.0")
print("")
print("Chcesz wyższej oceny? Wybierz zadania poniżej! ⬇️")
print("="*60)
