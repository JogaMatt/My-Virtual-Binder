from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.binder import Binder
from flask_app.models.card import Card
from pprint import pprint

@app.route('/binder_creation')
def binder_creation():
    if 'user_id' not in session:
        return redirect('/login')
    return render_template('binder.html')

@app.route('/submit_binder', methods=['POST'])
def submit_binder():
    pprint(request.form)
    Binder.save(request.form)

    return redirect('/profile')

@app.route('/show_binder/<id>')
def show_binder(id):

    data = {
        'binder_id': id
    }

    session['binder_id'] = id

    cards = Card.get_my_cards(data)
    return render_template('mybinder.html', cards = cards)