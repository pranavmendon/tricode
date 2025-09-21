from flask import Flask, render_template, request, redirect, url_for, flash, session

from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017/')
db=client.tricode
users=db.login_data


app=Flask(__name__)
app.config["SECRET_KEY"]="vpa.tricode#887"

@app.route("/")
def index():
    return render_template("Home.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user=users.find_one({"username": username})
        if user and user['password'] == password:
            session['user_id'] = str(user['_id']) 
            session["username"]=user["username"]
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('Login.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if users.find_one({"username": username}):
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))
        if password == confirm_password:
            db.users.insert_one({"username": username, "password": password})
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Passwords do not match', 'danger')
    return render_template("Register.html")
if __name__=="__main__":
    app.run(debug=True, port=8080)
    