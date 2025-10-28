; ============================================
; SELF-STUDY TASK 1: Silnia (Factorial)
; ============================================
; OPIS:
; Oblicz silnię liczby n: n! = 1 * 2 * 3 * ... * n
; 
; Przykłady:
;   5! = 1 * 2 * 3 * 4 * 5 = 120
;   6! = 1 * 2 * 3 * 4 * 5 * 6 = 720
;   0! = 1 (z definicji)
; 
; ALGORYTM (iteracyjny):
;   wynik = 1
;   for i = 1 to n:
;       wynik = wynik * i
; ============================================
; TRUDNOŚĆ: ⭐⭐ (średnia)
; CZAS: 30 minut
; ============================================

section .data
    n dq 5          ; Oblicz 5! = 120
    wynik dq 0      ; Tutaj zapisz wynik

section .text
    global _start

_start:
    ; ========================================
    ; TODO: Oblicz n! (silnia)
    ; ========================================
    ; 
    ; ALGORYTM:
    ; 1. wynik = 1 (rax)
    ; 2. i = 1 (rcx)
    ; 3. Pętla od 1 do n:
    ;      wynik = wynik * i
    ;      i++
    ; 4. Zapisz wynik
    ; 
    ; WSKAZÓWKI:
    ; - Użyj rax jako akumulator (wynik)
    ; - Użyj rcx jako licznik (i)
    ; - Użyj rbx do przechowania n
    ; - Mnożenie: imul rax, rcx (rax = rax * rcx)
    ; - Pętla: inc rcx + cmp rcx, rbx + jle
    
    ; TWÓJ KOD TUTAJ:
    
    
    
    
    
    
    
    
    
    
    
    ; Exit
    mov rax, 60
    xor rdi, rdi
    syscall

; ============================================
; SPRAWDZENIE:
; 
; $ nasm -f elf64 task1-factorial.asm -o task1.o
; $ ld task1.o -o task1
; $ gdb ./task1
; (gdb) break _start
; (gdb) run
; (gdb) continue
; (gdb) x/d &wynik
; 
; OCZEKIWANE WYNIKI:
;   n=5  → wynik=120
;   n=6  → wynik=720
;   n=10 → wynik=3628800
; 
; UWAGA: Dla n>20 może być overflow (liczby są ogromne!)
; ============================================

; ============================================
; EDGE CASES:
; 
; Co jeśli n=0?
; - Matematycznie: 0! = 1
; - Twoja funkcja powinna zwrócić 1
; 
; Co jeśli n=1?
; - 1! = 1
; 
; Sprawdź czy Twój kod obsługuje te przypadki!
; ============================================