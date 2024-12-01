from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def mainpage():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/home")
def statichome():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/payment")
def payment():
    return render_template("payment.html")


if "__main__" == __name__:
    app.run(debug=True)
