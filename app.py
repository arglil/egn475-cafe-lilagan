from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Lilagan Café"


@app.route("/about")
def about():
    return "Lilagan Café is a neighborhood coffee shop serving fresh coffee and pastries."
