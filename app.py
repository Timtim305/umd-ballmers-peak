from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

print 'Everything compiles'

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

if __name__ == '__main__':
    app.run()
