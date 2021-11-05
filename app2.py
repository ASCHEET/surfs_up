from flask import Flask
app = Flask(___name___)

@app.route('/')
def hello_world():
    return 'Hello World'