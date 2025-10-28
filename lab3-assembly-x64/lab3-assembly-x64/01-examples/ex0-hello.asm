; ============================================
; Przykład 0: Hello World (x64)
; Podstawowy program wypisujący tekst
; ============================================
; KOMPILACJA:
;   nasm -f elf64 ex0-hello.asm -o ex0-hello.o
;   ld ex0-hello.o -o ex0-hello
;   ./ex0-hello
; ============================================

section .data
    ; Sekcja .data - dane zainicjalizowane
    ; Tutaj definiujemy stałe, stringi, tablice
    
    msg db 'Hello, Assembly x64!', 0xA  ; db = define byte
                                         ; 0xA = newline (\n)
    len equ $ - msg                      ; equ = stała
                                         ; $ = aktualny adres
                                         ; len = długość stringa

section .bss
    ; Sekcja .bss - dane niezainicjalizowane
    ; Tutaj rezerwujemy miejsce w pamięci (bez wartości początkowej)
    ; W tym przykładzie: pusta

section .text
    ; Sekcja .text - kod programu (instrukcje)
    
    global _start   ; Punkt wejścia (wymagany przez linker)

_start:
    ; ----------------------------------------
    ; SYSCALL: sys_write
    ; Wypisuje tekst na ekran (stdout)
    ; ----------------------------------------
    ; Prototyp w C: ssize_t write(int fd, const void *buf, size_t count);
    ;
    ; W x64 argumenty syscall przekazujemy przez rejestry:
    ;   rax = numer syscall (1 = sys_write)
    ;   rdi = argument 1 (fd: 1 = stdout)
    ;   rsi = argument 2 (buffer: adres tekstu)
    ;   rdx = argument 3 (count: liczba bajtów)
    
    mov rax, 1          ; rax = 1 (syscall number dla write)
    mov rdi, 1          ; rdi = 1 (file descriptor: stdout)
    mov rsi, msg        ; rsi = adres msg
    mov rdx, len        ; rdx = długość msg
    syscall             ; wywołanie systemowe
    
    ; ----------------------------------------
    ; SYSCALL: sys_exit
    ; Kończy program
    ; ----------------------------------------
    ; Prototyp w C: void exit(int status);
    ;
    ; rax = numer syscall (60 = sys_exit)
    ; rdi = kod wyjścia (0 = sukces)
    
    mov rax, 60         ; rax = 60 (syscall number dla exit)
    xor rdi, rdi        ; rdi = 0 (xor sama ze sobą = 0)
                        ; xor jest szybszy niż mov rdi, 0
    syscall             ; wywołanie systemowe

; ============================================
; NOTATKI:
;
; 1. RÓŻNICE x86 vs x64:
;    x86: eax=4, ebx=1, ecx=msg, edx=len, int 0x80
;    x64: rax=1, rdi=1, rsi=msg, rdx=len, syscall
;
; 2. DLACZEGO "msg" bez nawiasów?
;    mov rsi, msg   → rsi = ADRES msg
;    mov rsi, [msg] → rsi = WARTOŚĆ pod adresem msg (pierwsze bajty)
;
; 3. CO TO $ w "equ $ - msg"?
;    $ = aktualny adres w pamięci
;    $ - msg = długość od msg do $
;
; 4. DLACZEGO xor rdi, rdi zamiast mov rdi, 0?
;    xor jest szybszy (1 bajt vs 5 bajtów w kodzie maszynowym)
; ============================================