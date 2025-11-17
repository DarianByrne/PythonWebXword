from flask import Flask

app = Flask(__name__)

@app.get("/hello")
def hello():
    return "Hello from the smallest Flask webapp there is!"

if __name__ == "__main__":
    app.run()