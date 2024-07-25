from flask import Flask, request
from main import hello_http

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def server():
    return hello_http(request)

if __name__ == "__main__":
    app.run(debug=True)