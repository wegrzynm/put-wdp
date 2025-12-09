"""
Część 1: Rozgrzewka
Zadania 1-3
"""

# ==== ZADANIE 1: Suma liczb ====
def suma_liczb(n):
    """
    Zwraca sumę liczb od 1 do n (włącznie).
    Wskazówka: Użyj pętli for z range().
    """
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

# ==== ZADANIE 2: Maksimum z listy ====
def znajdz_max(lista):
    """
    Zwraca największą wartość z listy bez użycia wbudowanej funkcji max().
    """
    if not lista:
        return None
    
    maks = lista[0]
    for element in lista[1:]:
        if element > maks:
            maks = element
    return maks

# ==== ZADANIE 3: Suma do zera ====
def suma_do_zera():
    """
    Czyta liczby od użytkownika, sumuje je i kończy gdy użytkownik wpisze 0.
    """
    print("--- Zadanie 3: Suma do zera ---")
    suma = 0
    while True:
        try:
            tekst = input("Podaj liczbę: ")
            liczba = int(tekst)
            
            if liczba == 0:
                break
                
            suma += liczba
        except ValueError:
            print("To nie jest poprawna liczba całkowita!")
            
    print(f"Suma: {suma}")

if __name__ == "__main__":
    print("=== CZĘŚĆ 1: ROZGRZEWKA ===\n")

    # Test Zadanie 1
    print("--- Zadanie 1: Suma liczb ---")
    vals = [5, 10, 100]
    for v in vals:
        print(f"suma_liczb({v}) = {suma_liczb(v)}")
    print()

    # Test Zadanie 2
    print("--- Zadanie 2: Maksimum z listy ---")
    lists = [
        [3, 7, 2, 9, 1],
        [-5, -2, -10, -1],
        [42]
    ]
    for lst in lists:
        print(f"znajdz_max({lst}) = {znajdz_max(lst)}")
    print()

    # Test Zadanie 3
    # Odkomentuj poniższą linię, aby przetestować interaktywnie:
    print("--- Zadanie 3: Suma do zera (uruchomienie pominięte w trybie automatycznym) ---")
    print("Aby uruchomić, wywołaj funkcję suma_do_zera() ręcznie.")
    # suma_do_zera() 
