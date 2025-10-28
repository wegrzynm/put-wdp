; ============================================
; Przykład 3: Pętla - Suma 1+2+3+...+10 (x64)
; Pokazuje jak działa pętla w Assembly
; ============================================
; KOMPILACJA:
;   nasm -f elf64 ex3-loop.asm -o ex3-loop.o
;   ld ex3-loop.o -o ex3-loop
;   gdb ./ex3-loop
; ============================================

section .data
    n dq 10         ; Sumujemy od 1 do n
    wynik dq 0      ; Miejsce na wynik

section .text
    global _start

_start:
    ; ========================================
    ; ALGORYTM:
    ; wynik = 0
    ; for i = 1 to n:
    ;     wynik = wynik + i
    ; ========================================
    
    xor rax, rax        ; rax = 0 (akumulator wyniku)
    mov rcx, 1          ; rcx = 1 (licznik: od 1)
    mov rbx, [n]        ; rbx = 10 (górna granica)
    
petla_start:
    ; ----------------------------------------
    ; Sprawdź warunek: czy rcx <= rbx?
    ; ----------------------------------------
    cmp rcx, rbx        ; porównaj rcx z rbx
    jg petla_koniec     ; jeśli rcx > rbx, skocz do końca
    
    ; ----------------------------------------
    ; Ciało pętli: wynik = wynik + i
    ; ----------------------------------------
    add rax, rcx        ; rax = rax + rcx
    
    ; ----------------------------------------
    ; Inkrementacja: i++
    ; ----------------------------------------
    inc rcx             ; rcx = rcx + 1
    
    ; ----------------------------------------
    ; Powrót na początek pętli
    ; ----------------------------------------
    jmp petla_start     ; bezwarunkowy skok
    
petla_koniec:
    ; Zapisz wynik
    mov [wynik], rax    ; wynik = 55 (1+2+...+10)
    
    ; ========================================
    ; ALTERNATYWNA WERSJA: Instrukcja LOOP
    ; (działa w x86 i x64)
    ; ========================================
    ; xor rax, rax        ; wynik = 0
    ; mov rcx, [n]        ; licznik = 10
    ; mov rbx, 1          ; i = 1
    ; 
    ; petla:
    ;     add rax, rbx    ; wynik += i
    ;     inc rbx         ; i++
    ;     loop petla      ; rcx--, jeśli rcx != 0 skocz
    ;
    ; mov [wynik], rax
    ; ========================================
    
    ; ========================================
    ; SPRAWDZENIE w GDB:
    ; ========================================
    ; (gdb) break petla_start
    ; (gdb) run
    ; (gdb) info registers rax rcx
    ; (gdb) continue 10    → wykonaj pętlę 10 razy
    ; (gdb) x/d &wynik     → sprawdź wynik (powinno być 55)
    ; ========================================
    
    ; Exit
    mov rax, 60
    xor rdi, rdi
    syscall

; ============================================
; INSTRUKCJE SKOKÓW I PĘTLI:
;
; JMP label
;   Bezwarunkowy skok do label
;
; CMP operand1, operand2
;   Porównanie (ustawia flagi)
;   Nie zmienia operandów!
;
; JE/JZ label   (Jump if Equal / Zero)
;   Skocz jeśli operandy równe
;
; JNE/JNZ label (Jump if Not Equal / Not Zero)
;   Skocz jeśli operandy różne
;
; JG label      (Jump if Greater - signed)
;   Skocz jeśli operand1 > operand2
;
; JL label      (Jump if Less - signed)
;   Skocz jeśli operand1 < operand2
;
; JGE label     (Jump if Greater or Equal)
;   Skocz jeśli operand1 >= operand2
;
; JLE label     (Jump if Less or Equal)
;   Skocz jeśli operand1 <= operand2
;
; LOOP label
;   rcx--, jeśli rcx != 0 skocz do label
;   (Uwaga: działa tylko z rcx! W x64 to rcx, nie ecx)
;
; ============================================
; SCHEMAT PĘTLI:
;
; 1. Inicjalizacja licznika (rcx = start)
; 2. Sprawdzenie warunku (CMP + skok warunkowy)
; 3. Ciało pętli
; 4. Inkrementacja/dekrementacja (INC/DEC)
; 5. Skok na początek (JMP)
; ============================================