import re

# Zadanie 5.1: URL Parser with Capturing Groups
def parse_url(text):
    pattern = r"(https?)://([a-zA-Z0-9.-]+)(/[a-zA-Z0-9._/-]*)?"
    match = re.search(pattern, text)
    
    if match:
        protocol = match.group(1)
        domain = match.group(2)
        path = match.group(3) if match.group(3) else "/"
        
        print(f"Protocol: {protocol}")
        print(f"Domain: {domain}")
        print(f"Path: {path}")
    else:
        print("No URL found")

# Zadanie 5.2: Password Validator with Lookaheads
def validate_strong_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
    return bool(re.match(pattern, password))

# Zadanie 5.3: Log Parser with Named Groups
def parse_log_line_named(log_line):
    pattern = r"(?P<ip>\d+\.\d+\.\d+\.\d+) - (?P<method>\w+) (?P<endpoint>/\S+) - (?P<status>\d{3})"
    match = re.search(pattern, log_line)
    
    if match:
        print(f"IP: {match.group('ip')}")
        print(f"Method: {match.group('method')}")
        print(f"Endpoint: {match.group('endpoint')}")
        print(f"Status: {match.group('status')}")
    else:
        print("Invalid log format")

if __name__ == "__main__":
    print("\n--- 5.1 URL Parser ---")
    parse_url("Visit https://example.com/path/to/page")

    print("\n--- 5.2 Strong Password ---")
    print(validate_strong_password("SecureP@ss1"))
    print(validate_strong_password("weak"))

    print("\n--- 5.3 Log Parser Named ---")
    parse_log_line_named("192.168.1.1 - GET /admin - 403")
