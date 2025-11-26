from flask import Flask, render_template, request

import model
import xword

app = Flask(__name__)

@app.get("/")
def opening_page():
    data = model.get_log_data()
    return render_template(
        "pattern.html",
        the_title="Welcome to Xword on the Web!",
        data_table=data
    )

@app.get("/bytimestamp")
def order_by_timestamp():
    data = model.get_log_data("ts")
    return render_template(
        "ordered.html",
        data_table=data
    )

@app.get("/bypattern")
def order_by_pattern():
    data = model.get_log_data("pattern")
    return render_template(
        "ordered.html",
        data_table=data
    )

@app.get("/bymatches")
def order_by_matches():
    data = model.get_log_data("matches")
    return render_template(
        "ordered.html",
        data_table=data
    )

@app.post("/processpattern")
def get_the_results():
    pat = request.form["pattern"]
    results = xword.find_possible_matches(pat)

    model.add_to_database(pat, len(results))

    return render_template(
        "results.html",
        the_title="Possible Matches",
        the_results=results
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)