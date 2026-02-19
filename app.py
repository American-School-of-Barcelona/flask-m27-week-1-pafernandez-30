from flask import Flask, render_template

app = Flask(__name__)

# TODO: Add your routes below this line

@app.route("/")
def home():
    return render_template ("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
    