from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<c> Hello World </c>"

if __name__ == "__main__":
    app.run()