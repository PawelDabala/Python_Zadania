"""
Napisz funkcję censor, która przyjmie jako parametr dowolnie długi łańcuch tekstowy. Następnie:

rozbije łańcuch tekstowy na listę wyrazów,
sprawdzi, czy nie znajdują się w nim słowa niedozwolone,
jeśli tak -- zamieni je na cztery gwiazdki (****)
ponownie połączy listę w string i zwróci wartość.
Słowa niedozwolone:

Java, C#, Ruby, PHP.

Słowa niedozwolone trzymaj jako listę wewnątrz funkcji censor.

Przykład

c = censor("Java is the best, but PHP is the bestest!")  # ;-)
print (c)
**** is the best, but **** is the bestest!
"""

def censor(text1):
    forb = ["Java", "C#", "Ruby", "PHP"]
    txt_list = text1.split(" ")
    new_list = []
    for i in txt_list:
        if i in forb:
            new_list.append("****")
        else:
            new_list.append(i)
    return " ".join(new_list)

print(censor("Java is the best, but PHP is the bestest!"))
