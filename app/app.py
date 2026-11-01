from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Project1</h1>
    <p>Flask application is running.</p>
    """
