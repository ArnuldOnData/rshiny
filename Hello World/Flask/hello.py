from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'My First Web-App in Python!!!'