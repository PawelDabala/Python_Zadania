"""
Napisz i uruchom swoją pierwszą aplikację Flaska, która po wejściu na / powita użytkownika napisem:
"Witaj użytkowniku!". Po wejściu na /hello/<imie> wypisze imię użytkownika podane w parametrze <imię>.

"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Witaj użytkowniku"

@app.route("/hello/<imie>")
def hello(imie):
    return imie




app.run(debug=True)




