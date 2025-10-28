; ============================================
; ZADANIE 1: Hello, [Twoje Imię]! (MINIMUM)
; ============================================
; OPIS:
; Zmodyfikuj program tak, aby wypisywał:
; "Hello, [Twoje Imię]!"
; 
; Np. "Hello, Bartosz!"
;     "Hello, Anna!"
; ============================================
; KOMPILACJA:
;   nasm -f elf64 zad1-hello.asm -o zad1-hello.o
;   ld zad1-hello.o -o zad1-hello
;   ./zad1-hello
; ============================================
; PUNKTY: 1 pkt (MINIMUM)
; ============================================

section .data
    ; TODO: Zmień komunikat na własny
    ; Pamiętaj o 0xA (newline) na końcu!
    
    msg db 'Hello, Mateusz!', 0xA    ; ← ZMIEŃ TO!
    len equ $ - msg

section .text
    global _start

_start:
    ; Wypisz komunikat
    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, len
    syscall
    
    ; Exit
    mov rax, 60
    xor rdi, rdi
    syscall

; ============================================
; WSKAZÓWKI:
; 
; 1. Zmień tylko linię z "msg db ..."
; 2. Pamiętaj o 0xA na końcu (newline)
; 3. "len equ $ - msg" automatycznie obliczy długość
; 4. Skompiluj i uruchom
; 
; PRZYKŁAD:
; msg db 'Hello, Bartosz!', 0xA
; ============================================