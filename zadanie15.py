"""
Napisz funkcję create_name, która przyjmie następujące parametry:

name: imię,
surname: nazwisko,
nickname: pseudonim.
Funkcja ma zwrócić łańcuch tekstowy z połączonymi paramterami w postaci Imię "Pseudonim" Nazwisko.
"""


def create_name(name, surname, nickname):
    return '{} "{}" {}'.format(name, nickname, surname)


print(create_name("Pawe", "Dabala", "Pablo"))

