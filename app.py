from flask import Flask, g
import sqlite3

DATABASE = 'Teams.db'

print 'Everything compiles'

app = Flask(__name__)

@app.route("/")
def main():
    cur = get_db().cursor()
    return "Welcome!"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

if __name__ == '__main__':
    app.run()
