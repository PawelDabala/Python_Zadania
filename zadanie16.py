"""
napisz funkcję calculate_net, która przyjmie argumenty:

gross, czyli kwotę brutto ceny zakupu,
vat, czyli wartość podatku VAT. Możesz założyć, że VAT ma być liczbą zmiennoprzecinkową z zakresu 0 – 1.
Funkcja ma zwrócić wartość netto ceny. Jakie obliczenia musisz wykonać?
"""


def calculate_net(gross, vat):
    return '{:.2f} '.format(gross / (1+vat))


print(calculate_net(1620, 0.23))

