# ===========================================================
# POZIOM MINIMUM - ROZGRZEWKA (5 zadań × 1 pkt = 5 pkt)
# ===========================================================


# [R1] 1 pkt - ZADANIE: Zmienne podstawowe
print("[R1] 1 pkt - Zmienne podstawowe")
# Zdefiniuj zmienne: imie (string), wiek (int), wzrost (float)
# Wyświetl je w formacie: "Imię: ..., Wiek: ..., Wzrost: ... cm"
# Twój kod:
imie = "Mateusz"
wiek = 20
wzrost = 185.1
print(f"Imię: {imie}, Wiek: {wiek}, Wzrost: {wzrost} cm")

# [R2] 1 pkt - ZADANIE: Proste obliczenia
print("\n[R2] 1 pkt - Proste obliczenia")
# Zdefiniuj cena = 19.99 i ilosc = 3
# Oblicz i wyświetl całkowitą wartość zakupu
# Twój kod:
cena = 19.99
ilosc = 3
wartosc = cena * ilosc
print(f"Wartosc: {wartosc}")



# [R3] 1 pkt - ZADANIE: Sprawdzanie typu
print("\n[R3] 1 pkt - Sprawdzanie typu")
# Zdefiniuj zmienną x = "123"
# Wyświetl jej typ (type(x))
# Przekonwertuj na int i wyświetl ponownie typ
# Twój kod:
x = "123"
print(type(x))
x = int(x)
print(type(x))




# [R4] 1 pkt - ZADANIE: Pierwszy if
print("\n[R4] 1 pkt - Pierwszy if")
# Zdefiniuj temperatura = 25
# Jeśli temperatura > 20, wyświetl "Ciepło"
# W przeciwnym razie wyświetl "Zimno"
# Twój kod:
temperatura = 25
if temperatura > 20:
    print('cieplo')
else:
    print('zimno')


# [R5] 1 pkt - ZADANIE: Prosty kalkulator
print("\n[R5] 1 pkt - Prosty kalkulator")
# Zdefiniuj a = 10, b = 3
# Oblicz i wyświetl: sumę, różnicę, iloczyn, iloraz
# Twój kod:
a = 10
b = 3
print(f'Suma: {a+b}, różnica: {a-b}\n iloczyn: {a*b}, iloraz: {a/b}')


