from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.binder import Binder
from flask_app.models.card import Card

from pprint import pprint

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

    binders = Binder.get_all_binders()

    data = {
        'id': session['user_id']
    }


    return render_template('mybinder.html', binders = binders, cards = cards)

@app.route('/other_users_binder/<id>')
def other_users_binder(id):

    data = {
        'binder_id': id
    }

    session['binder_id'] = id

    cards = Card.get_my_cards(data)

    binders = Binder.get_all_binders()

    data = {
        'id': session['user_id']
    }


    return render_template('other_users_binder.html', binders = binders, cards = cards)