from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects/score-clicker")
def score_clicker():
    return render_template("score_clicker.html")

if __name__ == "__main__":
    try:
        app.run(debug=True, host="127.0.0.1", port=5000)
    except Exception as e:
        print("ERROR:", e)
        input("Press Enter to close...")
