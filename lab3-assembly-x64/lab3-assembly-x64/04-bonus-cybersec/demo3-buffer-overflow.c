// ============================================
// Demo 3: Buffer Overflow (TYLKO POKAZAĆ!)
// NIE kompilujemy tego na laboratorium
// ============================================
// Czas: 5-10 minut (live demo)
// UWAGA: Ten kod jest celowo podatny!
// ============================================

#include <stdio.h>
#include <string.h>

// Funkcja z buffer overflow
void vulnerable_function(char *input) {
    char buffer[16];  // Mały bufor (16 bajtów)
    
    printf("Buffer address: %p\n", buffer);
    
    // NIEBEZPIECZNE! Nie sprawdza długości!
    strcpy(buffer, input);  // ← TUTAJ JEST BŁĄD!
    
    printf("Buffer content: %s\n", buffer);
}

// Funkcja którą chcemy wywołać (exploit target)
void secret_function() {
    printf("\n🚨 SUCCESS! Secret function executed!\n");
    printf("W prawdziwym exploicie tutaj byłby shellcode.\n\n");
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <input_string>\n", argv[0]);
        printf("\nExamples:\n");
        printf("  Safe:   %s \"Hello\"\n", argv[0]);
        printf("  Unsafe: %s \"AAAAAAAAAAAAAAAAAAAAAAAAAAAA\"\n", argv[0]);
        return 1;
    }
    
    printf("=== Buffer Overflow Demo ===\n\n");
    printf("Input length: %lu bytes\n", strlen(argv[1]));
    printf("Buffer size: 16 bytes\n\n");
    
    vulnerable_function(argv[1]);
    
    printf("\nProgram finished normally.\n");
    return 0;
}

// ============================================
// KOMPILACJA (z wyłączonymi zabezpieczeniami):
// 
// gcc -fno-stack-protector -z execstack \
//     -no-pie -o overflow demo3-buffer-overflow.c
// 
// Opcje:
// -fno-stack-protector = wyłącz canary
// -z execstack         = wykonywalny stos
// -no-pie              = stałe adresy
// ============================================

// ============================================
// DEMONSTRACJA:
// 
// 1. Normalny input:
//    ./overflow "Hello"
//    → Działa OK
// 
// 2. Długi input (overflow):
//    ./overflow "AAAAAAAAAAAAAAAAAAAAAAAAAAAA"
//    → Segmentation fault!
// 
// 3. Exploit (zaawansowane - tylko pokaż koncepcję):
//    Python script generuje payload który:
//    - Nadpisuje return address
//    - Wskazuje na secret_function()
//    - Wykonuje funkcję bez jej wywołania!
// ============================================

// ============================================
// CO POKAZAĆ STUDENTOM:
// 
// 1. "Bufor = 16 bajtów, ale wpisaliśmy 30"
// 2. "Program się crashuje - dlaczego?"
// 3. "Nadpisaliśmy return address na stosie!"
// 4. "Hacker może wskazać na własny kod"
// 5. "To podstawa exploitów (buffer overflow)"
// 
// NIE MUSISZ:
// - Pokazywać jak zrobić exploit
// - Tłumaczyć szczegółów stosu
// - Komplikować
// 
// CEL: "Widzicie? Dlatego Assembly jest ważny
//       w cybersecurity - musicie rozumieć pamięć!"
// ============================================