from flask import Flask, render_template, request
import xword

app = Flask(__name__)

@app.get("/")
def opening_page():
    first = 10
    second = 300
    return render_template(
        "pattern.html",
        the_title="Welcome to Xword on the Web!",
    )

@app.post("/processpattern")
def get_the_results():
    pat = request.form["pattern"]
    results = xword.find_possible_matches(pat)
    return render_template(
        "results.html",
        the_title="Possible Matches",
        the_results=results
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)