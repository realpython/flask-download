# project/helpers.py


from project.models import Product


def get_products():
    products = Product.query.filter_by(is_active=True).all()
    return products
