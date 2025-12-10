"""
Część 2: Float vs Int - podstawy
Zadania 4-10
"""

import math

# ==== ZADANIE 4: Dzielenie float vs int ====
def porownaj_dzielenie(a, b):
    div_float = a / b
    div_int = a // b
    print(f"Dane: {a}, {b}")
    print(f"Float: {a} / {b} = {div_float}")
    print(f"Int: {a} // {b} = {div_int}")
    print()

# ==== ZADANIE 5: Pułapka 0.3 ====
def pulapka_0_3():
    wynik = 0.1 + 0.2
    jest_rowne = (wynik == 0.3)
    
    print(f"0.1 + 0.2 = {wynik:.20f}")
    print(f"Czy równe 0.3? {jest_rowne}")
    
    # Wynik jest False, ponieważ liczby zmiennoprzecinkowe (float) w komputerze są reprezentowane
    print("# Patrz komentarz w kodzie z wyjaśnieniem.")

# ==== ZADANIE 6: Funkcja is_close ====
def is_close(a, b, epsilon=1e-10):
    return abs(a - b) < epsilon

# ==== ZADANIE 7: Notacja naukowa ====
def oblicz_naukowa(a_mantissa, a_exp, b_mantissa, b_exp, operacja):
    """
    Wykonuje operację na liczbach w notacji naukowej.
    a = a_mantissa * 10^a_exp
    b = b_mantissa * 10^b_exp
    Zwraca krotkę (wynik_mantissa, wynik_exp)
    """
    if operacja == "*":
        # (a * 10^x) * (b * 10^y) = (a*b) * 10^(x+y)
        new_mantissa = a_mantissa * b_mantissa
        new_exp = a_exp + b_exp
        return (new_mantissa, new_exp)
    elif operacja == "/":
        # (a * 10^x) / (b * 10^y) = (a/b) * 10^(x-y)
        new_mantissa = a_mantissa / b_mantissa
        new_exp = a_exp - b_exp
        return (new_mantissa, new_exp)
    else:
        raise ValueError("Nieznana operacja")

# ==== ZADANIE 8: Hipotenuza - metoda zła ====
def hipotenuza_zla(a, b, c):
    return c * math.sqrt(a**2 + b**2)

# ==== ZADANIE 9: Hipotenuza - metoda dobra ====
def hipotenuza_dobra(a, b, c):
    return c * a * math.sqrt(1 + (b/a)**2)

# ==== ZADANIE 10: Porównanie metod ====
def testuj_metody():
    testy = [
        (3, 4, 1, 5.0),                      # Normalne
        (5, 12, 1, 13.0),                    # Normalne
        (3e-200, 4e-200, 1e200, 5.0),       # Skrajne - małe a,b (underflow w a^2)
        (3e-100, 4e-100, 1e100, 5.0),       # Skrajne - średnie
    ]
    
    print(f"{'Test':<5} | {'a':<10} | {'b':<10} | {'c':<8} | {'Oczekiwane':<10} | {'Zła':<10} | {'Błąd':<8} | {'Dobra':<10} | {'Błąd':<8}")
    print("-" * 100)
    
    for i, (a, b, c, oczekiwany) in enumerate(testy, 1):
        try:
            wynik_zla = hipotenuza_zla(a, b, c)
            blad_zla = abs(wynik_zla - oczekiwany)
        except Exception as e:
            wynik_zla = "ERROR"
            blad_zla = "N/A"
            
        try:
            wynik_dobra = hipotenuza_dobra(a, b, c)
            blad_dobra = abs(wynik_dobra - oczekiwany)
        except Exception as e:
            wynik_dobra = "ERROR"
            blad_dobra = "N/A"

        def fmt(val):
            if isinstance(val, (int, float)):
                return f"{val:.4g}"
            return str(val)

        print(f"{i:<5} | {fmt(a):<10} | {fmt(b):<10} | {fmt(c):<8} | {fmt(oczekiwany):<10} | {fmt(wynik_zla):<10} | {fmt(blad_zla):<8} | {fmt(wynik_dobra):<10} | {fmt(blad_dobra):<8}")

if __name__ == "__main__":
    print("=== CZĘŚĆ 2: FLOAT VS INT ===\n")
    
    print("--- Zadanie 4 ---")
    porownaj_dzielenie(10, 4)
    porownaj_dzielenie(7, 3)
    
    print("--- Zadanie 5 ---")
    pulapka_0_3()
    print()
    
    print("--- Zadanie 6 ---")
    print(f"is_close(0.1 + 0.2, 0.3) -> {is_close(0.1 + 0.2, 0.3)}")
    print(f"is_close(0.1 + 0.2, 0.3, 1e-20) -> {is_close(0.1 + 0.2, 0.3, 1e-20)}")
    print(f"is_close(1.0, 1.0000001, 1e-5) -> {is_close(1.0, 1.0000001, 1e-5)}")
    print()
    
    print("--- Zadanie 7 ---")
    # (3 x 10^4) * (2 x 10^3) = 6 x 10^7
    print(f"Mnożenie (3,4) * (2,3): {oblicz_naukowa(3, 4, 2, 3, '*')}")
    # (8 x 10^6) / (2 x 10^3) = 4 x 10^3
    print(f"Dzielenie (8,6) / (2,3): {oblicz_naukowa(8, 6, 2, 3, '/')}")
    print()
    
    print("--- Zadanie 8 i 9 (Testy ręczne) ---")
    print(f"Zła (3,4,1): {hipotenuza_zla(3, 4, 1)}")
    print(f"Dobra (3,4,1): {hipotenuza_dobra(3, 4, 1)}")
    print(f"Zła skrajne: {hipotenuza_zla(3e-200, 4e-200, 1e200)}")
    print(f"Dobra skrajne: {hipotenuza_dobra(3e-200, 4e-200, 1e200)}")
    print() # Zła metoda powinna dać 0.0, bo (3e-200)^2 to underflow do 0.0 w double.
    
    print("--- Zadanie 10: Tabela porównawcza ---")
    testuj_metody()
