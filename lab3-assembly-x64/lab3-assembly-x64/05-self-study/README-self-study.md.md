# 🎓 Self-Study - Dodatkowe zadania Assembly

Materiały dla studentów którzy:
- Skończyli zadania laboratoryjne (1-3) i chcą więcej
- Chcą przygotować się do następnych laboratoriów
- Lubią wyzwania i chcą pogłębić wiedzę

---

## 🎯 Dla kogo?

- ✅ Skończyłeś Lab 2 z oceną 4.0 lub 5.0
- ✅ Rozumiesz Load-Operate-Store
- ✅ Potrafisz napisać prostą pętlę
- ✅ Chcesz nauczyć się funkcji i rekurencji

**Nie wymagane na ocenę!** To materiały **dodatkowe** dla pasjonatów.

---

## 📋 Lista zadań

| Nr | Nazwa | Trudność | Czas | Koncepty |
|----|-------|----------|------|----------|
| 1 | Silnia (factorial) | ⭐⭐ | 30 min | Pętla, akumulator |
| 2 | Fibonacci | ⭐⭐⭐ | 45 min | Rekurencja, stos |
| 3 | strlen | ⭐⭐ | 30 min | Stringi, pętla |
| 4 | strcmp | ⭐⭐⭐ | 45 min | Stringi, porównania |
| 5 | power (a^b) | ⭐⭐⭐ | 60 min | Pętle zagnieżdżone |

**TOTAL:** ~3-4 godziny czystej pracy

---

## 🚀 Jak zacząć?

### Krok 1: Wybierz zadanie
Zacznij od task1 (najłatwiejsze), potem task2, itd.

### Krok 2: Przeczytaj opis
Każde zadanie ma:
- Opis algorytmu
- Przykłady działania
- Wskazówki
- Oczekiwane wyniki

### Krok 3: Napisz kod
Otwórz plik `.asm` i uzupełnij sekcję `; TWÓJ KOD TUTAJ:`

### Krok 4: Testuj
```bash
nasm -f elf64 task1-factorial.asm -o task1.o
ld task1.o -o task1
gdb ./task1
```

### Krok 5: Sprawdź rozwiązanie
Jeśli utkniesz > 30 minut, zobacz `SOLUTIONS/`

---

## 💡 Wskazówki ogólne

### Debugging w GDB:
```bash
gdb ./program
(gdb) break _start
(gdb) run
(gdb) info registers
(gdb) stepi          # Krok po kroku
(gdb) x/d &wynik     # Sprawdź zmienną
```

### Typowe błędy:
- ❌ Nieskończona pętla → Sprawdź warunek końca
- ❌ Segfault → Sprawdź adresy (nawiasy `[]`)
- ❌ Zły wynik → Wypisz kroki w GDB

### Stack overflow (rekurencja):
Jeśli program wywala się przy rekurencji:
- Zwiększ rozmiar stosu: `ulimit -s unlimited`
- Albo zmniejsz głębokość rekurencji (mniejsze n)

---

## 📚 Przydatne materiały

### Dokumentacja:
- NASM manual: https://www.nasm.us/doc/
- x64 syscalls: https://syscalls.w3challs.com/
- x64 calling convention: https://wiki.osdev.org/System_V_ABI

### Tutoriale:
- x86-64 Assembly: https://cs.lmu.edu/~ray/notes/nasmtutorial/
- GDB tutorial: https://www.gdbtutorial.com/

### Narzędzia:
- Godbolt: https://godbolt.org/ (zobacz jak kompilator generuje ASM)
- OnlineGDB: https://www.onlinegdb.com/ (test online)

---

## 🎁 Bonusy

Jeśli skończysz wszystkie 5 zadań:

### Challenge 1: ROT13 cipher
Napisz funkcję która szyfruje string algorytmem ROT13.

### Challenge 2: Bubble sort
Posortuj tablicę 10 liczb (bubble sort).

### Challenge 3: Prime checker
Sprawdź czy liczba jest liczbą pierwszą.

---

## 📧 Feedback

Jeśli:
- Rozwiązałeś zadania i chcesz feedback
- Masz pomysł na nowe zadanie
- Znalazłeś błąd

Napisz: bartekel@gmail.com

---

**Powodzenia!** 🚀

Assembly to fundamenty - im więcej ćwiczysz, tym lepiej rozumiesz jak działa komputer!