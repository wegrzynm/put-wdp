# Lab 9: Zadania MEGA rozszerzone

import itertools

def solve_sat(variables, clauses):
    """
    Prosty SAT solver brute-force.
    variables: lista nazw zmiennych, np. ['A', 'B', 'C']
    clauses: lista klauzul, gdzie każda klauzula to funkcja przyjmująca słownik przypisań
    """
    n = len(variables)
    print(f"Sprawdzanie {2**n} kombinacji dla zmiennych: {variables}")
    
    for values in itertools.product([True, False], repeat=n):
        assignment = dict(zip(variables, values))
        
        if all(clause(assignment) for clause in clauses):
            return assignment
            
    return None

def zadanie_12_sat_solver():
    print("Zadanie 12: Simple SAT Solver")
    print("Formuła: (A ∨ B) ∧ (¬A ∨ C) ∧ (¬B ∨ ¬C)")
    
    variables = ['A', 'B', 'C']
    
    # Definicja klauzul
    # (A OR B)
    clause1 = lambda d: d['A'] or d['B']
    # (NOT A OR C)
    clause2 = lambda d: (not d['A']) or d['C']
    # (NOT B OR NOT C)
    clause3 = lambda d: (not d['B']) or (not d['C'])
    
    clauses = [clause1, clause2, clause3]
    
    result = solve_sat(variables, clauses)
    
    if result:
        print(f"Znaleziono rozwiązanie: {result}")
        v1 = result['A'] or result['B']
        v2 = (not result['A']) or result['C']
        v3 = (not result['B']) or (not result['C'])
        print(f"Weryfikacja: {v1} AND {v2} AND {v3} = {v1 and v2 and v3}")
    else:
        print("Nie znaleziono rozwiązania (formuła niespełnialna).")
        
    print("\nPrzykład formuły niespełnialnej: (A) ∧ (¬A)")
    res_unsat = solve_sat(['A'], [lambda d: d['A'], lambda d: not d['A']])
    print(f"Wynik dla (A ∧ ¬A): {res_unsat}")
    print("-" * 30)

if __name__ == "__main__":
    zadanie_12_sat_solver()
