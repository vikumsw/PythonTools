from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/vikka")
def vikka():
    return "Hello, Vikka!"


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/parent")
def parent():
    return render_template("template.html")

@app.route("/other")
def other():
    return render_template("other.html")

if __name__ == "__main__":
    app.run(debug=True)