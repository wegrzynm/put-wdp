# 📝 Zadania - Assembly x64

Cztery zadania do samodzielnego rozwiązania.

---

## 📊 System oceniania

### ✅ ZALICZENIE (ocena 4.0):
Musisz zrobić **oba zadania podstawowe**:
- ✅ Zadanie 1: Hello [Name]
- ✅ Zadanie 2: Kalkulator (dodawanie + odejmowanie)

### 🚀 BARDZO DOBRZE (ocena 5.0):
- ✅ Zadanie 3: Mnożenie w pętli (+1 zadanie)

### 🎁 BONUS (dla chętnych, bez oceny):
- Zadanie 4: Suma tablicy (self-study, materiał dodatkowy)

**Przelicznik ocen:**
- **0-1 zadań:** 2.0 (niezaliczone)
- **2 zadania (1+2):** 4.0 (zaliczone!)
- **3 zadania (1+2+3):** 5.0 (bardzo dobrze!)

---

## 📋 Lista zadań

| Nr | Nazwa | Poziom | Ocena | Czas |
|----|-------|--------|-------|------|
| 1 | Hello [Name] | Łatwy | wymagane (4.0) | 5 min |
| 2 | Kalkulator | Łatwy | wymagane (4.0) | 15 min |
| 3 | Mnożenie w pętli | Średni | rozszerzone (5.0) | 15 min |
| 4 | Suma tablicy | Trudny | bonus (self-study) | 20 min |

**TOTAL na 4.0:** ~20 minut  
**TOTAL na 5.0:** ~35 minut

---

## 🚀 Jak rozwiązywać zadania?

### Krok 1: Otwórz plik zadania
```bash
cd lab2-assembly-x64/02-exercises
cat zad1-hello.asm
```

### Krok 2: Przeczytaj opis i wskazówki
Każde zadanie ma:
- Opis co zrobić
- Algorytm/pseudokod
- Wskazówki z kodem
- Instrukcje sprawdzenia w GDB

### Krok 3: Napisz kod
Znajdź sekcję `; TWÓJ KOD TUTAJ:` i uzupełnij.

### Krok 4: Skompiluj
```bash
nasm -f elf64 zad1-hello.asm -o zad1-hello.o
ld zad1-hello.o -o zad1-hello
```

### Krok 5: Sprawdź
```bash
# Dla zad1 (wypisuje tekst):
./zad1-hello

# Dla zad2, zad3, zad4 (sprawdzanie w GDB):
gdb ./zad2-calculator
(gdb) break _start
(gdb) run
(gdb) continue
(gdb) x/d &suma
```

---

## 🔍 Sprawdzanie wyników w GDB

### Podstawowe komendy:
```bash
# Uruchom debugger
gdb ./program

# Ustaw breakpoint i uruchom
(gdb) break _start
(gdb) run

# Przejdź do końca programu
(gdb) continue

# Sprawdź zmienne
(gdb) x/d &zmienna        # decimal
(gdb) x/x &zmienna        # hex
(gdb) x/4d &tablica       # 4 elementy tablicy
```

### Oczekiwane wyniki:

| Zadanie | Zmienna | Oczekiwany wynik |
|---------|---------|------------------|
| zad1 | (tekst) | "Hello, [TwojeImię]!" |
| zad2 | `suma` | 42 (23 + 19) |
| zad2 | `roznica` | 38 (50 - 12) |
| zad3 | `wynik` | 42 (7 * 6) |
| zad4 | `suma` | 75 (5+10+15+20+25) |

---

## 💡 Często zadawane pytania

### Q: Jak załadować wartość zmiennej do rejestru?

**A:** Użyj nawiasów kwadratowych:
```asm
mov rax, [x]    ; rax = wartość x
```

Bez nawiasów:
```asm
mov rax, x      ; rax = ADRES x (prawie nigdy nie chcesz tego!)
```

### Q: Jak zapisać wynik z rejestru do zmiennej?

**A:**
```asm
mov [wynik], rax    ; zmienna wynik = wartość rax
```

### Q: Jak zrobić pętlę?

**A:** Dwa sposoby:

**Sposób 1: Instrukcja LOOP**
```asm
mov rcx, 10         ; licznik
petla:
    ; ... ciało pętli ...
    loop petla      ; rcx--, jeśli != 0 skocz
```

**Sposób 2: DEC + JNZ**
```asm
mov rcx, 10         ; licznik
petla:
    ; ... ciało pętli ...
    dec rcx         ; rcx--
    jnz petla       ; jeśli != 0, skocz
```

### Q: Jak przejść do następnego elementu tablicy?

**A:** Dodaj rozmiar elementu (dq = 8 bajtów):
```asm
mov rsi, tablica    ; wskaźnik na pierwszy element
add rax, [rsi]      ; użyj pierwszego elementu
add rsi, 8          ; przejdź do następnego (dq = 8 bajtów!)
add rax, [rsi]      ; użyj drugiego elementu
```

### Q: Dlaczego mój program kończy się błędem?

**A:** Najczęstsze przyczyny:
1. Zapomniałeś wywołać `syscall` do exit
2. Błędny dostęp do pamięci (sprawdź nawiasy!)
3. Nieskończona pętla (sprawdź warunek!)

**Debug:** Uruchom w GDB i zobacz gdzie wywala się program.

---

## 📦 Oddawanie zadań

### Format:
Spakuj wszystkie pliki `.asm` do ZIP:
```bash
zip Lab2_ASM_JanKowalski.zip zad*.asm
```

### Nazwa pliku:
```
Lab2_ASM_[ImięNazwisko].zip
```

### Co powinno być w ZIP:

**Dla oceny 4.0:**
```
Lab2_ASM_JanKowalski.zip
├── zad1-hello.asm
└── zad2-calculator.asm
```

**Dla oceny 5.0:**
```
Lab2_ASM_JanKowalski.zip
├── zad1-hello.asm
├── zad2-calculator.asm
└── zad3-multiply.asm
```

**Opcjonalnie (self-study):**
```
├── zad4-array-sum.asm (nie wpływa na ocenę, ale mile widziane!)
```

### Upload:
Wgraj na platformę eKursy do [DEADLINE].

---

## 🆘 Potrzebujesz pomocy?

### Podczas laboratorium:
- Zapytaj prowadzącego
- Zobacz przykłady w `01-examples/`
- Sprawdź wskazówki w komentarzach zadania

### Po laboratoriach:
- Forum na eKursy
- Email: bartekel@gmail.com
- Self-study materiały (dodatkowe zadania)

---

## 🎯 Powodzenia!

Pamiętaj:
- **4.0** to dobry wynik - pokazuje że zrozumiałeś podstawy!
- **5.0** to bonus - dla tych którzy szybko załapali pętle
- Czytaj komentarze w kodzie
- Testuj w GDB
- Eksperymentuj!

Assembly to fundamenty - zrozumienie ich pomoże Ci w:
- Reverse engineering
- Malware analysis
- Exploit development
- Debugowaniu
- Optymalizacji kodu

**To pierwsze zajęcia z Assembly - jeśli zrozumiesz Load-Operate-Store, masz już solidne podstawy!** 🚀