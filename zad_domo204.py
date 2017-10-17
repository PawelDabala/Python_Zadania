"""
Napisz funkcję find_boundaries, która przyjmie listę liczb. Funkcja powinna zwrócić krotkę z najmniejszą i największą
liczbą w zestawie. Jeśli na liście będzie element, nie będący liczbą, powinien zostać zignorowany.

Przykład:

b = find_boundaries([1, 5, 2, 3.5, -1])
print(b)
(-1, 5)
b = find_boundaries([0, 2, "a kuku!", 10])
print(b)
(0, 10)
"""
import numbers

def find_boundaries(lis_1):
    lis_temp = [x for x in lis_1 if isinstance(x, numbers.Number)]

    return [min(lis_temp), max(lis_temp)]



print(find_boundaries([1, 5, 2, 3.5, -1]))


