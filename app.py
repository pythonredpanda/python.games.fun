
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects/score-clicker")
def score_clicker():
    return render_template("score_clicker.html")

@app.route("/static/styles.css")
def coular():
    return render_template("styles.css")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
