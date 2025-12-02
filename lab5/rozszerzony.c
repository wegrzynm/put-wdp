#include <stdio.h>
#include <string.h>

/*
🚀 ROZSZERZONY (4 zadania, po 3 pkt) - OPCJONALNIE
Zadanie 9: Union Basics (3 pkt)
Cel: Zrozumieć różnicę między struct a union.

Treść: Utwórz:

Struct Data1 z polami: int i, float f, char c
Union Data2 z polami: int i, float f, char c
Program powinien:

Wypisać rozmiar struct i union
Ustawić wartości w struct (wszystkie pola naraz)
Wypisać wartości struct
Ustawić wartości w union (po kolei, obserwując nadpisywanie)
Wypisać wartości union po każdym ustawieniu
Przykładowy output:

sizeof(struct Data1): 12 bytes
sizeof(union Data2): 4 bytes

STRUCT (każde pole niezależne):
i=10, f=3.14, c=A

UNION (współdzielona pamięć):
After setting i=10:   i=10, f=0.000000, c=\n
After setting f=3.14: i=1078523331, f=3.140000, c=\xdb
After setting c=A:    i=1078523329, f=3.140000, c=A
Wskazówki:

Union: wszystkie pola w TYM SAMYM miejscu pamięci
Ustawiając f, nadpisujesz i
Wartości "śmieciowe" to normalne - to są bajty z innego pola!
*/

struct Data1 {
    int i;
    float f;
    char c;
};

union Data2 {
    int i;
    float f;
    char c;
};

/*
Zadanie 10: Float Analysis (IEEE 754) (3 pkt) 🌟
Cel: Użyć union do analizy reprezentacji float.

Treść: Utwórz union Real z polami:

float x (liczba zmiennoprzecinkowa)
unsigned char bytes[4] (4 bajty pamięci)
Program powinien:

Zapytać użytkownika o liczbę float
Wypisać wartość float
Wypisać reprezentację hex (4 bajty)
Powtórzyć dla kilku liczb: 0.0, 1.0, -1.0, 3.14159
Przykładowy output:

Enter a float: 4.0
Float: 4.000000
Hex bytes: 00 00 80 40

Enter a float: 1.0
Float: 1.000000
Hex bytes: 00 00 80 3f

Enter a float: -1.0
Float: -1.000000
Hex bytes: 00 00 80 bf

Enter a float: 3.14159
Float: 3.141590
Hex bytes: d0 0f 49 40
Wskazówki:

Format %02x dla hex (2 cyfry, z zerem na początku)
Iteruj po bytes[0] do bytes[3]
To jest IEEE 754! Widzisz jak komputer przechowuje float!
Bonus: Spróbuj wpisać 0.1 - zobaczysz czemu 0.1 + 0.2 != 0.3!
*/

union Real {
    float x;
    unsigned char bytes[4];
};

void analyzeFloat(float val) {
    union Real r;
    r.x = val;
    printf("Float: %f\n", r.x);
    printf("Hex bytes: ");
    for(int i=0; i<4; i++) {
        printf("%02x ", r.bytes[i]);
    }
    printf("\n\n");
}

/*
Zadanie 11: sizeof Comparison (3 pkt)
Cel: Porównać rozmiary różnych struktur i unionów.

Treść: Utwórz 4 struktury/uniony:

Struct z: char, int, char
Struct z: char, char, int
Union z: char, int, char
Union z: char, char, int
Wypisz rozmiar każdego i wyjaśnij różnice.

Przykładowy output:

Struct 1 (char, int, char): 12 bytes
Struct 2 (char, char, int): 8 bytes
Union 1 (char, int, char): 4 bytes
Union 2 (char, char, int): 4 bytes

Observations:
- Struct 1 > Struct 2 due to padding alignment
- Both unions are 4 bytes (size of largest member: int)
- Order matters in structs (padding), not in unions
Wskazówki:

Padding - kompilator wyrównuje pamięć dla wydajności
W struct kolejność pól ma znaczenie!
W union rozmiar = rozmiar największego pola
*/

struct S1 {
    char c1;
    int i;
    char c2;
};

struct S2 {
    char c1;
    char c2;
    int i;
};

union U1 {
    char c1;
    int i;
    char c2;
};

union U2 {
    char c1;
    char c2;
    int i;
};

/*
Zadanie 12: Security - Password Struct (3 pkt)
Cel: Praktyczne zadanie z cybersecurity.

Treść: Utwórz strukturę User z polami:

username (string, max 20 znaków)
password (string, max 20 znaków)
isAdmin (int, 0 lub 1)
Napisz funkcje:

int authenticate(User user, char* inputUsername, char* inputPassword) - zwraca 1 jeśli dane poprawne, 0 jeśli nie
void displayUser(User user) - wyświetla dane użytkownika (bez hasła!)
W main():

Utwórz 3 użytkowników (w tym 1 admin)
Zapytaj o username i password
Sprawdź autentykację
Jeśli poprawne - wyświetl dane + "Access granted"
Jeśli niepoprawne - "Access denied"
Przykładowy output:

Users in database:
- alice (user)
- bob (admin)
- charlie (user)

Enter username: bob
Enter password: secret123

Authentication successful!
User: bob
Role: Admin
Access granted.
Wskazówki:

Użyj strcmp(str1, str2) do porównania stringów
NIE wypisuj hasła w displayUser()!
isAdmin == 1 → "Admin", isAdmin == 0 → "User"
*/

typedef struct {
    char username[21];
    char password[21];
    int isAdmin;
} User;

int authenticate(User user, char* inputUsername, char* inputPassword) {
    if (strcmp(user.username, inputUsername) == 0 && strcmp(user.password, inputPassword) == 0) {
        return 1;
    }
    return 0;
}

void displayUser(User user) {
    printf("User: %s\n", user.username);
    printf("Role: %s\n", user.isAdmin ? "Admin" : "User");
}

int main() {
    // --- ZADANIE 9 ---
    printf("--- ZADANIE 9 ---\n");
    struct Data1 s1 = {10, 3.14, 'A'};
    union Data2 u2;

    printf("sizeof(struct Data1): %zu bytes\n", sizeof(struct Data1));
    printf("sizeof(union Data2): %zu bytes\n\n", sizeof(union Data2));

    printf("STRUCT (każde pole niezależne):\n");
    printf("i=%d, f=%.2f, c=%c\n\n", s1.i, s1.f, s1.c);

    printf("UNION (współdzielona pamięć):\n");
    u2.i = 10;
    printf("After setting i=10:   i=%d, f=%f, c=%c\n", u2.i, u2.f, u2.c);
    u2.f = 3.14;
    printf("After setting f=3.14: i=%d, f=%f, c=%c\n", u2.i, u2.f, u2.c);
    u2.c = 'A';
    printf("After setting c=A:    i=%d, f=%f, c=%c\n\n", u2.i, u2.f, u2.c);

    // --- ZADANIE 10 ---
    printf("--- ZADANIE 10 ---\n");
    float val;
    printf("Enter a float: ");
    scanf("%f", &val);
    analyzeFloat(val);
    
    // Przykładowe wartości z zadania
    analyzeFloat(0.0);
    analyzeFloat(1.0);
    analyzeFloat(-1.0);
    analyzeFloat(3.14159);

    // --- ZADANIE 11 ---
    printf("--- ZADANIE 11 ---\n");
    printf("Struct 1 (char, int, char): %zu bytes\n", sizeof(struct S1));
    printf("Struct 2 (char, char, int): %zu bytes\n", sizeof(struct S2));
    printf("Union 1 (char, int, char): %zu bytes\n", sizeof(union U1));
    printf("Union 2 (char, char, int): %zu bytes\n\n", sizeof(union U2));
    
    printf("Observations:\n");
    printf("- Struct 1 > Struct 2 due to padding alignment\n");
    printf("- Both unions are 4 bytes (size of largest member: int)\n");
    printf("- Order matters in structs (padding), not in unions\n\n");

    // --- ZADANIE 12 ---
    printf("--- ZADANIE 12 ---\n");
    User users[3] = {
        {"alice", "pass1", 0},
        {"bob", "secret123", 1},
        {"charlie", "qwerty", 0}
    };

    printf("Users in database:\n");
    for(int i=0; i<3; i++) {
        printf("- %s (%s)\n", users[i].username, users[i].isAdmin ? "admin" : "user");
    }
    printf("\n");

    char inUser[21], inPass[21];
    printf("Enter username: ");
    scanf("%s", inUser);
    printf("Enter password: ");
    scanf("%s", inPass);

    int found = 0;
    for(int i=0; i<3; i++) {
        if (authenticate(users[i], inUser, inPass)) {
            printf("\nAuthentication successful!\n");
            displayUser(users[i]);
            printf("Access granted.\n");
            found = 1;
            break;
        }
    }

    if (!found) {
        printf("\nAccess denied.\n");
    }

    return 0;
}