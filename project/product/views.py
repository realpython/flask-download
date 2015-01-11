# project/product/views.py


#################
#### imports ####
#################

import stripe

from flask import render_template, Blueprint, \
    request, abort, send_from_directory

from project import app, db
from project.models import Purchase


################
#### config ####
################

product_blueprint = Blueprint('product', __name__,)


################
#### routes ####
################


@product_blueprint.route('/purchase', methods=['POST'])
def purchase():
    product_price = app.config['PRODUCT_AMOUNT']
    product_currency = app.config['PRODUCT_CURRENCY']
    stripe_token = request.form['stripeToken']
    print stripe_token
    email = request.form['stripeEmail']

    try:
        stripe.Charge.create(
            amount=product_price,
            currency=product_currency,
            card=stripe_token,
            description=email)
    except stripe.CardError:
        return render_template('product/charge_error.html')

    purchase = Purchase(email=email)
    db.session.add(purchase)
    db.session.commit()

    return render_template('product/success.html', url=str(purchase.id))


@product_blueprint.route('/<purchase_id>')
def download(purchase_id):
    purchase = Purchase.query.filter_by(id=purchase_id).first()
    if purchase:
        purchase.downloads_left -= 1
        if purchase.downloads_left < 1:
            db.session.commit()
            return render_template('product/exceeded.html')
        db.session.commit()
        return send_from_directory(
            directory=app.static_folder,
            filename='foo.bar',
            as_attachment=True
        )
    else:
        abort(404)
