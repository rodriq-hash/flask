import flask
from flask import*
import pymysql
import os
# initialize the app
app=Flask(__name__)
app.config["UPLOAD_FOLDER"]="static/images"
# define your route
@app.route("/api/add_product",methods=["POST"])
# define your function 
def add_product ():
    # get product input
    name=request.form["name"]
    brand=request.form["brand"]
    model=request.form["model"]
    storage=request.form["storage"]
    ram=request.form["ram"]
    battery=request.form["battery"]
    price=request.form["price"]
    stock=request.form["stock"]
    photo=request.files["photo"]
    # get file name
    filename=photo.filename
    # show where the image would be saved 
    photopath=os.path.join(app.config["UPLOAD_FOLDER"],filename)
    # SAVE THE PHOTO
    photo.save(photopath)
    # establish connection
    connection=pymysql.connect(user="root",host="localhost",password="",database="kifarusokogarden")
    # define your cursor
    cursor=connection.cursor()
    # define sql to insert
    sql="insert into smartphones(name,brand,model,storage,ram,battery,price,stock,photo)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # define data 
    data=(name,brand,model,storage,ram,battery,price,stock,filename)
    # execute/run querry 
    cursor.execute(sql,data)
    # commit/save changes 
    connection.commit()
    return jsonify({"message":"product added successsful"})






# run the app
app.run(debug=True)