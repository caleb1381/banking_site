from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def mainpage():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if "__main__" == __name__:
    app.run(debug=True)
