# ===========================================================
# BLOK D: CASE/MATCH (3 zadania × 3 pkt = 9 pkt)
# ===========================================================

print("\n--- BLOK D: CASE/MATCH (lub if-elif) ---\n")

# [2.4] 3 pkt - Kalkulator
print("[2.4] 3 pkt - Prosty kalkulator")
print("""
Zadanie:
  Stwórz kalkulator dla 4 działań: +, -, *, /
  Wejście: a = 10, b = 5, operator = '+'
  Wyświetl wynik w formacie: "10 + 5 = 15"
  
Metoda 1 - if-elif-else:
  if operator == '+':
      wynik = a + b
  elif operator == '-':
      wynik = a - b
  ...
  
Metoda 2 - match/case (Python 3.10+):
  match operator:
      case '+':
          wynik = a + b
      case '-':
          wynik = a - b
      ...
  
Test:
  a, b = 10, 5
  operator = '+'  → 10 + 5 = 15
  operator = '-'  → 10 - 5 = 5
  operator = '*'  → 10 * 5 = 50
  operator = '/'  → 10 / 5 = 2.0
""")
# Twój kod:
def calculator(a,b, operator):
    match operator:
        case '+':
            return a+b
        case '-':
            return a-b
        case '*':
            return a * b
        case '/':
            return a/b
        
a = 10
b =5
print(calculator(a,b,'+'))
print(calculator(a,b,'-'))
print(calculator(a,b,'*'))
print(calculator(a,b,'/'))

# [2.5] 3 pkt - Konwerter jednostek
print("\n[2.5] 3 pkt - Konwerter jednostek odległości")
print("""
Zadanie:
  Konwertuj odległości: km ↔ m ↔ cm
  Wejście: wartosc, jednostka_z, jednostka_na
  
Przeliczniki:
  1 km = 1000 m
  1 m = 100 cm
  1 km = 100000 cm
  
Przykłady:
  5 km → m: 5 * 1000 = 5000 m
  5000 m → km: 5000 / 1000 = 5 km
  2 m → cm: 2 * 100 = 200 cm
  
Algorytm (najprostszy):
  1. Sprawdź parę jednostka_z → jednostka_na
  2. Zastosuj odpowiedni przelicznik
  3. Wyświetl wynik
  
Test:
  wartosc, z, na = 5, 'km', 'm'
  → "5 km = 5000 m"
  
  wartosc, z, na = 200, 'cm', 'm'
  → "200 cm = 2.0 m"
""")
# Twój kod:
def konwerter_jednostek(wartosc, jednostka_z, jednostka_na):
  match (jednostka_z, jednostka_na):
    case ("km", "m"):
      wynik = wartosc * 1000
    case ("m", "km"):
      wynik = wartosc / 1000
    case ("m", "cm"):
      wynik = wartosc * 100
    case ("cm", "m"):
      wynik = wartosc / 100
    case ("km", "cm"):
      wynik = wartosc * 100000
    case ("cm", "km"):
      wynik = wartosc / 100000
    case (a, b) if a == b:
      wynik = wartosc
    case _:
      return "Nieobsługiwana konwersja"
  return f"{wartosc} {jednostka_z} = {wynik} {jednostka_na}"

# Testy przykładowe
print(konwerter_jednostek(5, 'km', 'm'))      # 5 km = 5000 m
print(konwerter_jednostek(5000, 'm', 'km'))   # 5000 m = 5 km
print(konwerter_jednostek(2, 'm', 'cm'))      # 2 m = 200 cm
print(konwerter_jednostek(200, 'cm', 'm'))    # 200 cm = 2.0 m
print(konwerter_jednostek(1, 'km', 'cm'))     # 1 km = 100000 cm
print(konwerter_jednostek(100000, 'cm', 'km'))# 100000 cm = 1 km
print(konwerter_jednostek(10, 'm', 'm'))      # 10 m = 10 m




# [2.6] 3 pkt - Ocena na słowo
print("\n[2.6] 3 pkt - Ocena liczbowa na opis słowny")
print("""
Zadanie:
  Zamień ocenę liczbową (2.0-5.0) na opis słowny
  
Mapowanie:
  5.0 → "Celujący"
  4.5 → "Bardzo dobry plus"
  4.0 → "Bardzo dobry"
  3.5 → "Dobry plus"
  3.0 → "Dobry"
  2.0 → "Dostateczny"
  Inne → "Niepoprawna ocena"
  
Metoda - match/case lub if-elif:
  match ocena:
      case 5.0:
          opis = "Celujący"
      case 4.5:
          opis = "Bardzo dobry plus"
      ...
  
Test:
  ocena = 5.0 → "Ocena 5.0: Celujący"
  ocena = 3.5 → "Ocena 3.5: Dobry plus"
  ocena = 1.0 → "Ocena 1.0: Niepoprawna ocena"
""")
# Twój kod:
def ocena(ocena):
   match ocena:
    case 5.0 :
        return "Celujący"
    case 4.5 :
        return "Bardzo dobry plus"
    case 4.0 :
        return "Bardzo dobry"
    case 3.5: 
        return "Dobry plus"
    case 3.0 : 
        return "Dobry"
    case 2.0 :
        return "Dostateczny"
    case _:
         return "Niepoprawna ocena"
         
      
print(ocena(5))
print(ocena(4))
print(ocena(3))
print(ocena(2))
print(ocena(1))
print(ocena(0))

