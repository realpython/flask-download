# project/main/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint

from project.helpers import get_products


################
#### config ####
################

main_blueprint = Blueprint('main', __name__,)


################
#### routes ####
################


@main_blueprint.route('/')
def home():
    products = get_products()
    return render_template('main/home.html', products=products)
