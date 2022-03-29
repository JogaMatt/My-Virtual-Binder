from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.card import Card
from flask_app.models.user import User

from pprint import pprint

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/start_search', methods=['POST'])
def start_search():
    data = Card.get_all(request.form['search'])
    pprint(data)
    return redirect('/search')

@app.route('/search_one/<id>')
def search_one(id):
    data = Card.get_one(id)
    pprint(data)
    return redirect('/profile')

@app.route('/card/<id>')
def uniqueCard(id):
    card = Card.get_one(id)

    data = {
        'id': session['user_id']
    }

    user = User.get_one(data)

    pprint(id)
    return render_template('showcard.html', data = card, user = user )

@app.route('/save_card', methods=['POST'])
def save_to_binder():
    Card.save(request.form)
    return redirect('/profile')