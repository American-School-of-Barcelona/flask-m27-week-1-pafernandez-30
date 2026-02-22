from flask import Flask, render_template

app = Flask(__name__)

# TODO: Add your routes below this line

@app.route("/")
def home():
    return render_template ("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/tasks")
def tasks():
    return render_template("tasks.html")

@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", name=name)

@app.route("/nav")
def nav():
    return render_template("nav.html")


if __name__ == "__main__":
    app.run(debug=True)
    