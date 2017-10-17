"""
Napisz funkcję find_number, która przyjmie liczbę i sprawdzi, czy liczba jest podzielna przez 4
i odpowiednio zwróci True lub False.
"""

def find_number(num):
    if num % 4 == 0:
        return True
    else:
        return False


print(find_number(9))
