; ============================================
; SELF-STUDY TASK 4: strcmp - porównanie stringów
; ============================================
; OPIS:
; Porównaj dwa stringi. Zwróć:
;   0  jeśli równe
;   -1 jeśli string1 < string2
;   +1 jeśli string1 > string2
; 
; Przykłady:
;   "abc" vs "abc" → 0 (równe)
;   "abc" vs "abd" → -1 (a<b, więc pierwszy jest mniejszy)
;   "xyz" vs "abc" → +1 (x>a)
; 
; ALGORYTM:
;   i = 0
;   while string1[i] != '\0' AND string2[i] != '\0':
;       if string1[i] != string2[i]:
;           return sign(string1[i] - string2[i])
;       i++
;   # Jeśli dotarliśmy tu, jeden string się skończył
;   if string1[i] == string2[i]: return 0
;   if string1[i] == 0: return -1 (pierwszy krótszy)
;   else: return +1
; ============================================
; TRUDNOŚĆ: ⭐⭐⭐ (trudna)
; CZAS: 45 minut
; ============================================

section .data
    string1 db "Hello", 0
    string2 db "Hello", 0
    wynik dq 0          ; 0 = równe, -1 = s1<s2, +1 = s1>s2

section .text
    global _start

_start:
    ; ========================================
    ; TODO: Porównaj string1 i string2
    ; ========================================
    ; 
    ; ALGORYTM (uproszczony):
    ; 1. rsi = adres string1
    ; 2. rdi = adres string2
    ; 3. Pętla:
    ;      a) Pobierz bajt z [rsi] i [rdi]
    ;      b) Jeśli oba == 0: stringi równe, zwróć 0
    ;      c) Jeśli różne: porównaj i zwróć -1 lub +1
    ;      d) Jeśli równe: rsi++, rdi++, kontynuuj
    ; 
    ; WSKAZÓWKI:
    ; - movzx al, byte [rsi] (załaduj bajt do al, reszta=0)
    ; - movzx bl, byte [rdi]
    ; - cmp al, bl
    ; - jl mniejszy (jump if less)
    ; - jg wiekszy (jump if greater)
    ; - je rowne (jump if equal)
    
    ; TWÓJ KOD TUTAJ:
    
    
    
    
    
    
    
    
    
    
    
    
    
    ; Exit
    mov rax, 60
    xor rdi, rdi
    syscall

; ============================================
; SPRAWDZENIE:
; 
; $ nasm -f elf64 task4-strcmp.asm -o task4.o
; $ ld task4.o -o task4
; $ gdb ./task4
; (gdb) break _start
; (gdb) run
; (gdb) continue
; (gdb) x/d &wynik
; 
; TEST CASES:
;   "Hello" vs "Hello" → wynik=0
;   "abc" vs "abd" → wynik=-1
;   "xyz" vs "abc" → wynik=+1
;   "test" vs "testing" → wynik=-1 (krótszy)
; 
; Zmień stringi i przetestuj różne przypadki!
; ============================================

; ============================================
; DLACZEGO movzx?
; 
; movzx al, byte [rsi]
; - mov + zero-extend
; - al = 8-bitowy rejestr (dolna część rax)
; - Wypełnia resztę rax zerami
; 
; Alternatywa:
;   xor rax, rax
;   mov al, byte [rsi]
; 
; Oba działają, movzx jest krótsza.
; ============================================