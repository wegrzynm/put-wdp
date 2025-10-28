# 🔧 Setup - Instalacja środowiska NASM x64

## Szybki start (Ubuntu/Linux w labie)
```bash
# 1. Przejdź do folderu setup
cd lab3-assembly-x64/00-setup

# 2. Uruchom skrypt instalacyjny
chmod +x install.sh
./install.sh
```

Jeśli wszystko poszło dobrze, zobaczysz:
```
✅ Architektura OK (x86_64)
✅ NASM: NASM version 2.xx.xx
✅ Linker (ld): OK
✅ Kompilacja OK!
Hello from NASM x64!
🎉 Wszystko działa! Gotowy do laboratorium.
```

---

## Instalacja ręczna (jeśli skrypt nie działa)

### Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install nasm build-essential
```

### Fedora/RHEL:
```bash
sudo dnf install nasm gcc
```

### Arch Linux:
```bash
sudo pacman -S nasm gcc
```

### macOS:
```bash
brew install nasm
```

---

## Weryfikacja instalacji
```bash
# Sprawdź wersję NASM
nasm -v

# Powinno wyświetlić coś w stylu:
# NASM version 2.15.05

# Sprawdź linker
ld --version
```

---

## Test kompilacji

### Krok 1: Stwórz plik testowy

Stwórz plik `test.asm`:
```asm
section .data
    msg db 'Test OK!', 0xA
    len equ $ - msg

section .text
    global _start

_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, len
    syscall
    
    mov rax, 60
    xor rdi, rdi
    syscall
```

### Krok 2: Skompiluj
```bash
# Asemblacja (źródło → kod maszynowy)
nasm -f elf64 test.asm -o test.o

# Linkowanie (kod maszynowy → wykonywalny program)
ld test.o -o test

# Uruchomienie
./test
```

**Oczekiwany output:**
```
Test OK!
```

---

## Proces kompilacji - co się dzieje?
```
test.asm  →  [NASM]  →  test.o  →  [LD]  →  test (wykonywalny)
(źródło)    (assembler) (object)  (linker)  (program)
```

### 1. NASM (Assembler):
- Tłumaczy mnemoniki (mov, add) → kody maszynowe (binarnie)
- Generuje plik `.o` (object file)
- Format: ELF64 (Executable and Linkable Format, 64-bit)

### 2. LD (Linker):
- Łączy pliki `.o` w jeden wykonywalny program
- Ustawia punkt wejścia (`_start`)
- Tworzy nagłówki ELF

### 3. Kernel:
- Ładuje program do pamięci
- Wykonuje instrukcje procesora

---

## Kompilacja z debugowaniem

Jeśli chcesz używać GDB (debuggera):
```bash
# Dodaj informacje debugowania (-g)
nasm -f elf64 -g -F dwarf test.asm -o test.o
ld test.o -o test

# Uruchom w debuggerze
gdb ./test
```

W GDB:
```
(gdb) break _start
(gdb) run
(gdb) info registers
(gdb) stepi
(gdb) continue
```

---

## Makefile (opcjonalnie, dla wygody)

Stwórz plik `Makefile`:
```makefile
AS = nasm
ASFLAGS = -f elf64 -g -F dwarf
LD = ld

# Zmień na nazwę twojego programu
TARGET = test

all: $(TARGET)

$(TARGET): $(TARGET).o
	$(LD) $< -o $@

$(TARGET).o: $(TARGET).asm
	$(AS) $(ASFLAGS) $< -o $@

clean:
	rm -f *.o $(TARGET)

run: $(TARGET)
	./$(TARGET)

.PHONY: all clean run
```

Użycie:
```bash
make           # kompiluje
make run       # kompiluje i uruchamia
make clean     # usuwa pliki tymczasowe
```

---

## Troubleshooting

### Problem: "command not found: nasm"
**Rozwiązanie:** NASM nie jest zainstalowany. Uruchom `install.sh` lub zainstaluj ręcznie.

### Problem: "cannot find -lc"
**Rozwiązanie:** Używamy `ld` zamiast `gcc`, więc nie linkujemy z biblioteką C. To jest OK.

### Problem: "Segmentation fault"
**Możliwe przyczyny:**
1. Zapomniałeś wywołać `syscall`
2. Zapomniałeś zakończyć program (`sys_exit`)
3. Błędny dostęp do pamięci

**Debug:**
```bash
gdb ./program
(gdb) run
(gdb) where
```

### Problem: "Wrong ELF class: ELFCLASS32"
**Rozwiązanie:** Kompilujesz jako 32-bit zamiast 64-bit. Użyj `-f elf64`.

### Problem: macOS "ld: unknown option: -m"
**Rozwiązanie:** macOS używa innego linkera. Dla macOS lepiej użyć Dockera lub Linux VM.

---

## Backup: Online compiler

Jeśli nie możesz zainstalować NASM lokalnie:

1. **OnlineGDB** (łatwy)
   - https://www.onlinegdb.com/
   - Wybierz "Assembly (NASM)"
   - Wklej kod
   - Kliknij "Run"

2. **Godbolt Compiler Explorer** (zaawansowany)
   - https://godbolt.org/
   - Świetny do analizy kodu
   - Pokazuje jak C przekłada się na Assembly

---

## 🎯 Gotowy?

Jeśli widzisz "Hello from NASM x64!" po uruchomieniu `test-hello`, jesteś gotowy!

**Następny krok:** Przejdź do `01-examples/` i zobacz przykłady kodu.