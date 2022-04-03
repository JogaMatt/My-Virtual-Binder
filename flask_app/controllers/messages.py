from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.message import Message


from pprint import pprint

@app.route('/send_message', methods=['POST'])
def send_message():
    pprint(request.form)
    Message.save(request.form)
    return redirect('/')

@app.route('/delete_message/<id>')
def delete_message(id):
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')
    data = {
        "id": id
    }
    Message.delete(data)
    return redirect('/profile')