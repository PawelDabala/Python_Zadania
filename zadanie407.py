"""
Napisz i uruchom aplikację, która:

wyświetli na ekranie formularz pytający użytkownika o imię
po jego wysłaniu powita użytkownika napisem: "Witaj <Imię>!"

"""
from flask import Flask, request

app = Flask(__name__)

form_1 = """
    <form action="/" method='POST' >
          <label for="first-name">imie</label>
          <input id="first-name" type="text" name="name" />
          <input type="submit" name="submit" />
    </form>
"""


@app.route("/", methods=['GET', 'POST'] )
def index():
    if request.method == 'GET':
        return form_1
    else:
        name = request.form["name"]
        return name


if __name__ == "__main__":
    app.run(debug=True)


