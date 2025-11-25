# Part 2

def factorial_iter(n):
    """
    Oblicza n! iteracyjnie (z pętlą).
    
    Args:
        n (int): liczba naturalna (n >= 0)
    
    Returns:
        int: wartość n!
    """
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

def factorial_rec(n):
    """
    Oblicza n! rekurencyjnie.
    
    Args:
        n (int): liczba naturalna (n >= 0)
    
    Returns:
        int: wartość n!
    """
    if n == 0 or n == 1:  # Przypadek bazowy
        return 1
    return n * factorial_rec(n-1)

print(factorial_iter(0))  # 1
print(factorial_rec(0))   # 1

print(factorial_iter(5))  # 120
print(factorial_rec(5))   # 120

print(factorial_iter(10)) # 3628800
print(factorial_rec(10))  # 3628800


def fibonacci_iter(n):
    """
    Oblicza n-ty wyraz ciągu Fibonacciego iteracyjnie.
    
    Args:
        n (int): indeks wyrazu (n >= 0)
    
    Returns:
        int: n-ty wyraz ciągu Fibonacciego
    """
    if n < 2:
        return 1
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a + b
    return b


def fibonacci_rec(n):
    """
    Oblicza n-ty wyraz ciągu Fibonacciego rekurencyjnie.
    
    Args:
        n (int): indeks wyrazu (n >= 0)
    
    Returns:
        int: n-ty wyraz ciągu Fibonacciego
    """
    if n < 2:
        return 1
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)

print(fibonacci_iter(0))  # 1
print(fibonacci_rec(0))   # 1

print(fibonacci_iter(7))  # 21
print(fibonacci_rec(7))   # 21

print(fibonacci_iter(10)) # 89
print(fibonacci_rec(10))  # 89

def gcd(a, b):
    """
    Oblicza NWD(a, b) algorytmem Euklidesa (rekurencyjnie).
    
    Args:
        a (int): pierwsza liczba (a >= 0)
        b (int): druga liczba (b >= 0)
    
    Returns:
        int: największy wspólny dzielnik
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(48, 18))  # 6
print(gcd(100, 35)) # 5
print(gcd(17, 19))  # 1 (liczby pierwsze względem siebie)
print(gcd(12, 8))   # 4

def sum_of_digits_rec(n):
    """
    Oblicza sumę cyfr liczby n rekurencyjnie.
    
    Args:
        n (int): liczba naturalna (n >= 0)
    
    Returns:
        int: suma cyfr
    """
    if n < 10:  # Przypadek bazowy
        return n
    return (n % 10) + sum_of_digits_rec(n // 10)

print(sum_of_digits_rec(123))   # 6
print(sum_of_digits_rec(4567))  # 22
