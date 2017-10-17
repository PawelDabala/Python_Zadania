"""
W tym zadaniu nie musisz pisać funkcji)

Napisz program, który:

poprosi użytkownika o podanie 2 liczb z klawiatury,
wprowadzone dane zamieni na liczby naturalne,
podzieli jedną liczbę przez drugą,
wyświetli wynik.
Dodatkowo należy zabezpieczyć się przed wszystkimi możliwymi błędami (niewłaściwe dane, dzielenie przez zero).

Sprawdź w interaktywnej konsoli Pythona, jakie błędy mogą wystąpić i zabezpiecz się przed nimi.
"""

def program():
    try:
        a = int(input("Podaj liczbe: "))
        b = int(input("Podaj liczbe: "))
        wynik = a / b
    except (ZeroDivisionError, ValueError):
        return None
    else:
        return wynik


print(program())
