"""
Napisz funkcję safe_get, która przyjmue dwa parametry:

l: dowolna lista,
index: liczba.
Funkcja powinna zwracać element listy o indeksie index. Jeśli nie ma takiego elementu, powinna zwracać None.

uwaga: zrób to używając obsługi wyjątków.
"""


def safe_get(l, index):
    try:
        return l[index]
    except IndexError:
        return None


l2 = []

print(safe_get(l2, 1))
