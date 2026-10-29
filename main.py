from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def name():
    dates = ["April 7, 2014", "April 2, 2014"]
    return render_template("name.html", dates=dates), 200

if __name__ == "__main__":
    app.run(debug=True)