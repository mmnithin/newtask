from flask import Flask,render_template
from employeeList import Employee

getemployee=Employee()

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/employee')
def employee():
    return render_template("employeeData.html",employeeList=getemployee)

if (__name__ == '__main__'):
   app.run(debug=True)
