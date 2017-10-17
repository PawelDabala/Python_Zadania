"""
Napisz funkcję format_date, która przyjmie 3 parametry:
day: dzień,
month: miesiąc,
year: rok.
Funkcja powinna sprawdzić, czy data jest poprawna:
miesiąc powinen być w granicach (1, 12),
dzień nie może być większy od 30 - 31 (lub 28 w przypadku lutego, pomiń sprawdzanie lat przestępnych).
Jeśli któryś z warunków będzie niezgodzny z kalendarzem, funkcja ma zwrócić None.
Funkcja powinna zwrócić sformatowany łańcuch tekstowy w formacie "dzień miesiąc rok".
"""
import datetime

# ver_1

def format_date(dd, mm, yyyy):
    try:
        d = datetime.date(yyyy, mm, dd)
        return d.strftime('%d %B %Y')
    except ValueError:
        return None