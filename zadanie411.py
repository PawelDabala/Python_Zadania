"""
Używając Flaska, napisz i uruchom program, który:

po wejściu metodą GET wyświetli pusty formularz z następującymi polami:
imię,
nazwisko
przycisk "Wyślij"
powyższy formularz ma wysyłać dane metodą POST.
po wejściu metodą POST wyświetli komunikat „Witaj imię nazwisko”.
"""
from flask import Flask, request


app = Flask(__name__)

form_1 = """
        <form action="/" method='POST' >
             <label>Imie
              <input type="text" name="imie" />
              </label>
              <label>Nazwisko
              <input type="text" name="nazwisko" />
              </label>
              <input type="submit" name="submit" />
        </form>
        """

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return  form_1
    else:
        imie = request.form['imie']
        nazwisko = request.form['nazwisko']
        return "Witaj {} {}".format(imie, nazwisko)


if __name__ == "__main__":
    app.run(debug=True)
