from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import subprocess
import threading
import platform
from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017/')
db=client.tricode
users=db.users

def adk():
    adk_path = "/Users/pranavmendon/Documents/projects/tricode/.venv/bin/adk"
    process = subprocess.Popen(
        ["adk", "web", "--port", "8000"],
        cwd=adk_path,                  # 👈 This sets the working directory
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,
        close_fds=True
    )

app=Flask(__name__)

app.config["SECRET_KEY"]="vpa.tricode#887"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user=users.find_one({"username": username})
        if user and user['password'] == password :
            session['user_id'] = str(user['_id'])
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login', error='Invalid username or password'))
    return render_template('login.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip
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
            flash('Passwords do not match   ', 'danger')
    return render_template("register.html")


if __name__=="__main__": 
    threading.Thread(target=adk, daemon=True).start()
    app.run(debug=True, port=5000)