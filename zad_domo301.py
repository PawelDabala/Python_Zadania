"""
Napisz funkcję random_average(n), która wylosuje n liczb naturalnych od 1 do 100, zsumuje je, po czym
zwróci średnią arytmetyczną z tych liczb.
"""

import random

def random_average(n):
    return sum(random.sample(range(1, 101), n)) / n

print(random_average(100))
