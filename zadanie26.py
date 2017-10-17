"""
Napisz funkcję message, która jako parametr przyjmie słownik o następujących kluczach:

name,
role,
movie.
Następnie niech funkcja przygotuje sformatowany napis: "In movie, name is a role.",
gdzie w odpoweidnie miejsca podstawi wartości z ww. kluczy. Jeśli któregoś z kluczy nie będzie w słowniku, funkcja ma zwrócić wartość None.
"""


def message(dic_1):
    return "In {movie}, {name} is a {role}.".format(**dic_1)


input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}

print(message(input_dict))
