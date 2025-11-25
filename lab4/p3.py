
def reverse_list(lst):
    """
    Odwraca kolejność elementów w liście (in-place).
    
    Args:
        lst (list): lista do odwrócenia
    
    Returns:
        None (modyfikuje listę w miejscu)
    """
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

numbers = [1, 2, 3, 4, 5]
reverse_list(numbers)
print(numbers)  # [5, 4, 3, 2, 1]

letters = ['a', 'b', 'c']
reverse_list(letters)
print(letters)  # ['c', 'b', 'a']

# Funkcje pomocnicze:
def square(x):
    return x * x

def double(x):
    return x * 2

def negate(x):
    return -x

def apply_to_list(lst, func):
    """
    Aplikuje funkcję func do każdego elementu listy (in-place).
    
    Args:
        lst (list): lista do przetworzenia
        func (function): funkcja do zastosowania
    
    Returns:
        None (modyfikuje listę w miejscu)
    """
    for i in range(len(lst)):
        lst[i] = func(lst[i])

numbers = [1, 2, 3, 4, 5]
apply_to_list(numbers, square)
print(numbers)  # [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]
apply_to_list(numbers, double)
print(numbers)  # [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5]
apply_to_list(numbers, negate)
print(numbers)  # [-1, -2, -3, -4, -5]