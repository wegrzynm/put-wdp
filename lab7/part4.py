import re

# Zadanie 4.1: Extract URLs
def extract_urls(text):
    pattern = r"https?://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9._-]*)?"
    return re.findall(pattern, text)

# Zadanie 4.2: Find Dates
def find_dates(text):
    pattern = r"\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2}"
    return re.findall(pattern, text)

# Zadanie 4.3: Extract Hashtags
def extract_hashtags(text):
    pattern = r"#[a-zA-Z0-9_]+"
    return re.findall(pattern, text)

# Zadanie 4.4: Validate Hex Color
def validate_hex_color(color):
    pattern = r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
    return bool(re.match(pattern, color))

if __name__ == "__main__":
    print("\n--- 4.1 URLs ---")
    print(extract_urls("Visit https://example.com/page and http://test.org"))

    print("\n--- 4.2 Dates ---")
    print(find_dates("Event on 25.12.2024 or 2024-12-25"))

    print("\n--- 4.3 Hashtags ---")
    print(extract_hashtags("Check #cybersecurity and #InfoSec trends!"))

    print("\n--- 4.4 Hex Colors ---")
    print(validate_hex_color("#FF5733")) # True
    print(validate_hex_color("FF5733"))  # False
