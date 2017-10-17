"""
Napisz funkcję divide, która przyjmie dwa argumenty: a i b. Muszą być to liczby naturalne. Funkcja ma działać następująco:

ma sprawdzić, czy a i b to liczby,
ma obsłużyć problem dzielenia przez zero.
Oba powyższe przypadki muszą być obsłużone przez wychwytywanie wyjątków.

Jeśli któryś z powyższych warunków nie zostanie spełniony, funkcja ma zwrócić None.
"""

def divde(a,b):
    try:
        return a/b
    except (TypeError, ZeroDivisionError):
        return None

print(divde("1dfsd", 2))

