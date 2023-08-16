from flask import Flask

app = Flask("my web application")


@app.route("/")
def hello_flask():
    return "hello from flask!"
