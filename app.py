from flask import Flask, render_template, request
from db import addCont,viewCont
import sqlite3
app = Flask(__name__)


@app.route('/')
def viewContestants():
    return viewCont("testin")

@app.route('/add', methods=['GET', 'POST'])
def addContestants():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        ig = request.form["ig"]    
        try:
            addCont(name, phone, ig)
            return "Success!"
        except sqlite3.IntegrityError:
            return "Error" 
    elif request.method == "GET":       
        return render_template("addContestant.html")

@app.route('/view', methods=["GET","POST"])
def viewSpecific():
    if request.method == "POST":
        contName = request.form["name"]
        try:
            name, ph, ig = viewCont(contName)
            return render_template("successContestant.html", ph=ph, name=name, ig=ig)
        except Exception as e:
            print(e)
            return "ERROR"
    elif request.method == "GET":       
        return render_template("viewContestant.html")   

if __name__ == '__main__':
    app.run()
