"""
Używając Flaska napisz program który
będzie zwracał wynik dodawania dwóch liczb przesłanych w żądaniu GET /licz/liczba1/liczba2
"""
from flask import Flask

app= Flask(__name__)

@app.route("/licz/<int:x>/<int:y>")
def index(x,y):
    return str(x+y)

if __name__ == "__main__":
    app.run(debug=True)