"""
Napisz funkcję find_first_and_last, która przyjmie listę lub krotkę.
Następnie zwróć krotkę, która będzie zawierać pierwszy i ostatni element parametru.
"""

def find_first_and_last(lis_1):
    return tuple([lis_1[0],lis_1[-1]])


print(find_first_and_last([1, 2, 3, 4]))

