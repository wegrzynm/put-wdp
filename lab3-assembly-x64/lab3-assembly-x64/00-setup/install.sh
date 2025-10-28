#!/bin/bash
# ============================================
# Skrypt instalacyjny NASM x64
# Lab 2: Assembly Language Basics
# ============================================

echo "🔧 Instalacja NASM dla x64..."
echo ""

# Sprawdź architekturę
ARCH=$(uname -m)
echo "📊 Twoja architektura: $ARCH"

if [ "$ARCH" != "x86_64" ]; then
    echo "⚠️  UWAGA: Ten lab wymaga architektury x86_64 (64-bit)"
    echo "   Twoja architektura: $ARCH"
    echo ""
    echo "Opcje:"
    echo "1. Użyj komputera 64-bitowego"
    echo "2. Użyj online compilera: https://www.onlinegdb.com/"
    exit 1
fi

echo "✅ Architektura OK (x86_64)"
echo ""

# Sprawdź czy NASM już zainstalowany
if command -v nasm &> /dev/null; then
    echo "✅ NASM już zainstalowany!"
    nasm -v
    echo ""
    echo "Test kompilacji..."
    cd $(dirname "$0")
    if [ -f "test-hello.asm" ]; then
        nasm -f elf64 test-hello.asm -o test-hello.o 2>/dev/null
        if [ $? -eq 0 ]; then
            ld test-hello.o -o test-hello 2>/dev/null
            if [ $? -eq 0 ]; then
                echo "✅ Kompilacja działa!"
                ./test-hello
                rm -f test-hello test-hello.o
                echo ""
                echo "🎉 Wszystko gotowe! Możesz zaczynać laboratorium."
                exit 0
            fi
        fi
    fi
fi

# Instalacja NASM
echo "📦 Instaluję NASM..."
echo ""

# Wykryj system
if [ -f /etc/debian_version ]; then
    # Debian/Ubuntu
    echo "System: Debian/Ubuntu"
    sudo apt-get update -qq
    sudo apt-get install -y nasm build-essential
    
elif [ -f /etc/redhat-release ]; then
    # RedHat/Fedora/CentOS
    echo "System: RedHat/Fedora"
    sudo dnf install -y nasm gcc
    
elif [ -f /etc/arch-release ]; then
    # Arch Linux
    echo "System: Arch Linux"
    sudo pacman -S --noconfirm nasm gcc
    
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    echo "System: macOS"
    if ! command -v brew &> /dev/null; then
        echo "❌ Homebrew nie zainstalowany!"
        echo "Zainstaluj z: https://brew.sh"
        exit 1
    fi
    brew install nasm
    
else
    echo "❌ Nieznany system operacyjny"
    echo "Zainstaluj NASM ręcznie:"
    echo "  Ubuntu/Debian: sudo apt-get install nasm"
    echo "  Fedora: sudo dnf install nasm"
    echo "  Arch: sudo pacman -S nasm"
    echo "  macOS: brew install nasm"
    exit 1
fi

# Weryfikacja
echo ""
echo "📋 Weryfikacja instalacji..."
echo ""

if command -v nasm &> /dev/null; then
    echo "✅ NASM:"
    nasm -v
else
    echo "❌ NASM - instalacja nieudana"
    exit 1
fi

if command -v ld &> /dev/null; then
    echo "✅ Linker (ld): OK"
else
    echo "❌ Linker - brak"
    exit 1
fi

# Test kompilacji
echo ""
echo "🧪 Test kompilacji..."
cd $(dirname "$0")

if [ ! -f "test-hello.asm" ]; then
    echo "⚠️  Brak pliku test-hello.asm"
    echo "Stwórz go ręcznie i uruchom ponownie."
    exit 0
fi

nasm -f elf64 test-hello.asm -o test-hello.o
if [ $? -ne 0 ]; then
    echo "❌ Błąd asemblacji"
    exit 1
fi

ld test-hello.o -o test-hello
if [ $? -ne 0 ]; then
    echo "❌ Błąd linkowania"
    exit 1
fi

echo "✅ Kompilacja OK!"
echo ""
echo "Uruchamiam test..."
./test-hello

# Cleanup
rm -f test-hello test-hello.o

echo ""
echo "🎉 Wszystko działa! Gotowy do laboratorium."
echo ""
echo "NASTĘPNE KROKI:"
echo "1. Przejdź do folderu z przykładami: cd ../01-examples"
echo "2. Zobacz przykłady: ls -la"
echo "3. Skompiluj pierwszy przykład:"
echo "   nasm -f elf64 ex0-hello.asm -o ex0-hello.o"
echo "   ld ex0-hello.o -o ex0-hello"
echo "   ./ex0-hello"