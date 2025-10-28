; ============================================
; SELF-STUDY TASK 3: strlen - długość stringa
; ============================================
; OPIS:
; Oblicz długość stringa (liczbę znaków do '\0').
; 
; Przykład:
;   "Hello" → długość = 5
;   "Assembly" → długość = 8
;   "" → długość = 0
; 
; ALGORYTM:
;   length = 0
;   while string[length] != '\0':
;       length++
;   return length
; ============================================
; TRUDNOŚĆ: ⭐⭐ (średnia)
; CZAS: 30 minut
; ============================================

section .data
    string db "Hello, World!", 0    ; String zakończony '\0'
    dlugosc dq 0                    ; Tutaj zapisz długość

section .text
    global _start

_start:
    ; ========================================
    ; TODO: Oblicz długość stringa
    ; ========================================
    ; 
    ; ALGORYTM:
    ; 1. rsi = adres początku stringa
    ; 2. rcx = 0 (licznik)
    ; 3. Pętla:
    ;      Sprawdź czy [rsi] == 0
    ;      Jeśli tak, zakończ
    ;      Jeśli nie: rcx++, rsi++
    ; 4. Zapisz rcx do 'dlugosc'
    ; 
    ; WSKAZÓWKI:
    ; - mov rsi, string (adres początku)
    ; - cmp byte [rsi], 0 (porównaj bajt z zerem)
    ; - je koniec (jeśli zero, skocz)
    ; - inc rsi (następny znak)
    ; - inc rcx (długość++)
    
    ; TWÓJ KOD TUTAJ:
    
    
    
    
    
    
    
    
    
    
    
    ; Exit
    mov rax, 60
    xor rdi, rdi
    syscall

; ============================================
; SPRAWDZENIE:
; 
; $ nasm -f elf64 task3-strlen.asm -o task3.o
; $ ld task3.o -o task3
; $ gdb ./task3
; (gdb) break _start
; (gdb) run
; (gdb) continue
; (gdb) x/d &dlugosc
; 
; OCZEKIWANE WYNIKI:
;   "Hello, World!" → dlugosc=13
;   "Hello" → dlugosc=5
;   "" → dlugosc=0
; 
; Zmień string w sekcji .data i przetestuj!
; ============================================

; ============================================
; DLACZEGO bajt [rsi], a nie qword?
; 
; String to tablica BAJTÓW (char = 1 bajt).
; 
; cmp byte [rsi], 0   ✅ Porównaj 1 bajt
; cmp qword [rsi], 0  ❌ Porównaj 8 bajtów (za dużo!)
; 
; W x64, znaki to nadal 1 bajt (ASCII/UTF-8).
; ============================================