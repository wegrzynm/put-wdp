# Demo 2: Compiler Explorer (Godbolt)

## 🌐 Online narzędzie do analizy kodu

**Link:** https://godbolt.org/

---

## 🎯 Co to jest Godbolt?

Compiler Explorer pokazuje **jak kod wysokiego poziomu (C/C++) przekłada się na Assembly**.

To narzędzie używane przez:
- Programistów do optymalizacji
- Security researchers do reverse engineering
- Hackerów do znajdowania exploitów

---

## 🚀 Live Demo (na ekranie)

### Krok 1: Otwórz Godbolt
```
https://godbolt.org/
```

### Krok 2: Wklej prosty kod C
```c
int suma(int a, int b) {
    return a + b;
}
```

### Krok 3: Zobacz Assembly (x86-64 gcc)
```asm
suma(int, int):
    push rbp
    mov rbp, rsp
    mov DWORD PTR [rbp-4], edi
    mov DWORD PTR [rbp-8], esi
    mov edx, DWORD PTR [rbp-4]
    mov eax, DWORD PTR [rbp-8]
    add eax, edx
    pop rbp
    ret
```

### Krok 4: Włącz optymalizacje (-O3)
```asm
suma(int, int):
    lea eax, [rdi+rsi]    ; Tylko JEDNA instrukcja!
    ret
```

**WOW! Kompilator jest sprytny!**

---

## 💡 Eksperymenty dla studentów

### Eksperyment 1: Buffer
```c
char buffer[10];
```

**Pytanie:** Ile miejsca zajmie w assembly?  
**Odpowiedź:** Zobacz w Godbolt!

### Eksperyment 2: If-else
```c
int max(int a, int b) {
    if (a > b)
        return a;
    else
        return b;
}
```

**Pytanie:** Jakie instrukcje skoku użyje kompilator?  
**Odpowiedź:** `cmp`, `jle`, ...

### Eksperyment 3: Pętla
```c
int suma_100() {
    int s = 0;
    for (int i = 1; i <= 100; i++)
        s += i;
    return s;
}
```

**Z optymalizacją -O3:**
```asm
suma_100():
    mov eax, 5050    ; Kompilator OBLICZYŁ w compile-time!
    ret
```

**MAGIA!** Kompilator wie że 1+2+...+100 = 5050.

---

## 🔐 Zastosowania w Cybersecurity

### 1. Reverse Engineering
"Mam skompilowany program (bez źródeł). Co on robi?"
→ Używam Godbolt do nauki wzorców assembly.

### 2. Malware Analysis
"Ten plik .exe jest podejrzany. Analizuję w IDA Pro."
→ Rozumiem assembly dzięki ćwiczeniu z Godbolt.

### 3. Exploit Development
"Szukam buffer overflow w funkcji."
→ Godbolt pokazuje mi jak funkcja zarządza stosem.

### 4. Code Review
"Czy ten kod jest podatny na timing attack?"
→ Sprawdzam w assembly czy są warunkowe skoki.

---

## 🎓 Zadanie dla chętnych (self-study)

1. Wejdź na Godbolt
2. Napisz funkcję `factorial(n)` w C
3. Zobacz assembly dla:
   - Wersja bez optymalizacji
   - Wersja z -O3
4. Zrozum różnicę

**Bonus:** Spróbuj przepisać wygenerowany assembly do NASM i skompilować!

---

## 📚 Więcej narzędzi

- **Ghidra** (NSA): https://ghidra-sre.org/
- **IDA Pro**: Komercyjny disassembler
- **Radare2**: Open-source reverse engineering
- **GDB**: Debugger (już używaliśmy!)

---

## 🔗 Linki

- Godbolt: https://godbolt.org/
- Tutorial: https://www.youtube.com/results?search_query=compiler+explorer+tutorial
- Cheatsheet: https://github.com/mattgodbolt/compiler-explorer

---

**Czas demo:** 10 minut  
**Efekt:** "WOW, to tak działa!"