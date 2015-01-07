# project/user/views.py


#################
#### imports ####
#################

import stripe

from flask import render_template, Blueprint, url_for, \
    redirect, flash, request
from flask.ext.login import login_user, logout_user, \
    login_required

from project import app, bcrypt, stripe_keys
from project.models import User, Purchase
from project.user.forms import LoginForm

################
#### config ####
################

stripe.api_key = stripe_keys['stripe_secret_key']

user_blueprint = Blueprint('user', __name__,)


################
#### routes ####
################

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(
                user.password, request.form['password']):
            login_user(user)
            flash('You are logged in. Welcome!', 'success')
            return redirect(url_for('user.admin'))
        else:
            flash('Invalid email and/or password.', 'danger')
            return render_template('user/login.html', form=form)
    return render_template('user/login.html', form=form)


@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out. Bye!', 'success')
    return redirect(url_for('main.home'))


@user_blueprint.route('/admin')
@login_required
def admin():
    purchases = Purchase.query.all()
    total_sales = len(purchases) * (int(app.config['PRODUCT_AMOUNT']) / 100)
    return render_template('user/admin.html', total_sales=total_sales)
