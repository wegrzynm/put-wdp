import re

# Zadanie 3.1: Match Simple Pattern
def contains_admin(text):
    return bool(re.search(r"admin", text, re.IGNORECASE))

# Zadanie 3.2: Email Validator
def validate_email(email):
    pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.search(pattern, email))

# Zadanie 3.3: Find All Digits
def find_numbers(text):
    pattern = r"\d+"
    return re.findall(pattern, text)

# Zadanie 3.4: Phone Number Extractor
def extract_phone_numbers(text):
    pattern = r"(\+48\s?)?\d{3}[\s-]?\d{3}[\s-]?\d{3}"    
    real_pattern = r"(?:(?:\+48\s?)?\d{3}[\s-]?\d{3}[\s-]?\d{3})"
    return re.findall(real_pattern, text)

# Zadanie 3.5: IP Address Extractor
def extract_ips(text):
    pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    return re.findall(pattern, text)

if __name__ == "__main__":
    print("\n--- 3.1 Contains Admin ---")
    print(contains_admin("User logged to ADMIN panel"))

    print("\n--- 3.2 Email Validator ---")
    print(validate_email("user@example.com"))
    print(validate_email("user@"))

    print("\n--- 3.3 Find Numbers ---")
    print(find_numbers("Port 8080 on 192.168.1.1 failed at 14:32"))

    print("\n--- 3.4 Phone Numbers ---")
    print(extract_phone_numbers("Call me at +48 123 456 789 or 987-654-321"))

    print("\n--- 3.5 Extract IPs ---")
    print(extract_ips("Failed login from 192.168.1.1 and 10.0.0.5 detected."))
