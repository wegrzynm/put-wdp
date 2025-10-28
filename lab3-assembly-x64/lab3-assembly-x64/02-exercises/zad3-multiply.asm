; ============================================
; ZADANIE 3: Mnożenie w pętli (MINIMUM)
; ============================================
; OPIS:
; Napisz program który mnoży 7 * 6 BEZ użycia instrukcji MUL.
; Użyj pętli i dodawania.
; 
; Algorytm:
;   wynik = 0
;   for i = 1 to 6:
;       wynik = wynik + 7
; 
; Sprawdzenie w GDB:
;   (gdb) x/d &wynik  → powinno być: 42
; ============================================
; KOMPILACJA:
;   nasm -f elf64 zad3-multiply.asm -o zad3-multiply.o
;   ld zad3-multiply.o -o zad3-multiply
;   gdb ./zad3-multiply
; ============================================
; PUNKTY: 1 pkt (MINIMUM)
; ============================================

section .data
    ; Mnożenie: 7 * 6
    multiplicand dq 7       ; Mnożna (to co dodajemy)
    multiplier dq 6         ; Mnożnik (ile razy)
    
    wynik dq 0              ; Wynik (7 * 6 = 42)

section .text
    global _start

_start:
    ; ========================================
    ; TODO: Zaimplementuj mnożenie przez pętlę
    ; ========================================
    ; 
    ; ALGORYTM:
    ; 1. rax = 0 (akumulator wyniku)
    ; 2. rcx = 6 (licznik pętli)
    ; 3. Pętla:
    ;      a) Dodaj 7 do rax
    ;      b) Zmniejsz rcx o 1
    ;      c) Jeśli rcx != 0, wróć do (a)
    ; 4. Zapisz rax do 'wynik'
    
    ; TWÓJ KOD TUTAJ:
    xor rax, rax
    mov rcx, 1
    mov rbx, [multiplier]
    
    petla:
      cmp rcx, rbx
      jg koniec
      
      add rax, rcx
      inc rcx
      jmp petla
      
    koniec:
      mov [wynik], rax
    
    ; Exit
    mov rax, 60
    xor rdi, rdi
    syscall

; ============================================
; WSKAZÓWKI:
; 
; SZABLON PĘTLI (metoda 1 - LOOP instruction):
; 
;   xor rax, rax                ; wynik = 0
;   mov rcx, [multiplier]       ; licznik = 6
;   
; petla:
;   add rax, [multiplicand]     ; wynik += 7
;   loop petla                  ; rcx--, jeśli != 0 skocz
;   
;   mov [wynik], rax            ; zapisz
; 
; ----------------------------------------
; 
; SZABLON PĘTLI (metoda 2 - DEC + JNZ):
; 
;   xor rax, rax                ; wynik = 0
;   mov rcx, [multiplier]       ; licznik = 6
;   
; petla:
;   add rax, [multiplicand]     ; wynik += 7
;   dec rcx                     ; rcx--
;   jnz petla                   ; jeśli rcx != 0, skocz
;   
;   mov [wynik], rax            ; zapisz
; 
; ----------------------------------------
; 
; UWAGA: Używamy rcx (64-bit) dla licznika pętli!
;        Instrukcja LOOP w x64 używa rcx (nie ecx).
; 
; SPRAWDZENIE w GDB:
;   $ gdb ./zad3-multiply
;   (gdb) break petla
;   (gdb) run
;   (gdb) info registers rax rcx
;   (gdb) continue 6     → wykonaj pętlę 6 razy
;   (gdb) x/d &wynik
; 
; OCZEKIWANY WYNIK: 42
; ============================================