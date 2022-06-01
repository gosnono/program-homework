from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, 수업중</p>"

app.run(debug=True, host="0.0.0.0")
