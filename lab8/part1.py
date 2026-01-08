# Laboratorium 8: Złożoność obliczeniowa
# Cześć 1: Rozgrzewka - Zliczanie operacji

# Zadanie 1: Stała złożoność
def get_first(lista):
    """
    Pytanie: Ile operacji wykonuje ta funkcja dla listy o długości n?
    Odpowiedź: 1 (O(1))
    """
    if not lista:
        return None
    return lista[0]

# Przykład zadanie 1
moja_lista = [10, 20, 30, 40, 50]
print(f"Zadanie 1 - Pierwszy element: {get_first(moja_lista)}")


# Zadanie 2: Liniowa złożoność
def sum_all(lista):
    """
    Pytanie: Ile operacji dodawania wykonuje ta funkcja dla listy o długości n?
    Odpowiedź: n (O(n))
    """
    suma = 0
    for x in lista:
        suma += x
    return suma

# Przykład zadanie 2
print(f"Zadanie 2 - Suma elementów: {sum_all(moja_lista)}")


# Zadanie 3: Kwadratowa złożoność
def print_pairs(lista):
    """
    Pytanie: Ile par wypisze ten kod dla listy o długości n?
    Odpowiedź: n² (O(n²))
    """
    print(f"Zadanie 3 - Pary dla listy {lista}:")
    count = 0
    for i in lista:
        for j in lista:
            print(f"({i}, {j})", end=" ")
            count += 1
    print(f"\nLiczba wypisanych par: {count} (co odpowiada {len(lista)}^2)")

# Przykład zadanie 3
print_pairs([1, 2, 3])
