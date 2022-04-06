from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.binder import Binder
from flask_app.models.message import Message
from flask_app.models.friend import Friend


from pprint import pprint


bcrypt = Bcrypt(app)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect('/login')

    users = User.get_all_users()

    binders = Binder.get_all_binders()

    messages = Message.get_all_messages()

    friends = Friend.get_all_friends()


    return render_template('profile.html', friends = friends, messages = messages, users = users, binders = binders)

@app.route('/profile/<id>')
def other_user_profiles(id):
    if 'user_id' not in session:
        return redirect('/login')

    data = {
        'id': id
    }

    # pprint(int(data['id']))
    # pprint(session['user_id'])
    if session['user_id'] == int(data['id']):
        return redirect('/profile')

    users = User.get_one(data)
    
    binders = Binder.get_all_binders()

    friends = Friend.get_all_friends()

    return render_template('other_users_profile.html', friends = friends, users = users, binders = binders)

@app.route('/edit_profile/<id>')
def edit_profile(id):
    if 'user_id' not in session:
        return redirect('/login')

    data = {
        'id': id
    }

    users = User.get_one_user(data)
    return render_template('edit_profile.html', users = users)

@app.route('/save_update', methods=['POST'])
def save_update():
    
    data = {
        'username': request.form['username'],
        'profile_icon': request.form['profile_icon'],
        'profile_bio': request.form['profile_bio'],
        'email': request.form['email'],
        'id': session['user_id']
    }

    session['name'] = request.form['username']

    User.update(data)

    return redirect('profile')


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
    pprint(session['user_id'])
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
        "profile_icon": request.form['profile_icon'],
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