
lab05_zadania_studenci
Lab 5: Struktury w C - Ćwiczenia
Politechnika Poznańska
Introduction to Programming - Cybersecurity
Prowadzący: Bartosz Lewandowski

Czas: 90 minut (1,5h)
Język: C
Narzędzia: Programiz.com lub GCC lokalnie

📊 SYSTEM OCENIANIA
Sekcja	Zadania	Punkty	Wymagane na 3.0
Rozgrzewka	3	Po 1 pkt	✅ TAK
Minimum	5	Po 2 pkt	✅ TAK
Rozszerzony	4	Po 3 pkt	❌ Opcjonalnie
Punktacja:

3.0 = Rozgrzewka (3 pkt) + Minimum (10 pkt) = 13 pkt
3.5 = 13 pkt + 1 zadanie rozszerzone = 16 pkt
4.0 = 13 pkt + 2 zadania rozszerzone = 19 pkt
4.5 = 13 pkt + 3 zadania rozszerzone = 22 pkt
5.0 = Wszystkie zadania = 25 pkt
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
✅ MINIMUM (5 zadań, po 2 pkt) - OBOWIĄZKOWE NA 3.0
Zadanie 4: Student Record (2 pkt)
Cel: Struktura z wieloma polami, input od użytkownika.

Treść: Utwórz strukturę Student z polami:

name (string, max 50 znaków)
id (int, numer indeksu)
grade (float, ocena)
Program powinien:

Zapytać użytkownika o dane studenta
Zapisać dane w strukturze
Wypisać informacje o studencie
Przykładowy input:

Enter name: John
Enter student ID: 123456
Enter grade: 4.5
Przykładowy output:

Student Record:
Name: John
ID: 123456
Grade: 4.50
Wskazówki:

Użyj scanf("%s", student.name); dla stringa (bez spacji)
Użyj scanf("%d", &student.id); dla int
Użyj scanf("%f", &student.grade); dla float
Format %.2f wypisze float z 2 miejscami po przecinku
Zadanie 5: Rectangle - Pole i obwód (2 pkt)
Cel: Funkcje pracujące na strukturach.

Treść: Utwórz strukturę Rectangle z polami:

width (float, szerokość)
height (float, wysokość)
Napisz funkcje:

float area(Rectangle r) - zwraca pole
float perimeter(Rectangle r) - zwraca obwód
W main():

Utwórz prostokąt 5.0 x 3.0
Oblicz i wypisz pole i obwód
Przykładowy output:

Rectangle: 5.00 x 3.00
Area: 15.00
Perimeter: 16.00
Wskazówki:

Pole = width * height
Obwód = 2 * (width + height)
Przekazuj strukturę przez wartość (kopię)
Zadanie 6: Array of Structs (2 pkt)
Cel: Tablica struktur, iteracja.

Treść: Utwórz tablicę 3 studentów (struktura Student z Zadania 4).

Program powinien:

Zapytać użytkownika o dane 3 studentów
Zapisać w tablicy
Wypisać wszystkich studentów
Przykładowy input:

Student 1:
Enter name: Alice
Enter ID: 111
Enter grade: 5.0

Student 2:
Enter name: Bob
Enter ID: 222
Enter grade: 4.0

Student 3:
Enter name: Charlie
Enter ID: 333
Enter grade: 3.5
Przykładowy output:

All Students:
1. Alice (ID: 111) - Grade: 5.00
2. Bob (ID: 222) - Grade: 4.00
3. Charlie (ID: 333) - Grade: 3.50
Wskazówki:

Deklaracja: Student students[3];
Dostęp: students[0].name, students[1].grade, etc.
Użyj pętli for do iteracji
Zadanie 7: Find Oldest Person (2 pkt)
Cel: Wyszukiwanie w tablicy struktur.

Treść: Dany jest kod z 5 osobami (struktura Person z polami name i age).

Napisz funkcję:

Person findOldest(Person people[], int size)
Funkcja powinna zwrócić najstarszą osobę.

W main():

Utwórz tablicę 5 osób (dowolne dane)
Znajdź najstarszą osobę
Wypisz jej imię i wiek
Przykładowy output:

People:
Alice (25)
Bob (30)
Charlie (28)
Diana (35)
Eve (22)

Oldest person: Diana (35)
Wskazówki:

Iteruj po tablicy
Śledź maksymalny wiek i indeks
Zwróć strukturę people[maxIndex]
Zadanie 8: Average Grade (2 pkt)
Cel: Obliczanie średniej z danych w strukturach.

Treść: Dany jest kod z tablicą 5 studentów (struktura Student z Zadania 4).

Napisz funkcję:

float calculateAverage(Student students[], int size)
Funkcja powinna zwrócić średnią ocen.

W main():

Utwórz tablicę 5 studentów z ocenami
Oblicz średnią
Wypisz średnią z dokładnością do 2 miejsc po przecinku
Przykładowy output:

Students:
Alice: 5.0
Bob: 4.0
Charlie: 3.5
Diana: 4.5
Eve: 5.0

Average grade: 4.40
Wskazówki:

Suma ocen / liczba studentów
Użyj float dla średniej (nie int!)
Format %.2f dla 2 miejsc po przecinku
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
💡 OGÓLNE WSKAZÓWKI
Struktura programu w C:
#include <stdio.h>
#include <string.h>  // dla strcpy, strcmp

// 1. Definicje struktur
typedef struct {
    int field1;
    char field2[50];
} MyStruct;

// 2. Deklaracje funkcji (opcjonalnie)
void myFunction(MyStruct s);

// 3. Funkcja main()
int main() {
    // Twój kod tutaj
    return 0;
}

// 4. Implementacje funkcji
void myFunction(MyStruct s) {
    // Implementacja
}
Dostęp do pól:
MyStruct s;
s.field1 = 10;              // kropka dla zmiennej

MyStruct *ptr = &s;
(*ptr).field1 = 10;         // długa wersja dla wskaźnika
ptr->field1 = 10;           // krótsza wersja (to samo!)
Kopiowanie struktur:
MyStruct a, b;
a.field1 = 10;
b = a;  // Kopiuje wszystkie pola!
Porównanie stringów:
char str1[] = "hello";
char str2[] = "hello";

// ❌ ZŁE:
if (str1 == str2) { ... }  // Porównuje adresy!

// ✅ DOBRE:
if (strcmp(str1, str2) == 0) { ... }  // Porównuje zawartość
Debugowanie:
printf("DEBUG: value=%d\n", myStruct.field);  // Dodaj komunikaty debug
🎯 WORKFLOW - JAK PRACOWAĆ?
Krok po kroku:
Rozgrzewka (15 min)

Zadanie 1 → 2 → 3
Cel: przypomnieć struct, typedef, sizeof
Minimum (45 min)

Zadanie 4 → 5 → 6 → 7 → 8
Cel: zdobyć 3.0
Sprawdzaj każde zadanie przed następnym!
Rozszerzony (30 min)

Wybierz zadania które Cię interesują
Zadanie 10 (Float Analysis) jest super ciekawe! 🌟
Cel: wyższa ocena
Testowanie:
Dla każdego zadania:

Napisz kod
Skompiluj: gcc file.c -o file
Uruchom: ./file
Sprawdź output
Jeśli błędy → popraw → kompiluj ponownie
Jeśli działa → przechodź dalej
Narzędzia:
Online (Programiz.com):

Wejdź na https://www.programiz.com/c-programming/online-compiler/
Wklej kod
Kliknij "Run"
Zobacz output
Lokalnie (GCC):

gcc zadanie1.c -o zadanie1
./zadanie1
IDE (opcjonalnie):

VS Code z rozszerzeniem C/C++
Code::Blocks
CLion
❓ FAQ - Często zadawane pytania
Q: Czy mogę użyć innych nazw pól?
A: Tak! Nazwy pól mogą być dowolne (ale opisowe).

Q: Czy muszę używać typedef?
A: W rozgrzewce tak (Zadanie 2). W innych - opcjonalnie, ale wygodniejsze.

Q: Co jeśli sizeof daje inny wynik?
A: To normalne! Zależy od kompilatora i systemu. Ważna jest koncepcja.

Q: Union nadpisuje dane - czy to błąd?
A: Nie! To normalne zachowanie union. Wszystkie pola dzielą pamięć.

Q: Jak wypełnić struct wartościami początkowymi?
A:

MyStruct s = {10, "hello"};  // Kolejność pól
Q: Mogę przekazać struct do funkcji?
A: Tak! Przez wartość (kopię) lub przez wskaźnik (referencję).

📚 DODATKOWE MATERIAŁY
Jeśli skończysz wcześniej:

Eksperymentuj z różnymi strukturami
Spróbuj zagnieżdżonych struktur (struct w struct)
Przeczytaj o IEEE 754: https://en.wikipedia.org/wiki/IEEE_754
Spróbuj union z różnymi typami danych
Przydatne linki:

C structs: https://www.programiz.com/c-programming/c-structures
C unions: https://www.programiz.com/c-programming/c-unions
IEEE 754: https://www.h-schmidt.net/FloatConverter/IEEE754.html
✅ SPRAWDZENIE ZADAŃ
Po laboratorium:

Pokaż kod prowadzącemu
Uruchom program i pokaż działanie
Wyjaśnij co robi Twój kod
Oddawanie:

Pliki .c dla każdego zadania
Ewentualnie zrzuty ekranu z działającymi programami
Powodzenia! 🚀

Pamiętaj: Zadawaj pytania! Prowadzący jest po to, żeby pomagać! 💪