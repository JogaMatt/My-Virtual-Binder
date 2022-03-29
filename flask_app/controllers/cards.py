from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.card import Card
from pprint import pprint

@app.route('/search', methods=['POST'])
def search():
    data = Card.get_all(request.form['search'])
    pprint(data)
    return redirect('/profile')

@app.route('/search_one/<id>')
def search_one(id):
    data = Card.get_one(id)
    pprint(data)
    return redirect('/profile')

@app.route('/card/<id>')
def uniqueCard(id):
    data = Card.get_one(id)
    pprint(id)
    return render_template('showcard.html', data = data )