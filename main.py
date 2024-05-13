from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World! This is your main page."


if __name__ == "__main__":
    app.run(debug=True)
