; ============================================
; SELF-STUDY TASK 5: Potęgowanie (a^b)
; ============================================
; OPIS:
; Oblicz a^b (a do potęgi b).
; 
; Przykłady:
;   2^3 = 8
;   5^4 = 625
;   10^2 = 100
;   a^0 = 1 (z definicji)
; 
; ALGORYTM:
;   wynik = 1
;   for i = 1 to b:
;       wynik = wynik * a
; ============================================
; TRUDNOŚĆ: ⭐⭐⭐ (trudna - pętle zagnieżdżone możliwe)
; CZAS: 60 minut
; ============================================

section .data
    a dq 2          ; Podstawa
    b dq 10         ; Wykładnik
    wynik dq 0      ; a^b (2^10 = 1024)

section .text
    global _start

_start:
    ; ========================================
    ; TODO: Oblicz a^b
    ; ========================================
    ; 
    ; ALGORYTM:
    ; 1. wynik = 1 (rax)
    ; 2. i = 0 (rcx)
    ; 3. Pętla od 0 to b-1:
    ;      wynik = wynik * a
    ;      i++
    ; 4. Zapisz wynik
    ; 
    ; WSKAZÓWKI:
    ; - rax = wynik (akumulator)
    ; - rcx = i (licznik)
    ; - rbx = a (podstawa)
    ; - r8 = b (wykładnik)
    ; - Mnożenie: imul rax, rbx
    ; 
    ; EDGE CASE: b=0
    ; - a^0 = 1 dla każdego a
    ; - Sprawdź na początku!
    
    ; TWÓJ KOD TUTAJ:
    
    
    
    
    
    
    
    
    
    
    
    
    ; Exit
    mov rax, 60
    xor rdi, rdi
    syscall

; ============================================
; SPRAWDZENIE:
; 
; $ nasm -f elf64 task5-power.asm -o task5.o
; $ ld task5.o -o task5
; $ gdb ./task5
; (gdb) break _start
; (gdb) run
; (gdb) continue
; (gdb) x/d &wynik
; 
; OCZEKIWANE WYNIKI:
;   2^3 = 8
;   2^10 = 1024
;   5^4 = 625
;   10^0 = 1
;   10^1 = 10
; ============================================

; ============================================
; BONUS: Szybkie potęgowanie (fast exponentiation)
; 
; Jeśli chcesz wyzwania, zaimplementuj algorytm
; "exponentiation by squaring":
; 
; power(a, b):
;     if b == 0: return 1
;     if b % 2 == 0:
;         temp = power(a, b/2)
;         return temp * temp
;     else:
;         return a * power(a, b-1)
; 
; To jest O(log b) zamiast O(b) - dużo szybsze!
; Wymaga rekurencji lub stack manipulation.
; ============================================