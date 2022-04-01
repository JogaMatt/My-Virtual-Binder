from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.card import Card
from flask_app.models.user import User


from pprint import pprint

@app.route('/search')
def search():
    if 'user_id' not in session:
        return redirect('/login')
    return render_template('search.html')

@app.route('/start_search', methods=['POST'])
def start_search():
    data = Card.get_all(request.form['search'])
    pprint(data)
    return redirect('/search')

@app.route('/search_one/<id>')
def search_one(id):
    if 'user_id' not in session:
        return redirect('/login')
    data = Card.get_one(id)
    pprint(data)
    return redirect('/profile')

@app.route('/card/<id>')
def uniqueCard(id):
    card = Card.get_one(id)

    data = {
        'id': session['user_id']
    }

    users = User.get_one(data)

    data = {
        'id': id
    }

    users_with_cards = Card.get_one_with_users(data)

    check_users = {

    }
    check_users_to_pass = []

    for user in users_with_cards:
        pprint(user.username)
        pprint(check_users)

        if user.username not in check_users:
            check_users_to_pass.append(user)
            check_users[user.username] = 1
        # else:
        #     check_users['username'] = user.username
        pprint(check_users_to_pass)


    # pprint(id)
    return render_template('showcard.html', data = card, users = users, users_with_cards = check_users_to_pass)

@app.route('/save_card', methods=['POST'])
def save_to_binder():
    pprint(request.form)
    if not Card.validate_save(request.form):
        return redirect(f"/card/{request.form['card_id']}")

    data = {
        'name': request.form['name'],
        'card_condition': request.form['card_condition'],
        'api_id': request.form['api_id'],
        'card_id': request.form['card_id'],
        'binder_id': request.form['binder_id']
    }

    quantity = request.form['quantity']
    pprint(quantity)
    
    if quantity == "1":
        Card.save(data)
    elif quantity == "2":
        Card.save(data)
        Card.save(data)
    elif quantity == "3":
        Card.save(data)
        Card.save(data)
        Card.save(data)
    elif quantity == "4":
        Card.save(data)
        Card.save(data)
        Card.save(data)
        Card.save(data)
    elif quantity == "5":
        Card.save(data)
        Card.save(data)
        Card.save(data)
        Card.save(data)
        Card.save(data)

    session['binder_id'] = request.form['binder_id']

    return redirect(f'/show_binder/{session["binder_id"]}')

@app.route('/delete/<id>')
def delete_card(id):
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')
    data = {
        "id": id
    }
    Card.delete(data)



    return redirect(f'/show_binder/{session["binder_id"]}')

@app.route('/calculator')
def calc():
    return render_template('calculator.html')