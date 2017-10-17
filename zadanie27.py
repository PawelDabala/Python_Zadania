"""
Napisz funkcję d6(num), która zasymuluje rzuty kostką sześcienną.
num to parametr, który oznacza liczbę rzutów kostką. Funkcja ma zwrócić sumę wyrzuconych oczek.
"""
from random import randint

def d6(num):
    return sum([randint(1, 6) for x in range(num)])


print(d6(2))
