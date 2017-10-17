"""
Zadanie 2 - rozwiązywane z wykładowcą.

Napisz funkcję tomorrow, która zwróci jutrzejszą datę.
"""
import datetime

def tomorrow():
    today = datetime.date.today()
    return today + datetime.timedelta(days=1)


print(tomorrow())