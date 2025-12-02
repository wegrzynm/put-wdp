#include <stdio.h>
#include <string.h>

/*
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
*/

typedef struct {
    char name[50];
    int id;
    float grade;
} Student;

/*
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
*/

typedef struct {
    float width;
    float height;
} Rectangle;

float area(Rectangle r) {
    return r.width * r.height;
}

float perimeter(Rectangle r) {
    return 2 * (r.width + r.height);
}

/*
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
*/

// (Wykorzystujemy strukturę Student zdefiniowaną wcześniej)

/*
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
*/

typedef struct {
    char name[50];
    int age;
} Person;

Person findOldest(Person people[], int size) {
    Person oldest = people[0];
    for (int i = 1; i < size; i++) {
        if (people[i].age > oldest.age) {
            oldest = people[i];
        }
    }
    return oldest;
}

/*
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
*/

float calculateAverage(Student students[], int size) {
    float sum = 0;
    for (int i = 0; i < size; i++) {
        sum += students[i].grade;
    }
    return sum / size;
}

int main() {
    // --- ZADANIE 4 ---
    printf("--- ZADANIE 4 ---\n");
    Student s1;
    printf("Enter name: ");
    scanf("%s", s1.name);
    printf("Enter student ID: ");
    scanf("%d", &s1.id);
    printf("Enter grade: ");
    scanf("%f", &s1.grade);
    
    printf("Student Record:\n");
    printf("Name: %s\n", s1.name);
    printf("ID: %d\n", s1.id);
    printf("Grade: %.2f\n\n", s1.grade);

    // --- ZADANIE 5 ---
    printf("--- ZADANIE 5 ---\n");
    Rectangle r = {5.0, 3.0};
    printf("Rectangle: %.2f x %.2f\n", r.width, r.height);
    printf("Area: %.2f\n", area(r));
    printf("Perimeter: %.2f\n\n", perimeter(r));

    // --- ZADANIE 6 ---
    printf("--- ZADANIE 6 ---\n");
    Student students[3];
    for(int i=0; i<3; i++) {
        printf("Student %d:\n", i+1);
        printf("Enter name: ");
        scanf("%s", students[i].name);
        printf("Enter ID: ");
        scanf("%d", &students[i].id);
        printf("Enter grade: ");
        scanf("%f", &students[i].grade);
        printf("\n");
    }
    
    printf("All Students:\n");
    for(int i=0; i<3; i++) {
        printf("%d. %s (ID: %d) - Grade: %.2f\n", i+1, students[i].name, students[i].id, students[i].grade);
    }
    printf("\n");

    // --- ZADANIE 7 ---
    printf("--- ZADANIE 7 ---\n");
    Person people[5] = {
        {"Alice", 25},
        {"Bob", 30},
        {"Charlie", 28},
        {"Diana", 35},
        {"Eve", 22}
    };
    
    printf("People:\n");
    for(int i=0; i<5; i++) {
        printf("%s (%d)\n", people[i].name, people[i].age);
    }
    
    Person oldest = findOldest(people, 5);
    printf("\nOldest person: %s (%d)\n\n", oldest.name, oldest.age);

    // --- ZADANIE 8 ---
    printf("--- ZADANIE 8 ---\n");
    Student group[5] = {
        {"Alice", 111, 5.0},
        {"Bob", 222, 4.0},
        {"Charlie", 333, 3.5},
        {"Diana", 444, 4.5},
        {"Eve", 555, 5.0}
    };
    
    printf("Students:\n");
    for(int i=0; i<5; i++) {
        printf("%s: %.1f\n", group[i].name, group[i].grade);
    }
    
    printf("\nAverage grade: %.2f\n", calculateAverage(group, 5));

    return 0;
}