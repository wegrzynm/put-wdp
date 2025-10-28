; ============================================
; Przykład 1: Zmienne i etykiety (x64)
; Pokazuje różnicę między adresem a wartością
; ============================================
; KOMPILACJA:
;   nasm -f elf64 ex1-variables.asm -o ex1-variables.o
;   ld ex1-variables.o -o ex1-variables
;   gdb ./ex1-variables
; ============================================

section .data
    ; Zmienne to ETYKIETY wskazujące na ADRESY w pamięci
    
    x dq 10         ; dq = define quadword (8 bajtów, 64 bity)
                    ; x to ETYKIETA (nazwa adresu)
                    ; Wartość: 10
    
    y dq 20         ; y = kolejna zmienna (8 bajtów dalej)
    
    z dq 0          ; z = miejsce na wynik

section .text
    global _start

_start:
    ; ----------------------------------------
    ; LOAD: Załaduj wartość z pamięci
    ; ----------------------------------------
    ; UWAGA: Nawias kwadratowy [] = "wartość pod adresem"
    
    mov rax, [x]        ; rax = wartość x (= 10)
                        ; To znaczy: "idź pod adres x i weź wartość"
    
    ; Bez nawiasów:
    ; mov rax, x        ; rax = ADRES x (np. 0x0000000000601000)
    
    ; ----------------------------------------
    ; OPERATE: Wykonaj operację
    ; ----------------------------------------
    
    add rax, [y]        ; rax = rax + wartość y
                        ; rax = 10 + 20 = 30
    
    ; ----------------------------------------
    ; STORE: Zapisz wynik do pamięci
    ; ----------------------------------------
    
    mov [z], rax        ; zapisz rax do zmiennej z
                        ; Teraz: z = 30
    
    ; ----------------------------------------
    ; SPRAWDZENIE w GDB:
    ; ----------------------------------------
    ; (gdb) break _start
    ; (gdb) run
    ; (gdb) x/d &x          → pokaż x jako decimal
    ; (gdb) x/d &y          → pokaż y
    ; (gdb) stepi           → krok po instrukcji
    ; (gdb) info registers rax
    ; (gdb) x/d &z          → sprawdź wynik
    ; ----------------------------------------
    
    ; Exit
    mov rax, 60
    xor rdi, rdi
    syscall

; ============================================
; KLUCZOWE KONCEPTY:
;
; 1. ETYKIETA (label) = NAZWA ADRESU
;    x, y, z to nie "zmienne" jak w Pythonie
;    To NAZWY ADRESÓW w pamięci
;
; 2. NAWIAS [] = "wartość pod adresem"
;    mov rax, x    → rax = adres (np. 0x601000)
;    mov rax, [x]  → rax = wartość (10)
;
; 3. LOAD-OPERATE-STORE
;    Procesor nie operuje bezpośrednio na pamięci!
;    Musi: załadować → operacja → zapisać
;
;    Python: z = x + y  (jedna linia)
;    Assembly: 
;        mov rax, [x]    ; LOAD
;        add rax, [y]    ; OPERATE
;        mov [z], rax    ; STORE
;
; 4. DLACZEGO dq (64-bit)?
;    W x64, naturalny rozmiar rejestru to 64 bity
;    dq (quadword) = 8 bajtów = 64 bity = pasuje do rax
;    Możesz też użyć dd (32-bit) ale wtedy używaj eax
; ============================================