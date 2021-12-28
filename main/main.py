from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>복주머니를 만들어보아요</p>"