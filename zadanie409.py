"""
Napisz i uruchom prostą zgadywankę, która:

wylosuje poprawną odpowiedź,
zapyta użytkownika - "Spróbuj zgadnąć liczbę", wyświetlając formularz
po wysłaniu formularza z odpowiedzią, wypisze na ekranie:
"za mało!" jeżeli odpowiedź użytkownika jest mniejsza niż liczba i formatkę jeszcze raz,
"za dużo!" jeżeli odpowiedź użytkownika jest większa niż liczba i formatkę jeszcze raz,
"Gratulacje, udało Ci się!" jeżeli użytkownik trafi.
"""
from flask import Flask, request
import random

app= Flask(__name__)
form_1 = """
        <form action="/" method='POST' >
         <label>Podaj liczbe
          <input type="text" name="nr" />
          </label>
          <input type="submit" name="submit" />
    </form>

        """
number = random.randint(1, 5)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == "GET":
        return form_1
    else:
        nr = int(request.form['nr'])

        if number < nr:
            return "<p> Za dużo </p>" + form_1
        if number > nr:
            return "<p> Za malo </p>" + form_1
        else:
            return "Hura, trafiles"



if __name__ == "__main__":
    app.run(debug=True)