"""
Napisz funkcję list_keys(d), gdzie d to dowolny słownik. Niech funkcja przeiteruje pętlą for po
kluczach słownika i zwróci listę tych kluczy. Sprawdź w dokumentacji, czy można zrobić to prościej.
"""

def list_keys(d):
    l = [k for k, v in d.items()]
    return l


d = {'a': 12, 'b': 13}

print(list_keys(d))




