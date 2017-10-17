"""
Napisz funkcję check_palindrome, która pobierze jeden wyraz i sprawdzi, czy jest palindromem.
Funkcja powinna zwracać True, jeśli łańcuch jest palindromem, False, jeśli nie jest.
"""
def check_palindrome(txt):
    if txt.upper() == txt[::-1].upper():
        return True
    else:
        return False

print(check_palindrome("Kajak"))
