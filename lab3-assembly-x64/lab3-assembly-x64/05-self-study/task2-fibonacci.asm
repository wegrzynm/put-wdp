; ============================================
; SELF-STUDY TASK 2: Ciąg Fibonacciego
; ============================================
; OPIS:
; Oblicz n-ty wyraz ciągu Fibonacciego:
;   F(0) = 0
;   F(1) = 1
;   F(n) = F(n-1) + F(n-2)
; 
; Przykłady:
;   F(5) = 5:  0, 1, 1, 2, 3, 5
;   F(10) = 55: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
; 
; ALGORYTM (iteracyjny - łatwiejszy):
;   a = 0, b = 1
;   for i = 2 to n:
;       temp = a + b
;       a = b
;       b = temp
;   return b
; ============================================
; TRUDNOŚĆ: ⭐⭐⭐ (trudna - rekurencja opcjonalna)
; CZAS: 45 minut
; ============================================

section .data
    n dq 10         ; Oblicz F(10) = 55
    wynik dq 0      ; Tutaj zapisz wynik

section .text
    global _start

_start:
    ; ========================================
    ; TODO: Oblicz F(n) - Fibonacci
    ; ========================================
    ; 
    ; ALGORYTM ITERACYJNY (łatwiejszy):
    ; 
    ; if n == 0: return 0
    ; if n == 1: return 1
    ; 
    ; a = 0
    ; b = 1
    ; for i = 2 to n:
    ;     temp = a + b
    ;     a = b
    ;     b = temp
    ; return b
    ; 
    ; WSKAZÓWKI:
    ; - rax = a (poprzedni wyraz)
    ; - rbx = b (aktualny wyraz)
    ; - rcx = i (licznik)
    ; - rdx = temp (tymczasowa)
    ; - r8 = n (przechowaj n)
    
    ; TWÓJ KOD TUTAJ:
    
    
    
    
    
    
    
    
    
    
    
    
    ; Exit
    mov rax, 60
    xor rdi, rdi
    syscall

; ============================================
; SPRAWDZENIE:
; 
; $ nasm -f elf64 task2-fibonacci.asm -o task2.o
; $ ld task2.o -o task2
; $ gdb ./task2
; (gdb) break _start
; (gdb) run
; (gdb) continue
; (gdb) x/d &wynik
; 
; OCZEKIWANE WYNIKI:
;   n=0  → wynik=0
;   n=1  → wynik=1
;   n=5  → wynik=5
;   n=10 → wynik=55
;   n=20 → wynik=6765
; ============================================

; ============================================
; BONUS: Wersja rekurencyjna
; 
; Jeśli czujesz się na siłach, napisz wersję
; rekurencyjną (jak na wykładzie):
; 
; fibonacci(n):
;     if n <= 1: return n
;     return fibonacci(n-1) + fibonacci(n-2)
; 
; UWAGA: Wymaga obsługi stosu (push/pop)!
; ============================================