def is_prime(n):
    """
    Sprawdza czy n jest liczbą pierwszą.
    
    Args:
        n (int): liczba do sprawdzenia (n >= 2)
    
    Returns:
        bool: True jeśli pierwsza, False w przeciwnym razie
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 

print(is_prime(2))   # True
print(is_prime(7))   # True
print(is_prime(10))  # False
print(is_prime(17))  # True
print(is_prime(20))  # False

def sum_of_digits(n):
    """
    Oblicza sumę cyfr liczby n.
    
    Args:
        n (int): liczba naturalna (n >= 0)
    
    Returns:
        int: suma cyfr liczby n
    """
    return sum(int(digit) for digit in str(n))

print(sum_of_digits(123))   # 6 (1+2+3)
print(sum_of_digits(4567))  # 22 (4+5+6+7)
print(sum_of_digits(1000))  # 1 (1+0+0+0)
print(sum_of_digits(999))   # 27 (9+9+9)


def digit_count(n):
    """
    Oblicza liczbę cyfr w liczbie n.
    
    Args:
        n (int): liczba naturalna (n >= 0)
    
    Returns:
        int: liczba cyfr
    """
    return len(str(n))

print(digit_count(5))      # 1
print(digit_count(42))     # 2
print(digit_count(1000))   # 4
print(digit_count(999999)) # 6
print(digit_count(0))      # 1 (zero ma jedną cyfrę!)