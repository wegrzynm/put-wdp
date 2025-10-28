; ============================================
; ZADANIE 4: Suma tablicy (ROZSZERZONE)
; ============================================
; OPIS:
; Napisz program który oblicza sumę elementów tablicy:
; tablica = [5, 10, 15, 20, 25]
; suma = 5 + 10 + 15 + 20 + 25 = 75
; 
; Użyj pętli do iteracji po tablicy.
; ============================================
; KOMPILACJA:
;   nasm -f elf64 zad4-array-sum.asm -o zad4-array-sum.o
;   ld zad4-array-sum.o -o zad4-array-sum
;   gdb ./zad4-array-sum
; ============================================
; PUNKTY: 2 pkt (ROZSZERZONE)
; ============================================

section .data
    ; Tablica 5 elementów (każdy po 8 bajtów = dq)
    tablica dq 5, 10, 15, 20, 25
    rozmiar dq 5        ; Liczba elementów
    
    suma dq 0           ; Wynik (powinno być 75)

section .text
    global _start

_start:
    ; ========================================
    ; TODO: Oblicz sumę elementów tablicy
    ; ========================================
    ; 
    ; ALGORYTM:
    ; 1. rax = 0 (akumulator sumy)
    ; 2. rcx = 5 (licznik elementów)
    ; 3. rsi = adres tablicy (wskaźnik)
    ; 4. Pętla:
    ;      a) Dodaj [rsi] do rax
    ;      b) Przesuń rsi o 8 bajtów (następny element)
    ;      c) Zmniejsz rcx o 1
    ;      d) Jeśli rcx != 0, wróć do (a)
    ; 5. Zapisz rax do 'suma'
    
    ; TWÓJ KOD TUTAJ:
    
    
    
    
    
    
    
    
    
    
    
    ; Exit
    mov rax, 60
    xor rdi, rdi
    syscall

; ============================================
; WSKAZÓWKI:
; 
; DOSTĘP DO TABLICY:
; 
; Tablica w pamięci (każdy element = 8 bajtów):
; ┌────┬────┬────┬────┬────┐
; │ 5  │ 10 │ 15 │ 20 │ 25 │
; └────┴────┴────┴────┴────┘
;  ^rsi      ^rsi+8   ^rsi+16
; 
; Aby przejść do następnego elementu:
;   add rsi, 8    (bo dq = 8 bajtów)
; 
; UWAGA: W x64 adresy to 64 bity, więc używamy
;        RSI (nie esi!) dla wskaźnika!
; 
; ----------------------------------------
; 
; SZABLON ROZWIĄZANIA:
; 
;   xor rax, rax                ; suma = 0
;   mov rcx, [rozmiar]          ; licznik = 5
;   mov rsi, tablica            ; wskaźnik na tablicę
;   
; petla:
;   add rax, [rsi]              ; suma += tablica[i]
;   add rsi, 8                  ; przejdź do następnego (8 bajtów!)
;   dec rcx                     ; licznik--
;   jnz petla                   ; jeśli != 0, kontynuuj
;   
;   mov [suma], rax             ; zapisz wynik
; 
; ----------------------------------------
; 
; DLACZEGO rsi (64-bit) a nie esi (32-bit)?
; 
; W x64, ADRESY są 64-bitowe!
; - rsi = 64-bit register (dla adresów)
; - esi = 32-bit register (dla wartości)
; 
; Używanie esi dla adresu to ZŁA PRAKTYKA w x64!
; (Może działać dla małych adresów, ale nie zawsze)
; 
; ----------------------------------------
; 
; SPRAWDZENIE w GDB:
;   $ gdb ./zad4-array-sum
;   (gdb) x/5d &tablica   → pokaż tablicę
;   (gdb) break petla
;   (gdb) run
;   (gdb) info registers rax rsi rcx
;   (gdb) continue 5      → wykonaj pętlę 5 razy
;   (gdb) x/d &suma
; 
; OCZEKIWANY WYNIK: 75
; ============================================