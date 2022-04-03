from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.friend import Friend


from pprint import pprint

@app.route('/send_request', methods=['POST'])
def send_request():
    pprint(request.form)

    Friend.save(request.form)
    return redirect('/')

@app.route('/respond_request', methods=['POST'])
def respond_request():
    pprint(request.form)
    Friend.update(request.form)
    return redirect('/profile')

@app.route('/delete_request/<id>')
def delete_request(id):
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')
    data = {
        "id": id
    }
    Friend.delete(data)
    return redirect('/profile')