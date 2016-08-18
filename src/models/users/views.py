from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

import src.models.users.errors as UserErrors
from src.models.users.user import User

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/login', methods=['GET','POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['hashed']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return redirect(url_for('.user_alerts'))
        except UserErrors.UserError as e:
            return e.message
    else:
        return render_template('users/login.jinja2')

@user_blueprint.route('/register', methods=['POST', 'GET'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['hashed']

        try:
            if User.register_user(email, password):
                session['email'] = email
                return redirect(url_for('.user_alerts'))
        except UserErrors.UserError as e:
            return e.message
    else:
        return render_template('users/register.jinja2')

@user_blueprint.route('/alerts')
def user_alerts():
    return 'This is the alerts page.'


@user_blueprint.route('/logout')
def logout_user():
    session['email'] = None
    return redirect(url_for('.home'))

@user_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts(user_id):
    pass



