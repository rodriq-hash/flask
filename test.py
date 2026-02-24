# import flask
from flask import *
# initialize the app
app=Flask(__name__)
# define your route/endpiont
@app.route("/api/home")
# define your function
def home ():
    return "welcome home"
@app.route("/api/products")
def products():
    return "welcome to our products"
# services
@app.route("/api/services")
def services():
    return "welcome to our services"
# contact
@app.route("/api/contact")
def contact():
    return "please contact us kindly"
@app.route("/api/calc", methods=["POST"])
def calc ():
    num1=request.form["num1"]
    num2=request.form["num2"]
    answer=int (num1)+int (num2)
    return jsonify({"sum":answer})












# run the app
app.run(debug=True)