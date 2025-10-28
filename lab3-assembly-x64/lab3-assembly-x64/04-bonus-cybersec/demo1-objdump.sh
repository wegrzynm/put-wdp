#!/bin/bash
# ============================================
# Demo 1: Jak wygląda kod maszynowy?
# Narzędzie: objdump
# Czas: 5 minut
# ============================================

echo "═══════════════════════════════════════════"
echo "  DEMO 1: Kod Assembly → Kod Maszynowy"
echo "═══════════════════════════════════════════"
echo ""

# Sprawdź czy jest przykładowy program
if [ ! -f "../01-examples/ex0-hello" ]; then
    echo "❌ Brak skompilowanego programu!"
    echo "Najpierw uruchom:"
    echo "  cd ../01-examples"
    echo "  nasm -f elf64 ex0-hello.asm -o ex0-hello.o"
    echo "  ld ex0-hello.o -o ex0-hello"
    exit 1
fi

echo "📦 Program: ex0-hello"
echo ""

# Pokaż rozmiar
echo "▶ Rozmiar pliku:"
ls -lh ../01-examples/ex0-hello | awk '{print "  " $5 " (" $9 ")"}'
echo ""

# Disassembly całego programu
echo "▶ Disassembly (kod maszynowy → assembly):"
echo ""
objdump -d ../01-examples/ex0-hello | grep -A 20 "<_start>:"
echo ""

# Hex dump pierwszych bajtów
echo "▶ Raw bajty (hex):"
hexdump -C ../01-examples/ex0-hello | head -20
echo ""

echo "═══════════════════════════════════════════"
echo "  CO WIDZIMY?"
echo "═══════════════════════════════════════════"
echo ""
echo "1. mov rax, 1   →  48 c7 c0 01 00 00 00"
echo "   (7 bajtów kodu maszynowego!)"
echo ""
echo "2. syscall      →  0f 05"
echo "   (2 bajty)"
echo ""
echo "3. Procesor wykonuje DOKŁADNIE te bajty"
echo "   Assembly to tylko 'ludzka' reprezentacja"
echo ""

echo "═══════════════════════════════════════════"
echo "  ZNACZENIE DLA CYBERSECURITY"
echo "═══════════════════════════════════════════"
echo ""
echo "✓ Reverse Engineering: Masz tylko bajty, musisz"
echo "  zrozumieć co robi program (malware analysis)"
echo ""
echo "✓ Exploity: Wstrzykujesz kod maszynowy"
echo "  (shellcode = bajty, nie assembly!)"
echo ""
echo "✓ Debugowanie: IDA Pro, Ghidra pokazują"
echo "  disassembly - musisz umieć czytać"
echo ""

# Opcjonalnie: pokaż sekcje ELF
echo "═══════════════════════════════════════════"
echo "  BONUS: Struktura pliku ELF"
echo "═══════════════════════════════════════════"
echo ""
readelf -S ../01-examples/ex0-hello | grep -E "Section|\.text|\.data"
echo ""
echo "✓ .text  = kod (instrukcje)"
echo "✓ .data  = dane (zmienne)"
echo "✓ .bss   = niezainicjalizowane"
echo ""

echo "Koniec demo!"