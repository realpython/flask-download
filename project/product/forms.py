# project/product/forms.py


from flask_wtf import Form
from wtforms import TextField, DecimalField
from wtforms.validators import DataRequired


class ProductForm(Form):
    name = TextField('Product Name', [DataRequired()])
    version = TextField('Version', [DataRequired()])
    price = DecimalField('Price', [DataRequired()])
