# 📚 Przykłady - Assembly x64

Cztery podstawowe przykłady pokazujące fundamenty Assembly.

---

## 📋 Lista przykładów

| Plik | Temat | Poziom | Czas |
|------|-------|--------|------|
| `ex0-hello.asm` | Hello World | Podstawowy | 5 min |
| `ex1-variables.asm` | Zmienne i etykiety | Podstawowy | 10 min |
| `ex2-operations.asm` | Operacje arytmetyczne | Podstawowy | 10 min |
| `ex3-loop.asm` | Pętla (suma 1..10) | Średni | 15 min |

**TOTAL:** ~40 minut (czytanie + eksperymentowanie)

---

## 🚀 Jak używać tych przykładów?

### Krok 1: Przeczytaj kod
```bash
cat ex0-hello.asm
```

Przeczytaj komentarze - wszystko jest wyjaśnione!

### Krok 2: Skompiluj
```bash
nasm -f elf64 ex0-hello.asm -o ex0-hello.o
ld ex0-hello.o -o ex0-hello
```

### Krok 3: Uruchom
```bash
./ex0-hello
```

### Krok 4 (opcjonalnie): Debuguj
```bash
# Kompilacja z informacjami debugowania
nasm -f elf64 -g -F dwarf ex0-hello.asm -o ex0-hello.o
ld ex0-hello.o -o ex0-hello

# Uruchom w GDB
gdb ./ex0-hello
```

---

## 🔍 Debugowanie w GDB

### Podstawowe komendy:
```bash
# Start debuggera
gdb ./program

# W GDB:
(gdb) break _start          # Ustaw breakpoint na początku
(gdb) run                   # Uruchom program
(gdb) info registers        # Pokaż wszystkie rejestry
(gdb) info registers rax    # Pokaż konkretny rejestr
(gdb) stepi                 # Wykonaj JEDNĄ instrukcję
(gdb) continue              # Kontynuuj do końca
(gdb) quit                  # Wyjdź z GDB
```

### Podgląd pamięci:
```bash
# x = examine (podgląd pamięci)
# Format: x/[liczba][format][rozmiar] adres

(gdb) x/d &wynik           # Pokaż zmienną jako decimal
(gdb) x/x &wynik           # Pokaż jako hex
(gdb) x/t &wynik           # Pokaż jako binary
(gdb) x/4d &tablica        # Pokaż 4 elementy tablicy

# Formaty:
# d = decimal (dziesiętnie)
# x = hex (szesnastkowo)
# t = binary (binarnie)
# s = string (tekst)
```

---

## 📖 Przykład sesji GDB (ex1-variables)
```bash
$ nasm -f elf64 -g -F dwarf ex1-variables.asm -o ex1-variables.o
$ ld ex1-variables.o -o ex1-variables
$ gdb ./ex1-variables

(gdb) break _start
Breakpoint 1 at 0x401000

(gdb) run
Starting program: ./ex1-variables
Breakpoint 1, 0x0000000000401000 in _start ()

(gdb) x/d &x
0x402000:	10

(gdb) x/d &y
0x402004:	20

(gdb) x/d &z
0x402008:	0

(gdb) stepi
...

(gdb) info registers eax
eax            0xa                 10

(gdb) stepi
...

(gdb) info registers eax
eax            0x1e                30

(gdb) x/d &z
0x402008:	30

(gdb) quit
```

---

## 💡 Co można zmodyfikować? (eksperymenty)

### ex0-hello.asm
- Zmień tekst na własny
- Dodaj drugą linię (drugi syscall write)
- Wypisz tekst 3 razy (pętla)

### ex1-variables.asm
- Dodaj czwartą zmienną `w`
- Oblicz: `w = (x + y) * 2`
- Sprawdź w GDB

### ex2-operations.asm
- Dodaj dzielenie (DIV instruction)
- Oblicz: `(a + b) * (a - b)`
- Dodaj więcej zmiennych

### ex3-loop.asm
- Zmień `n` na 100
- Policz sumę liczb parzystych: 2+4+6+...+20
- Policz iloczyn: 1*2*3*...*5 (silnia!)

---

## ❓ Pytania i odpowiedzi

### Q: Dlaczego `mov rsi, msg` a nie `mov rsi, [msg]`?

**A:** 
- `msg` = ADRES (potrzebujemy wskaźnika do stringa)
- `[msg]` = WARTOŚĆ (pierwsze 8 bajtów stringa)

Syscall `write` potrzebuje ADRESU bufora, nie wartości!

### Q: Czym różni się `add eax, [x]` od `add eax, x`?

**A:**
- `add eax, [x]` → eax = eax + **wartość x** (np. + 10)
- `add eax, x` → eax = eax + **adres x** (np. + 0x402000)

Prawie zawsze chcesz nawiasy!

### Q: Dlaczego `xor rdi, rdi` zamiast `mov rdi, 0`?

**A:** XOR jest szybszy:
- `xor rdi, rdi` → 3 bajty w kodzie maszynowym
- `mov rdi, 0` → 7 bajtów

Dla procesora: XOR anything z samym sobą = zawsze 0.

### Q: Co to znaczy `equ $ - msg`?

**A:**
- `$` = aktualny adres w pamięci
- `msg` = adres początku stringa
- `$ - msg` = różnica = długość stringa

To jest **compile-time constant** (obliczane przez assembler, nie w runtime).

### Q: Dlaczego `dd` a nie `db` dla liczb?

**A:**
- `db` = define byte (1 bajt, 0-255)
- `dw` = define word (2 bajty, 0-65535)
- `dd` = define doubleword (4 bajty, 0-4294967295)
- `dq` = define quadword (8 bajtów)

Dla liczb całkowitych używamy `dd` (32-bit) lub `dq` (64-bit).

---

## 🎯 Następny krok

Gdy zrozumiesz te przykłady, przejdź do:
```
cd ../02-exercises
```

Tam czekają zadania do samodzielnego rozwiązania!