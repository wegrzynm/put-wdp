import re
import os

# Zadanie 6.1: AI Buzzword Detector
def detect_ai_buzzwords_simple(text):
    pattern = r"(warto zauważyć|należy podkreślić|w kontekście|mam nadzieję|z przyjemnością|podsumowując)"
    matches = re.findall(pattern, text, re.IGNORECASE)
    print(f"{len(matches)} AI phrases found: {matches}")
    return len(matches)

# Zadanie 6.2: AI Content Detector - Comprehensive
def detect_title_case(text):
    words = text.split()
    capitalized = sum(1 for word in words if word and word[0].isupper())
    ratio = capitalized / len(words) if words else 0
    return 30 if ratio > 0.6 else 0

def detect_ai_buzzwords_score(text):
    pattern = r"(warto zauważyć|należy podkreślić|w kontekście|mam nadzieję|z przyjemnością|podsumowując)"
    matches = re.findall(pattern, text, re.IGNORECASE)
    return 30 if len(matches) > 2 else 0

def detect_numbered_list(text):
    pattern = r"^\d+\."
    if re.search(pattern, text, re.MULTILINE):
        return 20
    return 0

def detect_podsumowujac(text):
    return 20 if "podsumowując" in text.lower() else 0

def analyze_text(text, text_name):
    score = 0
    score += detect_title_case(text)
    score += detect_ai_buzzwords_score(text)
    score += detect_numbered_list(text)
    score += detect_podsumowujac(text)
    
    classification = "AI-GENERATED" if score >= 40 else "HUMAN"
    print(f"{text_name:<30}: {score}% - {classification}")
    return classification

def full_analysis():
    file_path = "lab7/Lab07_Dataset_Literatura.txt"
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return

    print("========================================")
    print("AI TEXT DETECTION REPORT")
    print("========================================")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    texts = content.split('\n\n')
    
    for i, txt in enumerate(texts):
        if txt.strip():
            analyze_text(txt, f"Text {i+1}")

    print("========================================")

if __name__ == "__main__":
    print("\n--- 6.1 Buzzwords ---")
    detect_ai_buzzwords_simple("Warto zauważyć, że w kontekście AI...");

    print("\n--- 6.2 Analysis ---")
    full_analysis()
