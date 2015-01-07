# project/main/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint  # pragma: no cover


################
#### config ####
################

main_blueprint = Blueprint('main', __name__,)  # pragma: no cover


################
#### routes ####
################


@main_blueprint.route('/')  # pragma: no cover
def home():
    return render_template('main/home.html')
