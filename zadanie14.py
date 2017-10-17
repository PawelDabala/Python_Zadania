"""
Napisz funkcję convert_to_usd, która przyjmuje parametr zlotys,
czyli kwotę w złotówkach. Funkcja ma zwrócić podaną kwotę w dolarach amerykańskich. Jako przelicznik przyjmij wartość 3,85 PLN = 1 USD.
"""


def convert_to_usd(zlotys, usd=3.85):
    return  zlotys/usd


print(convert_to_usd(100))
