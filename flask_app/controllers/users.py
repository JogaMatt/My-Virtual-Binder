from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.binder import Binder


bcrypt = Bcrypt(app)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect('/login')

    binder = Binder.get_all_binders()

    return render_template('profile.html', binder = binder)

@app.route('/login')
def login():
    if 'user_id' in session:
        return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('homepage.html')

@app.route('/account', methods=['POST'])
def account():
    data = { 
        "username" : request.form["username"]
    }
    user_in_db = User.get_by_username(data)
    if not user_in_db:
        flash("Invalid Username")
        return redirect("/login")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Password")
        return redirect('/login')
    session['user_id'] = user_in_db.id
    session['name'] = user_in_db.username
    return redirect("/")

@app.route('/create_account', methods=['POST'])
def create_account():
    if not User.validate_user(request.form):
        return redirect('/register')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "username": request.form['username'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    session['name'] = request.form['username']
    return redirect('/')

@app.route('/register')
def register():
    if 'user_id' in session:
        return redirect('/')
    return render_template('register.html')

@app.route('/create_binder')
def create_binder():
    if 'user_id' not in session:
        return redirect('/login')
    return render_template('create_binder.html')