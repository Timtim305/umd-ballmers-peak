from flask import Flask, render_template, request, g
import sqlite3 as sql
app = Flask(__name__)

DATABASE = 'Teams.db'

with sql.connect("Teams.db") as con:
    cur = con.cursor()

    result = cur.execute("SELECT * FROM REGISTERED WHERE NAME = (?) AND PASSWORD = (?)", ("admin", "admin")) 
    num = 0
    
    for res in result:
        num += 1

    print num