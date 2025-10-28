; ============================================
; Test instalacji NASM x64
; Prosty "Hello World" do weryfikacji środowiska
; ============================================

section .data
    msg db 'Hello from NASM x64!', 0xA  ; 0xA = newline
    len equ $ - msg

section .text
    global _start

_start:
    ; sys_write(stdout, msg, len)
    mov rax, 1          ; syscall: write
    mov rdi, 1          ; fd: stdout
    mov rsi, msg        ; buffer
    mov rdx, len        ; count
    syscall
    
    ; sys_exit(0)
    mov rax, 60         ; syscall: exit
    xor rdi, rdi        ; status: 0
    syscall