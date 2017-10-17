"""
Napisz funkcję make_tuple, która przyjmie cztery parametry: a, b, c i d. Niech parametry c i d
bedą opcjonalne i ich standardowe wartości będą wynosiły odpowiednio 3 i 4. Zwróć krotkę czterech elementów, której kolejnymi elementami będą wartości parametrów.
"""

def make_tuple(a, b, c=3, d=4):
    return tuple([a, b, c, d])


print(make_tuple("mama", "tata"))
