# Zadanie 1.1: ASCII Explorer
def ascii_explorer():
    print("--- 1.1 ASCII Explorer ---")
    char = input("Podaj znak: ")
    if len(char) == 1:
        print(ord(char))
    else:
        print("Podaj dokładnie jeden znak.")

# Zadanie 1.2: Caesar Cipher - Basic
def caesar_cipher_basic(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            code = ord(char) + 3
            if code > ord('z'):
                code -= 26
            result += chr(code)
        else:
            result += char
    return result

# Zadanie 1.3: Case Converter
def fix_title_case(text):
    sentences = text.split('. ')
    fixed_sentences = []
    for s in sentences:
        if s:
            # Capitalize first word, lowercase others
            words = s.split()
            if words:
                words[0] = words[0].capitalize()
                for i in range(1, len(words)):
                    words[i] = words[i].lower()
                fixed_sentences.append(" ".join(words))
    return ". ".join(fixed_sentences) + ("." if text.endswith(".") else "")

if __name__ == "__main__":
    ascii_explorer() 
    
    # Test 1.2
    print("\n--- 1.2 Caesar Cipher ---")
    print(caesar_cipher_basic("hello world"))  # khoor zruog
    
    # Test 1.3
    print("\n--- 1.3 Case Converter ---")
    print(fix_title_case("To Jest Przykładowy Tekst. Kolejne Zdanie Tutaj."))
