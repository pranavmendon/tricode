from flask import Flask, render_template, request
from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017/')
db=client.tricode
collection=db.login_data

app=Flask(__name__)
app.config["SECRET_KEY"]="vpa.tricode#887"

@app.route("/")
def home():
    return render_template("Home_page.html")

@app.route("/login" methods=["POST"])
def login():

    if methods=="POST":
        pass
    return render_template("Login.html")

if __name__=="__main__":
    app.run(debug=True)