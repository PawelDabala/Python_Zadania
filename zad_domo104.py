"""
Napisz funkcję o nazwie dogs_age, który przeliczy wiek psa w psich latach.

funkcja powinna przyjmować wiek psa jako parametr,
dla pierwszych dwóch lat, każdy rok życia psa jest równy 10.5 ludzkiego roku,
powyżej dwóch lat, każdy rok życia psa, to 4 ludzkie lata,
funkcja powinna zwrócić wiek psa.
Przykład:

azor = dogs_age(1.5)  # spodziewany wynik: 1.5 * 10.5 = 15.75

burek = dogs_age(5)  # spodziewany wynik: 2 * 10.5 + 3 * 4 = 33s
"""

def dogs_age(age):
    if age < 3:
        return age * 10.5
    else:
        return 2 * 10.5 + ((age-2)*4)


print(dogs_age(33))

