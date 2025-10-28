; ============================================
; ZADANIE 2: Prosty kalkulator (MINIMUM)
; ============================================
; OPIS:
; Napisz program który:
; 1. Dodaje dwie liczby: 23 + 19
; 2. Odejmuje dwie liczby: 50 - 12
; 3. Zapisuje wyniki do zmiennych
; 
; Sprawdzenie w GDB:
;   (gdb) x/d &suma      → powinno być: 42
;   (gdb) x/d &roznica   → powinno być: 38
; ============================================
; KOMPILACJA:
;   nasm -f elf64 zad2-calculator.asm -o zad2-calculator.o
;   ld zad2-calculator.o -o zad2-calculator
;   gdb ./zad2-calculator
; ============================================
; PUNKTY: 1 pkt (MINIMUM)
; ============================================

section .data
    ; Dane wejściowe
    a dq 23
    b dq 19
    c dq 50
    d dq 12
    
    ; Wyniki (do wypełnienia przez program)
    suma dq 0       ; Tutaj zapisz: a + b
    roznica dq 0    ; Tutaj zapisz: c - d

section .text
    global _start

_start:
    ; ========================================
    ; TODO: Oblicz sumę (a + b)
    ; ========================================
    ; Wskazówki:
    ; 1. Załaduj 'a' do rejestru (np. rax)
    ; 2. Dodaj 'b' 
    ; 3. Zapisz wynik do 'suma'
    
    ; TWÓJ KOD TUTAJ:
    mov rax, [a]
    add rax, [b]
    mov [suma], rax
    
    
    ; ========================================
    ; TODO: Oblicz różnicę (c - d)
    ; ========================================
    ; Wskazówki:
    ; 1. Załaduj 'c' do rejestru (np. rax)
    ; 2. Odejmij 'd'
    ; 3. Zapisz wynik do 'roznica'
    
    ; TWÓJ KOD TUTAJ:
    mov rax, [c]
    sub rax, [d]
    mov [roznica], rax
    
    
    ; Exit
    mov rax, 60
    xor rdi, rdi
    syscall

; ============================================
; WSKAZÓWKI:
; 
; SCHEMAT OPERACJI (LOAD-OPERATE-STORE):
; 
; Dodawanie:
;   mov rax, [a]        ; LOAD
;   add rax, [b]        ; OPERATE
;   mov [suma], rax     ; STORE
; 
; Odejmowanie:
;   mov rax, [c]        ; LOAD
;   sub rax, [d]        ; OPERATE
;   mov [roznica], rax  ; STORE
; 
; UWAGA: Używamy rax (64-bit) i dq (64-bit)
;        dla konsekwencji w x64!
; 
; SPRAWDZENIE w GDB:
;   $ gdb ./zad2-calculator
;   (gdb) break _start
;   (gdb) run
;   (gdb) continue
;   (gdb) x/d &suma
;   (gdb) x/d &roznica
; 
; OCZEKIWANE WYNIKI:
;   suma = 42 (23 + 19)
;   roznica = 38 (50 - 12)
; ============================================