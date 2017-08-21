from flask import Flask
import sqlite3


print 'Everything compiles'

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"


if __name__ == "__main__":
    app.run()

