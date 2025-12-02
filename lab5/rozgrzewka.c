#include <stdio.h>
#include <string.h>

/*
🔥 ROZGRZEWKA (3 zadania, po 1 pkt)
Zadanie 1: Hello Struct (1 pkt)
Cel: Zdefiniować strukturę, utworzyć zmienną, wypisać wartości.

Treść: Utwórz strukturę Person z polami:

name (string, max 50 znaków)
age (int)
W funkcji main():

Utwórz zmienną typu Person
Przypisz wartości: name="Alice", age=25
Wypisz: Name: Alice, Age: 25
Przykładowy output:

Name: Alice, Age: 25
Wskazówki:

Użyj char name[50]; dla stringa
Użyj strcpy(person.name, "Alice"); do przypisania stringa
Nie zapomnij #include <string.h>
*/

// Rozwiązanie Zadania 1 i 2 (definicja struktury)
struct Person {
    char name[50];
    int age;
};

/*
Zadanie 2: typedef - Krótsze nazwy (1 pkt)
Cel: Użyć typedef do uproszczenia kodu.

Treść: Zmodyfikuj kod z Zadania 1:

Dodaj typedef dla struktury Person jako Man
Użyj Man zamiast struct Person
Utwórz dwie zmienne: alice (25 lat) i bob (30 lat)
Wypisz dane obu osób
Przykładowy output:

Name: Alice, Age: 25
Name: Bob, Age: 30
Wskazówki:

Składnia: typedef struct Person Man;
Potem używasz: Man alice; zamiast struct Person alice;
*/

// Rozwiązanie Zadania 2 (typedef)
typedef struct Person Man;

/*
Zadanie 3: sizeof - Ile zajmuje struct? (1 pkt)
Cel: Zrozumieć rozmiar struktury w pamięci.

Treść: Utwórz strukturę Data z polami:

a (int)
b (char)
c (double)
Wypisz:

Rozmiar każdego pola osobno
Rozmiar całej struktury
Porównaj: suma pól vs rozmiar struktury
Przykładowy output:

sizeof(int): 4 bytes
sizeof(char): 1 byte
sizeof(double): 8 bytes
Sum: 13 bytes

sizeof(struct Data): 16 bytes

Difference: 3 bytes (padding!)
Wskazówki:

Użyj sizeof(int), sizeof(char), etc.
Użyj sizeof(struct Data) dla całej struktury
Różnica to padding - wyrównanie pamięci
*/

// Rozwiązanie Zadania 3 (struktura Data)
struct Data {
    int a;
    char b;
    double c;
};

int main() {
    // --- ZADANIE 1 ---
    printf("--- ZADANIE 1 ---\n");
    struct Person p1;
    strcpy(p1.name, "Alice");
    p1.age = 25;
    printf("Name: %s, Age: %d\n", p1.name, p1.age);
    printf("\n");

    // --- ZADANIE 2 ---
    printf("--- ZADANIE 2 ---\n");
    Man alice;
    strcpy(alice.name, "Alice");
    alice.age = 25;

    Man bob;
    strcpy(bob.name, "Bob");
    bob.age = 30;

    printf("Name: %s, Age: %d\n", alice.name, alice.age);
    printf("Name: %s, Age: %d\n", bob.name, bob.age);
    printf("\n");

    // --- ZADANIE 3 ---
    printf("--- ZADANIE 3 ---\n");
    struct Data d;
    
    size_t size_int = sizeof(d.a);
    size_t size_char = sizeof(d.b);
    size_t size_double = sizeof(d.c);
    size_t sum = size_int + size_char + size_double;
    size_t size_struct = sizeof(struct Data);

    printf("sizeof(int): %zu bytes\n", size_int);
    printf("sizeof(char): %zu bytes\n", size_char);
    printf("sizeof(double): %zu bytes\n", size_double);
    printf("Sum: %zu bytes\n\n", sum);

    printf("sizeof(struct Data): %zu bytes\n\n", size_struct);

    printf("Difference: %zu bytes (padding!)\n", size_struct - sum);

    return 0;
}