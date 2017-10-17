"""
Napisz funkcję mean(numbers),
gdzie numbers to lista liczb dowolnego typu. Funkcja powinna zwrócić średnią arytmetyczną wszystkich elementów listy
numbers. Czy znasz jakiś sposób, by ułatwić sobie pracę?
"""

import statistics

def mean1(list1):
    return statistics.mean(list1)


print(mean1([1, 2, 3]))


