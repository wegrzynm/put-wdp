"""
Część 3: Metody numeryczne - ROZSZERZONE
Zadania 11-15
"""

import math

# ==== ZADANIE 11: √2 metodą Newtona ====
def sqrt_newton(x, epsilon=1e-6):
    """
    Oblicza pierwiastek z x metodą Newtona.
    """
    if x < 0:
        raise ValueError("Nie można liczyć pierwiastka z liczby ujemnej")
    if x == 0:
        return 0, 0
        
    zgadniecie = x / 2.0
    iteracje = 0
    
    # Warunek stopu: |zgadnięcie^2 - x| <= epsilon
    while abs(zgadniecie**2 - x) > epsilon:
        zgadniecie = (zgadniecie + x / zgadniecie) / 2.0
        iteracje += 1
        
    return zgadniecie, iteracje

# ==== ZADANIE 12: Szereg geometryczny ====
def szereg_geometryczny(epsilon=1e-6):
    """
    Sumuje szereg 1 + 1/2 + 1/4... dopóki kolejny wyraz > epsilon.
    """
    suma = 0.0
    wyraz = 1.0
    liczba_wyrazow = 0
    
    while wyraz > epsilon:
        suma += wyraz
        wyraz /= 2.0
        liczba_wyrazow += 1
        
    return suma, liczba_wyrazow

# ==== ZADANIE 13: Machine epsilon ====
def znajdz_machine_epsilon():
    """
    Znajduje maszynowy epsilon.
    """
    eps = 1.0
    while (1.0 + eps / 2.0) > 1.0:
        eps /= 2.0
    return eps

# ==== ZADANIE 14: Problem modulo ====
def wielkie_modulo():
    """
    Oblicza 20202020202020202020 % 808.
    """
    liczba = 20202020202020202020
    dzielnik = 808
    return liczba % dzielnik

# ==== ZADANIE 15: Obliczanie PI (Leibniz) ====
def oblicz_pi(epsilon=1e-6):
    """
    Oblicza przybliżenie Pi z szeregu Leibniza.
    Pi/4 = 1 - 1/3 + 1/5 - 1/7 ...
    """
    suma = 0.0
    n = 0
    wyraz = 1.0
    
    while abs(wyraz) > epsilon:
        suma += wyraz
        n += 1
        mianownik = 2 * n + 1
        wyraz = ((-1)**n) / mianownik
        
    return suma * 4.0, n

if __name__ == "__main__":
    print("=== CZĘŚĆ 3: METODY NUMERYCZNE ===\n")

    # Zadanie 11
    print("--- Zadanie 11: √2 (Newton) ---")
    wynik, iteracje = sqrt_newton(2, 1e-6)
    print(f"√2 (eps=1e-6) ≈ {wynik}, iteracji: {iteracje}")
    print(f"Błąd bezwzględny: {abs(wynik - math.sqrt(2))}")
    
    wynik2, iteracje2 = sqrt_newton(2, 1e-12)
    print(f"√2 (eps=1e-12) ≈ {wynik2}, iteracji: {iteracje2}")
    print()

    # Zadanie 12
    print("--- Zadanie 12: Szereg geometryczny ---")
    suma_geo, wyrazy_geo = szereg_geometryczny(1e-6)
    print(f"Suma (eps=1e-6) ≈ {suma_geo}, wyrazów: {wyrazy_geo}")
    print(f"Oczekiwane: 2.0")
    print()

    # Zadanie 13
    print("--- Zadanie 13: Machine Epsilon ---")
    eps = znajdz_machine_epsilon()
    print(f"Obliczony epsilon: {eps}")
    print(f"1.0 + eps     = {1.0 + eps}")
    print(f"1.0 + eps/2   = {1.0 + eps/2}")
    print()

    # Zadanie 14
    print("--- Zadanie 14: Wielkie Modulo ---")
    reszta = wielkie_modulo()
    print(f"20202020202020202020 % 808 = {reszta}")
    print()

    # Zadanie 15
    print("--- Zadanie 15: Obliczanie PI ---")
    pi_approx, wyrazy_pi = oblicz_pi(1e-6)
    print(f"π (eps=1e-6) ≈ {pi_approx}")
    print(f"Liczba wyrazów: {wyrazy_pi}")
    print(f"math.pi      = {math.pi}")
    print(f"Błąd         = {abs(pi_approx - math.pi)}")
    print("Szereg zbiega bardzo wolno!")
