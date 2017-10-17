"""
Napisz i uruchom prosty kalulator, który:

wyświetli formatkę z dwoma polami na wprowadzenie liczb i listę wybieraną operacji (+, -, *, /)
po wciśnięciu guzika "wyślij" policzy wynik i wyświetli go na ekranie
"""

from flask import Flask, request

app = Flask(__name__)

form_1 = """
    <form action="/" method='POST' >
         
          <input type="text" name="nr_1" />
          <select name="znak">
              <option value="dodaj">+</option>
              <option value="odejmij">-</option>
              <option value="multi">*</option>
              <option value="podziel">/</option>
            </select>
          <input type="text" name="nr_2" />
          <input type="submit" name="submit" />
    </form>
"""

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == "GET":
        return form_1
    else:

        nr_1 = int(request.form["nr_1"])
        znak = request.form["znak"]
        nr_2 = int(request.form["nr_2"])

        if znak == "dodaj":
            return str(nr_1 + nr_2)
        elif znak == "odejmij":
            return str(nr_1 - nr_2)
        elif znak == "multi":
            return str(nr_1 * nr_2)
        elif znak == "podziel":
            return str(nr_1 / nr_2)



if __name__ == "__main__":
    app.run(debug=True)