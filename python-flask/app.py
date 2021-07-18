from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Halan ROCKS It"


@app.route("/<string:x>=<int:num>")
def number(x, num):
    x = num
    return str(x * x)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
