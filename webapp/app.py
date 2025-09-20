from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017/')
db=client.tricode
#users=db.login_data
users={
    "test":"pass123",
    "vais":"miu"
}

app=Flask(__name__)
app.config["SECRET_KEY"]="vpa.tricode#887"

@app.route("/")
def home():
    return render_template("Home_page.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('Login.html')
@app.route("/register")
def register():
    return render_template("register.html")
if __name__=="__main__":
    app.run(debug=True)