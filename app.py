from flask import Flask, render_template, request, g
import sqlite3 as sql
app = Flask(__name__)

DATABASE = 'Teams.db'

@app.route('/registerteam')
def new_team():
   return render_template('new_team.html')

@app.route('/codingq1')
def coding_q1():
   return render_template('codingquestion1.html')

@app.route("/")
def main():
    cur = get_db().cursor()
    return render_template("home.html")

@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html")

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect(DATABASE)
    return db

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         pin = request.form['pin']
         
         with sql.connect("Teams.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO REGISTERED (NAME,PASSWORD) VALUES (?,?)",(nm,pin) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/registermember')
def new_mem():
   return render_template('new_member.html')

@app.route('/addmem',methods = ['POST', 'GET'])
def addmem():
   if request.method == 'POST':
      try:
         player_name = request.form['name']
         team = request.form['team']
         pin = request.form['pin']
   
         with sql.connect("Teams.db") as con:
            cur = con.cursor()

            result = cur.execute("SELECT * FROM REGISTERED WHERE NAME = (?) AND PASSWORD = (?)", (team, pin)) 
            num = 0
            
            for res in result:
                num += 1


            if num > 0 and num < 3:    
              cur.execute("INSERT INTO TEAM_MEMBERS (NAME,TEAM_NAME) VALUES (?,?)",(player_name,team))
              con.commit()
              msg = "Record successfully added"
            elif num == 0:
              msg = "Invalid team credentials"
            else:
              msg = "Team size is out of bounds"
      except:
         con.rollback()
         msg = "Failed to add team"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()


if __name__ == '__main__':
   app.run(debug = True)
