# project/product/views.py


#################
#### imports ####
#################

# import stripe

from flask import render_template, Blueprint, request, flash

from forms import ProductForm
from project import db
from project.models import Product


################
#### config ####
################

product_blueprint = Blueprint('product', __name__,)


################
#### routes ####
################


@product_blueprint.route('/add', methods=['GET', 'POST'])
def add_product():
    form = ProductForm(request.form)
    if form.validate_on_submit():
        product = Product(
            name=form.name.data,
            version=form.version.data,
            price=form.price.data
        )
        db.session.add(product)
        db.session.commit()
        flash('Product added!', 'success')

    return render_template('product/add.html', form=form)
