"""
Używając Flaska napisz aplikację, która na żądanie GET /losuj wylosuje i wyświetli 3 cyfry (cyfry mogą się powtarzać)
"""
from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def index():
    l = random.sample([x for x in range(10)], 3)
    return "{} {} {}".format(*l)

if __name__ == "__main__":
    app.run(debug=True)