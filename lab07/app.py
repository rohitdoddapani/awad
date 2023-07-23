import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
import hashlib

app = Flask(__name__)
app.secret_key = "my_secret" 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/C:/Windows/System32/web.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
# print('sqlite:///' + os.path.join(basedir, 'database.db'))
db = SQLAlchemy(app)

# class ExampleTable(db.Model):
#     id = db.Column(db.Integer,primary_key=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'
    
@app.route('/')
def index():
    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Password does not meet criteria or does not match the confirmation.')
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash('Email address is already registered.','error')
            return redirect(url_for('register'))

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('thankyou'))

    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        user = User.query.filter_by(email=email, password=hashed_password).first()

        if user:
            return render_template('secretPage.html')
        else:
            flash('Invalid email or password.','error')
            return redirect(url_for('login'))

    return render_template('signin.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    with app.app_context(): 
        db.create_all()
    app.run(debug=True)

