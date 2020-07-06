from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"

@app.route("/vikka")
def vikka():
    return "Hello, Vikka!"


if __name__ == "__main__":
    app.run(debug=True)