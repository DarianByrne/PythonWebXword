from flask import Flask, render_template
from xword import matches

app = Flask(__name__)

@app.get("/hello")
def hello():
    return "Hello from /hello!"

@app.get("/bye")
def byebye():
    return "I'm so sorry to see you go (sniff)..."

@app.get("/whoops")
def omg():
    first = 10
    second = 300
    return render_template(
        "whoops.html",
        result=first/second,
        the_title="The results are in!",
    )

@app.get("/words")
def words():
    return matches("f___")

if __name__ == "__main__":
    app.run(debug=True)