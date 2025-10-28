; ============================================
; Przykład 2: Podstawowe operacje arytmetyczne (x64)
; Dodawanie, odejmowanie, mnożenie
; ============================================
; KOMPILACJA:
;   nasm -f elf64 ex2-operations.asm -o ex2-operations.o
;   ld ex2-operations.o -o ex2-operations
;   gdb ./ex2-operations
; ============================================

section .data
    a dq 15
    b dq 7
    
    suma dq 0       ; a + b
    roznica dq 0    ; a - b
    iloczyn dq 0    ; a * b

section .text
    global _start

_start:
    ; ========================================
    ; OPERACJA 1: Dodawanie
    ; suma = a + b
    ; ========================================
    
    mov rax, [a]        ; LOAD: rax = 15
    add rax, [b]        ; OPERATE: rax = 15 + 7 = 22
    mov [suma], rax     ; STORE: suma = 22
    
    ; ========================================
    ; OPERACJA 2: Odejmowanie
    ; roznica = a - b
    ; ========================================
    
    mov rax, [a]        ; LOAD: rax = 15
    sub rax, [b]        ; OPERATE: rax = 15 - 7 = 8
    mov [roznica], rax  ; STORE: roznica = 8
    
    ; ========================================
    ; OPERACJA 3: Mnożenie
    ; iloczyn = a * b
    ; ========================================
    ; UWAGA: Instrukcja MUL ma specjalną składnię!
    ; mul operand → mnoży rax * operand
    ;            → wynik w rdx:rax (128 bitów!)
    ;            → rdx = górne 64 bity
    ;            → rax = dolne 64 bity
    
    mov rax, [a]        ; LOAD: rax = 15
    mov rbx, [b]        ; LOAD: rbx = 7
    mul rbx             ; OPERATE: rax = rax * rbx = 105
                        ; (rdx = 0, bo mały wynik)
    mov [iloczyn], rax  ; STORE: iloczyn = 105
    
    ; ========================================
    ; ALTERNATYWA: Mnożenie bez MUL
    ; (jak na wykładzie: 7 * 6 przez dodawanie)
    ; ========================================
    ; Pętla 7 razy:
    ;   wynik = wynik + 15
    ;
    ; mov rcx, [b]        ; licznik = 7
    ; xor rax, rax        ; rax = 0 (wynik)
    ; petla:
    ;     add rax, [a]    ; rax = rax + 15
    ;     dec rcx         ; rcx--
    ;     jnz petla       ; jeśli rcx != 0, skocz
    ; mov [iloczyn], rax
    
    ; ========================================
    ; SPRAWDZENIE w GDB:
    ; ========================================
    ; (gdb) break _start
    ; (gdb) run
    ; (gdb) x/3d &suma    → pokaż 3 zmienne (suma, roznica, iloczyn)
    ; (gdb) continue
    ; (gdb) x/3d &suma    → sprawdź wyniki końcowe
    ; ========================================
    
    ; Exit
    mov rax, 60
    xor rdi, rdi
    syscall

; ============================================
; INSTRUKCJE ARYTMETYCZNE (x64):
;
; ADD destination, source
;   destination = destination + source
;   Przykład: add rax, rbx  → rax = rax + rbx
;
; SUB destination, source
;   destination = destination - source
;   Przykład: sub rax, rbx  → rax = rax - rbx
;
; MUL source (unsigned)
;   rdx:rax = rax * source (128-bit result!)
;   Przykład: mul rbx → rdx:rax = rax * rbx
;
; IMUL destination, source (signed)
;   destination = destination * source
;   Przykład: imul rax, rbx → rax = rax * rbx
;
; INC destination
;   destination = destination + 1
;   Przykład: inc rax → rax++
;
; DEC destination
;   destination = destination - 1
;   Przykład: dec rax → rax--
;
; NEG destination
;   destination = -destination (negacja w U2)
;   Przykład: neg rax → rax = -rax
;
; UWAGA: W x64 używamy rax, rbx, rcx, rdx (64-bit)
;        Możesz też użyć eax, ebx, etc. (32-bit) ale
;        dla konsekwencji używamy pełnych 64-bit rejestrów
; ============================================