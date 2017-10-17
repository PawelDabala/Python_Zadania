"""
Napisz funkcję max_length, która przyjmie listę wyrazów. Funkcja powinna zwrócić listę słów krótszych od 5 znaków.

Przykład

l = max_length(['Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie'])
print(l)
['moja', 'ty', 'jak']
"""

def max_length(lis1):
    return [x for x in lis1 if len(x)<5]


print(max_length(['Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie']))