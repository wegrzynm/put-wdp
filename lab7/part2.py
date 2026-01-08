# Zadanie 2.1: Password Strength Checker
def check_password_strength(password):
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    length_ok = len(password) >= 8

    if length_ok and has_digit and has_upper:
        return "STRONG"
    elif length_ok and has_digit:
        return "MEDIUM"
    else:
        return "WEAK"

# Zadanie 2.2: Simple Log Parser
def parse_log_line(log_line):
    parts = log_line.split(" - ")
    if len(parts) == 3:
        ip = parts[0].strip()
        middle = parts[1].strip().split()
        status = parts[2].strip()
        
        if len(middle) == 2:
            method = middle[0]
            endpoint = middle[1]
            print(f"IP: {ip}\nMethod: {method}\nEndpoint: {endpoint}\nStatus: {status}")
            return
            
    print("Invalid format")

# Zadanie 2.3: Count Suspicious Keywords
def count_suspicious_keywords(text):
    SUSPICIOUS = ['password', 'urgent', 'click here', 'verify', 'credit card']
    text_lower = text.lower()
    count = 0
    for keyword in SUSPICIOUS:
        count += text_lower.count(keyword)
    return count

if __name__ == "__main__":
    # Test 2.1
    print("\n--- 2.1 Password Strength ---")
    print(check_password_strength("password"))    # WEAK
    print(check_password_strength("password123")) # MEDIUM
    print(check_password_strength("Password123")) # STRONG

    # Test 2.2
    print("\n--- 2.2 Log Parser ---")
    parse_log_line("192.168.1.1 - GET /admin - 403")

    # Test 2.3
    print("\n--- 2.3 Suspicious Keywords ---")
    text = "URGENT: Verify your PASSWORD now! Click here to update credit card details."
    print(count_suspicious_keywords(text)) # 5
