; ============================================
; ROZWIĄZANIE: Silnia (Factorial)
; ============================================

section .data
    n dq 5
    wynik dq 0

section .text
    global _start

_start:
    ; ========================================
    ; Oblicz n! iteracyjnie
    ; ========================================
    
    mov rax, 1          ; wynik = 1
    mov rcx, 1          ; i = 1
    mov rbx, [n]        ; rbx = n
    
    ; Edge case: n=0 lub n=1
    cmp rbx, 1
    jle zapisz          ; Jeśli n<=1, wynik=1 (już w rax)
    
petla:
    ; Sprawdź czy i > n
    cmp rcx, rbx
    jg zapisz           ; Jeśli i > n, koniec
    
    ; wynik = wynik * i
    imul rax, rcx       ; rax = rax * rcx
    
    ; i++
    inc rcx
    
    ; Powtórz
    jmp petla

zapisz:
    mov [wynik], rax    ; Zapisz wynik
    
    ; Exit
    mov rax, 60
    xor rdi, rdi
    syscall

; ============================================
; NOTATKI:
; 
; 1. Edge case n=0:
;    Matematycznie 0! = 1, więc na początku
;    wynik=1, i jeśli n=0, od razu zapisujemy.
; 
; 2. Użycie imul (signed multiply):
;    W tym przypadku liczby są dodatnie,
;    więc imul i mul dadzą ten sam wynik.
;    imul ma wygodniejszą składnię.
; 
; 3. Overflow:
;    Dla n>20, silnia przekracza 64 bity!
;    Można to sprawdzić flagą OF (overflow flag).
; ============================================