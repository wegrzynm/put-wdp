# LAB 4: Functions and Procedures

**Kurs:** Introduction to Programming  
**Kierunek:** Cybersecurity, rok 1  
**Czas:** 90 minut  
**Język:** Python 3  
**Narzędzie:** Programiz.com lub lokalne środowisko

---

## 🎯 Cel laboratorium

- Nauczyć się definiować i używać funkcji
- Zrozumieć różnicę między iteracją, a rekurencją
- Porównać wydajność różnych podejść
- Pisać czysty, strukturyzowany kod

---

## 📊 System oceniania

- **3.0:** Part 1 (zadania 1-3) + Part 2 wersje iteracyjne (zadania 4-5)
- **4.0:** Powyższe + Part 2 wersje rekurencyjne + zadanie 6
- **5.0:** Powyższe + Part 3 (zadania 7-8)
- **Bonus:** Zadanie 9 (challenge)

---

## ⚠️ Ważne informacje

### Rekurencja - podstawy

Rekurencja to funkcja wywołująca samą siebie. Każda funkcja rekurencyjna **MUSI** mieć:

1. **Przypadek bazowy** (warunek stopu)
2. **Krok rekurencyjny** (wywołanie samej siebie)

Bez przypadku bazowego → błąd `RecursionError: maximum recursion depth exceeded`

### Parametry w Pythonie

- **Immutable** (int, float, str) - nie można zmienić w funkcji
- **Mutable** (list, dict) - można modyfikować w funkcji
- **Zwracanie wielu wartości:** `return a, b, c

---

# NOTATKI KOŃCOWE

## Co zapamiętać

1. **Funkcje = DRY** (Don't Repeat Yourself)
2. **Rekurencja = Base Case + Recursive Step**
3. **Rekurencja ≠ zawsze lepsza** (patrz Fibonacci)
4. **Parametry w Pythonie** działają inaczej niż w C

## Częste błędy

- Brak przypadku bazowego w rekurencji
- Zapomnienie `return` w funkcji
- Off-by-one errors w `range()`
- Mylenie `=` i `==`

## Linki

- Python functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- Recursion visualization: https://pythontutor.com/
- Big O cheat sheet: https://www.bigocheatsheet.com/

---

**Powodzenia! 🚀**

# PART 1: FUNKCJE PODSTAWOWE

## Zadanie 1: Liczba pierwsza ⭐

Napisz funkcję `is_prime(n)`, która sprawdza czy liczba `n` jest liczbą pierwszą.

**Definicja:** Liczba pierwsza to liczba naturalna większa od 1, która ma dokładnie dwa dzielniki: 1 i samą siebie.

### Specyfikacja

```python
def is_prime(n):
    """
    Sprawdza czy n jest liczbą pierwszą.
    
    Args:
        n (int): liczba do sprawdzenia (n >= 2)
    
    Returns:
        bool: True jeśli pierwsza, False w przeciwnym razie
    """
    pass  # TODO: Twoja implementacja
```

### Przykłady

```python
print(is_prime(2))   # True
print(is_prime(7))   # True
print(is_prime(10))  # False
print(is_prime(17))  # True
print(is_prime(20))  # False
```

### Wskazówka

Sprawdź czy istnieje dzielnik z przedziału od 2 do n-1. Użyj operatora modulo `%`.

---

## Zadanie 2: Suma cyfr ⭐

Napisz funkcję `sum_of_digits(n)`, która oblicza sumę cyfr liczby `n`.

### Specyfikacja

```python
def sum_of_digits(n):
    """
    Oblicza sumę cyfr liczby n.
    
    Args:
        n (int): liczba naturalna (n >= 0)
    
    Returns:
        int: suma cyfr liczby n
    """
    pass  # TODO: Twoja implementacja
```

### Przykłady

```python
print(sum_of_digits(123))   # 6 (1+2+3)
print(sum_of_digits(4567))  # 22 (4+5+6+7)
print(sum_of_digits(1000))  # 1 (1+0+0+0)
print(sum_of_digits(999))   # 27 (9+9+9)
```

### Wskazówki

- Ostatnia cyfra: `n % 10`
- Usuń ostatnią cyfrę: `n // 10`
- Powtarzaj dopóki `n > 0`

---

## Zadanie 3: Liczba cyfr ⭐

Napisz funkcję `digit_count(n)`, która zwraca liczbę cyfr w liczbie `n`.

### Specyfikacja

```python
def digit_count(n):
    """
    Oblicza liczbę cyfr w liczbie n.
    
    Args:
        n (int): liczba naturalna (n >= 0)
    
    Returns:
        int: liczba cyfr
    """
    pass  # TODO: Twoja implementacja
```

### Przykłady

```python
print(digit_count(5))      # 1
print(digit_count(42))     # 2
print(digit_count(1000))   # 4
print(digit_count(999999)) # 6
print(digit_count(0))      # 1 (zero ma jedną cyfrę!)
```

### Wskazówka

Dziel przez 10 i licz ile razy to zrobisz zanim dojdziesz do 0.

# PART 2: REKURENCJA

## Zadanie 4: Silnia ⭐⭐

Napisz **dwie wersje** funkcji obliczającej silnię: iteracyjną i rekurencyjną.

**Definicja:**

```
n! = 1 × 2 × 3 × ... × n
0! = 1
1! = 1
5! = 120
```

### Specyfikacja

```python
def factorial_iter(n):
    """
    Oblicza n! iteracyjnie (z pętlą).
    
    Args:
        n (int): liczba naturalna (n >= 0)
    
    Returns:
        int: wartość n!
    """
    pass  # TODO: Wersja z pętlą


def factorial_rec(n):
    """
    Oblicza n! rekurencyjnie.
    
    Args:
        n (int): liczba naturalna (n >= 0)
    
    Returns:
        int: wartość n!
    """
    pass  # TODO: Wersja rekurencyjna
```

### Przykłady

```python
print(factorial_iter(0))  # 1
print(factorial_rec(0))   # 1

print(factorial_iter(5))  # 120
print(factorial_rec(5))   # 120

print(factorial_iter(10)) # 3628800
print(factorial_rec(10))  # 3628800
```

### Wskazówki

**Iteracyjnie:**

```python
result = 1
for i in range(1, n+1):
    result = result * i
return result
```

**Rekurencyjnie:**

```python
if n == 0 or n == 1:  # Przypadek bazowy
    return 1
return n * factorial_rec(n-1)  # Krok rekurencyjny
```

---

## Zadanie 5: Ciąg Fibonacciego ⭐⭐⭐

Napisz **dwie wersje** funkcji obliczającej n-ty wyraz ciągu Fibonacciego.

**Definicja:**

```
F(0) = 1
F(1) = 1
F(n) = F(n-1) + F(n-2) dla n >= 2

Ciąg: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

### Specyfikacja

```python
def fibonacci_iter(n):
    """
    Oblicza n-ty wyraz ciągu Fibonacciego iteracyjnie.
    
    Args:
        n (int): indeks wyrazu (n >= 0)
    
    Returns:
        int: n-ty wyraz ciągu Fibonacciego
    """
    pass  # TODO: Wersja z pętlą


def fibonacci_rec(n):
    """
    Oblicza n-ty wyraz ciągu Fibonacciego rekurencyjnie.
    
    Args:
        n (int): indeks wyrazu (n >= 0)
    
    Returns:
        int: n-ty wyraz ciągu Fibonacciego
    """
    pass  # TODO: Wersja rekurencyjna
```

### Przykłady

```python
print(fibonacci_iter(0))  # 1
print(fibonacci_rec(0))   # 1

print(fibonacci_iter(7))  # 21
print(fibonacci_rec(7))   # 21

print(fibonacci_iter(10)) # 89
print(fibonacci_rec(10))  # 89
```

### Wskazówki

**Iteracyjnie:**

```python
if n < 2:
    return 1
a, b = 1, 1
for i in range(n-1):
    a, b = b, a + b
return b
```

**Rekurencyjnie:**

```python
if n < 2:
    return 1
return fibonacci_rec(n-1) + fibonacci_rec(n-2)
```

### ⚡ BONUS: Porównanie wydajności

```python
import time

def measure_time(func, n):
    start = time.time()
    result = func(n)
    elapsed = time.time() - start
    return result, elapsed

# Test dla różnych n
for n in [10, 20, 30, 35]:
    result_iter, time_iter = measure_time(fibonacci_iter, n)
    result_rec, time_rec = measure_time(fibonacci_rec, n)
    
    print(f"n={n}:")
    print(f"  Iteracyjnie: {time_iter:.6f}s")
    print(f"  Rekurencyjnie: {time_rec:.6f}s")
    print(f"  Różnica: {time_rec/time_iter:.1f}x wolniej\n")
```

**Pytanie:** Dlaczego rekurencja jest tak wolna dla dużych n?

---

## Zadanie 6: NWD - Algorytm Euklidesa ⭐⭐

Napisz funkcję `gcd(a, b)` obliczającą największy wspólny dzielnik **rekurencyjnie**.

**Algorytm Euklidesa:**

```
gcd(a, b) = gcd(b, a mod b)  jeśli b != 0
gcd(a, 0) = a
```

### Specyfikacja

```python
def gcd(a, b):
    """
    Oblicza NWD(a, b) algorytmem Euklidesa (rekurencyjnie).
    
    Args:
        a (int): pierwsza liczba (a >= 0)
        b (int): druga liczba (b >= 0)
    
    Returns:
        int: największy wspólny dzielnik
    """
    pass  # TODO: Implementacja rekurencyjna
```

### Przykłady

```python
print(gcd(48, 18))  # 6
print(gcd(100, 35)) # 5
print(gcd(17, 19))  # 1 (liczby pierwsze względem siebie)
print(gcd(12, 8))   # 4
```

### Wskazówka

```python
if b == 0:
    return a
else:
    return gcd(b, a % b)
```

---

## Zadanie BONUS: Suma cyfr rekurencyjnie ⭐⭐

Przepisz funkcję `sum_of_digits` z zadania 2, ale tym razem **rekurencyjnie**.

### Specyfikacja

```python
def sum_of_digits_rec(n):
    """
    Oblicza sumę cyfr liczby n rekurencyjnie.
    
    Args:
        n (int): liczba naturalna (n >= 0)
    
    Returns:
        int: suma cyfr
    """
    pass  # TODO: Implementacja rekurencyjna
```

### Przykłady

```python
print(sum_of_digits_rec(123))   # 6
print(sum_of_digits_rec(4567))  # 22
```

### Wskazówka

```python
if n < 10:  # Przypadek bazowy
    return n
return (n % 10) + sum_of_digits_rec(n // 10)
```

# PART 3: ZAAWANSOWANE

## Zadanie 7: Odwracanie listy ⭐⭐

Napisz funkcję `reverse_list(lst)`, która odwraca kolejność elementów w liście **in-place** (w miejscu).

**UWAGA:** Funkcja modyfikuje oryginalną listę, nic nie zwraca!

### Specyfikacja

```python
def reverse_list(lst):
    """
    Odwraca kolejność elementów w liście (in-place).
    
    Args:
        lst (list): lista do odwrócenia
    
    Returns:
        None (modyfikuje listę w miejscu)
    """
    pass  # TODO: Twoja implementacja
```

### Przykłady

```python
numbers = [1, 2, 3, 4, 5]
reverse_list(numbers)
print(numbers)  # [5, 4, 3, 2, 1]

letters = ['a', 'b', 'c']
reverse_list(letters)
print(letters)  # ['c', 'b', 'a']
```

### Wskazówka

Użyj dwóch indeksów: `left` i `right`. Zamieniaj elementy i przesuwaj do środka:

```python
left = 0
right = len(lst) - 1
while left < right:
    lst[left], lst[right] = lst[right], lst[left]
    left += 1
    right -= 1
```

---

## Zadanie 8: Zastosuj funkcję do listy ⭐⭐⭐

Napisz funkcję `apply_to_list(lst, func)`, która aplikuje funkcję `func` do każdego elementu listy i modyfikuje listę **in-place**.

**To funkcja wyższego rzędu - przyjmuje funkcję jako parametr!**

### Specyfikacja

```python
def apply_to_list(lst, func):
    """
    Aplikuje funkcję func do każdego elementu listy (in-place).
    
    Args:
        lst (list): lista do przetworzenia
        func (function): funkcja do zastosowania
    
    Returns:
        None (modyfikuje listę w miejscu)
    """
    pass  # TODO: Twoja implementacja
```

### Przykłady

```python
# Funkcje pomocnicze
def square(x):
    return x * x

def double(x):
    return x * 2

def negate(x):
    return -x

# Testy
numbers = [1, 2, 3, 4, 5]
apply_to_list(numbers, square)
print(numbers)  # [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]
apply_to_list(numbers, double)
print(numbers)  # [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5]
apply_to_list(numbers, negate)
print(numbers)  # [-1, -2, -3, -4, -5]
```

### Wskazówka

```python
for i in range(len(lst)):
    lst[i] = func(lst[i])
```

# CHALLENGE: Mini Hash Cracker 🔐

## Zadanie 9: Brute Force PIN ⭐⭐⭐⭐

Symulacja ataku brute-force na 4-cyfrowy PIN. Znajdź PIN wiedząc jego hash SHA-256.

**Cel:** Pokazać jak działa łamanie haseł i dlaczego słabe hasła są niebezpieczne.

### Setup

```python
import hashlib

def hash_pin(pin):
    """Oblicza hash SHA-256 dla PIN-u"""
    return hashlib.sha256(str(pin).encode()).hexdigest()

# Przykład: hash prawdziwego PIN-u
target_hash = hash_pin(1234)
print(f"Hash do złamania: {target_hash}")
```

### Zadanie

```python
def crack_pin(target_hash):
    """
    Znajduje 4-cyfrowy PIN metodą brute-force.
    
    Args:
        target_hash (str): hash SHA-256 szukanego PIN-u
    
    Returns:
        str: znaleziony PIN (z zerami wiodącymi) lub None
    """
    for pin in range(10000):
        pin_str = str(pin).zfill(4)  # Dodaj zera z przodu (0001, 0042, itp.)
        if hash_pin(pin_str) == target_hash:
            return pin_str
    return None
```

### Test

```python
# Test 1
target = hash_pin(1234)
result = crack_pin(target)
print(f"Znaleziony PIN: {result}")  # "1234"

# Test 2
target = hash_pin(7890)
result = crack_pin(target)
print(f"Znaleziony PIN: {result}")  # "7890"

# Test 3 - pomiar czasu
import time
target = hash_pin(9999)  # Najgorszy przypadek
start = time.time()
result = crack_pin(target)
elapsed = time.time() - start
print(f"Znaleziony PIN: {result}")
print(f"Czas: {elapsed:.2f}s")
```

### Pytania do przemyślenia

1. Ile kombinacji musisz sprawdzić w najgorszym przypadku?
2. Dlaczego 4-cyfrowy PIN jest słaby?
3. Jak długo zajęłoby złamanie 8-cyfrowego PIN-u?
4. A hasła alfanumerycznego 8-znakowego?

### Wskazówka

```python
for pin in range(10000):
    pin_str = str(pin).zfill(4)  # Dodaj zera z przodu (0001, 0042, itp.)
    if hash_pin(pin_str) == target_hash:
        return pin_str
return None
```

---