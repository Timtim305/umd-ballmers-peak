<<<<<<< HEAD
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()
=======
from flask import Flask, g
import sqlite3

DATABASE = 'Teams.db'
>>>>>>> 1b358197c99ec755ec4b4b0cd74fd4241879efe8

print 'Everything compiles'

app = Flask(__name__)

@app.route("/")
def main():
    
    cur = get_db().cursor()
    return "Welcome!"

<<<<<<< HEAD
if __name__ == '__main__':
    app.run()
=======
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

if __name__ == '__main__':
    app.run()
>>>>>>> 1b358197c99ec755ec4b4b0cd74fd4241879efe8
