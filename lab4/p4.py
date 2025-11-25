import hashlib

def hash_pin(pin):
    """Oblicza hash SHA-256 dla PIN-u"""
    return hashlib.sha256(str(pin).encode()).hexdigest()

# Przykład: hash prawdziwego PIN-u
target_hash = hash_pin(1234)
print(f"Hash do złamania: {target_hash}")

def crack_pin(target_hash):
    """
    Znajduje 4-cyfrowy PIN metodą brute-force.
    
    Args:
        target_hash (str): hash SHA-256 szukanego PIN-u
    
    Returns:
        str: znaleziony PIN (z zerami wiodącymi) lub None
    """
    for pin in range(10000):
        pin_str = str(pin).zfill(4)
        if hash_pin(pin_str) == target_hash:
            return pin_str
    return None

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
print(f"Czas: {elapsed:.4f}s")