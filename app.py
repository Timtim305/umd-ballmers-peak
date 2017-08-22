from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return "Welcome!"

@app.route('/registerteam')
def new_team():
   return render_template('new_team.html')

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


if __name__ == '__main__':
   app.run(debug = True)