"""
Napisz funkcję create_list, która przyjmie dwa argumenty dowolnego typu,
a następnie zwróci listę, której kolejne elementy będą parametrami powtórzonymi czterokrotnie.
"""

def create_list(a, b):
    return [a, b] * 4


print(create_list(2, 4))


