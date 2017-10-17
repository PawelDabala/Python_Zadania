"""
#### Zadanie 5.
Napisz funkcję `chessboard`, który przyjmie parametr `n` jako opcjonalny.
Standardowa wartość parametru ma wynosić 8. Funkcja ma rysować na ekranie szachownicę złożoną ze znaków # i spacji.
**Przykład dla n=8:**
"""



def chessboard2(n=8):
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print( ' ', end ='')
            else:
                print('##', end='')
        print('')