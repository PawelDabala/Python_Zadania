"""
Napisz i uruchom aplikację, która wyświetli na ekranie aktualny czas.
"""
from flask import Flask
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def index():
    return datetime.now().strftime('%H:%M:%S')



if __name__ == "__main__":
    app.run(debug=True)