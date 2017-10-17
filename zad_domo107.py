"""
Napisz funkcję histogram, która przyjmie listę liczb, po czym zwróci histogram ze znaków #. Jeśli użytkownik poda wartość nie będącą liczbą, funkcja powinna zwrócić wartość None.

Wynikowy histogram ma być wielolinijkowym napisem składającym się ze znaków #. Jedna linijka = jeden słupek histogramu.

Przykład:

h = histogram([2, 6, 3, 1])
print(h)
##
######
###
#
"""

def histogram(list_1):
    st =""
    for i in list_1:
        if isinstance(i, int):
            st += "#"*i + "\n"
        else:
            st += "None" + "\n"

    return st



print(histogram([2, 6, 3,"dsfsda"]))