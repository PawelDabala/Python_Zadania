"""
Napisz funkcję phone, która przyjmie parametr number, który oznacza numer telefonu.
Funkcja ma sprawdzić, czy podany numer znajduje się na liście numerów (wymyśl jakieś).
Jeśli nie - musi zwrócić wyjątek typu Exception z komentarzem Nie ma takiego numeru!.
"""

def phone(number):
    lis_numbe=[1,2,3]
    if number not in lis_numbe:
        raise Exception("Nie ma takiego numeru")


print(phone(10))
