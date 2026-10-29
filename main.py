from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def name():
    return render_template("name.html"), 200

if __name__ == "__main__":
    app.run(debug=True)