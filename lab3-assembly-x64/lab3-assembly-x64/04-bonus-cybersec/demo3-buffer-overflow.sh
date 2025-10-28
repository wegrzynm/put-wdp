#!/bin/bash
# ============================================
# Skrypt do demo Buffer Overflow
# ============================================

echo "═══════════════════════════════════════════"
echo "  DEMO 3: Buffer Overflow (Conceptual)"
echo "═══════════════════════════════════════════"
echo ""
echo "⚠️  UWAGA: Ten kod jest celowo podatny!"
echo "   Używamy go TYLKO do nauki, nie w produkcji!"
echo ""

# Sprawdź czy gcc jest zainstalowane
if ! command -v gcc &> /dev/null; then
    echo "❌ GCC nie jest zainstalowane"
    echo "Zainstaluj: sudo apt-get install gcc"
    exit 1
fi

# Kompilacja (z wyłączonymi zabezpieczeniami)
echo "▶ Kompilacja (z wyłączonymi zabezpieczeniami)..."
gcc -fno-stack-protector -z execstack -no-pie \
    -o overflow demo3-buffer-overflow.c 2>/dev/null

if [ $? -ne 0 ]; then
    echo "❌ Błąd kompilacji"
    exit 1
fi

echo "✅ Skompilowano"
echo ""

# Demo 1: Normalny input
echo "═══════════════════════════════════════════"
echo "  TEST 1: Normalny input (bezpieczny)"
echo "═══════════════════════════════════════════"
echo ""
./overflow "Hello"
echo ""

# Demo 2: Długi input (overflow)
echo "═══════════════════════════════════════════"
echo "  TEST 2: Długi input (buffer overflow!)"
echo "═══════════════════════════════════════════"
echo ""
./overflow "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
echo ""
echo "👆 Program się crashnął (Segmentation fault)"
echo ""

# Wyjaśnienie
echo "═══════════════════════════════════════════"
echo "  CO SIĘ STAŁO?"
echo "═══════════════════════════════════════════"
echo ""
echo "1. Buffer = 16 bajtów"
echo "2. Wpisaliśmy ~35 bajtów"
echo "3. Nadpisaliśmy pamięć poza buforem!"
echo ""
echo "┌─────────────────┐"
echo "│ buffer[16]      │ ← Tu powinno się skończyć"
echo "├─────────────────┤"
echo "│ ...             │"
echo "├─────────────────┤"
echo "│ return address  │ ← To zostało nadpisane!"
echo "└─────────────────┘"
echo ""
echo "4. Gdy funkcja kończy się (ret), CPU próbuje"
echo "   wrócić pod adres który nadpisaliśmy"
echo "5. Ten adres jest śmieciem → CRASH!"
echo ""

echo "═══════════════════════════════════════════"
echo "  DLACZEGO TO JEST NIEBEZPIECZNE?"
echo "═══════════════════════════════════════════"
echo ""
echo "Hacker może:"
echo ""
echo "1. Nadpisać return address swoim adresem"
echo "2. Wskazać na SWÓJ kod (shellcode)"
echo "3. Wykonać dowolne polecenia!"
echo ""
echo "Przykład shellcode (x64):"
echo "  \\x48\\x31\\xc0\\x48\\x31\\xff\\x48\\x31\\xf6..."
echo "  (bajty które wykonują /bin/sh)"
echo ""

echo "═══════════════════════════════════════════"
echo "  JAK SIĘ BRONIĆ?"
echo "═══════════════════════════════════════════"
echo ""
echo "✓ ASLR (Address Space Layout Randomization)"
echo "  → Losowe adresy w pamięci"
echo ""
echo "✓ Stack Canaries"
echo "  → 'Strażnik' przed return address"
echo ""
echo "✓ DEP/NX (Data Execution Prevention)"
echo "  → Stos nie-wykonywalny"
echo ""
echo "✓ Dobre praktyki programowania!"
echo "  → Używaj bezpiecznych funkcji:"
echo "     strcpy() ❌  →  strncpy() ✅"
echo "     gets()   ❌  →  fgets()   ✅"
echo ""

echo "═══════════════════════════════════════════"
echo "  WIĘCEJ INFORMACJI"
echo "═══════════════════════════════════════════"
echo ""
echo "📚 Książki:"
echo "  - 'Hacking: The Art of Exploitation'"
echo "  - 'The Shellcoder's Handbook'"
echo ""
echo "🎓 Kursy:"
echo "  - OSCP (Offensive Security)"
echo "  - PWK (Penetration Testing with Kali)"
echo ""
echo "🛠️ Narzędzia:"
echo "  - Metasploit (exploit framework)"
echo "  - pwntools (Python library)"
echo "  - ROPgadget"
echo ""

# Cleanup
rm -f overflow

echo "Koniec demo!"