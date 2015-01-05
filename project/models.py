# project/models.py


import datetime

from project import db, bcrypt


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return 'email {0}'.format(self.email)


class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    file_name = db.Column(db.String, nullable=False)
    version = db.Column(db.String, nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, version, price):
        self.name = name
        self.file_name = name + '_' + version
        self.version = version
        self.price = price

    def __repr__(self):
        return '{0} (v{1})'.format(self.name, self.version)


class Purchase(db.Model):

    __tablename__ = 'purchases'

    unique_id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    downloads_left = db.Column(db.Integer, default=5)
    sold_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, unique_id, email):
        self.unique_id = unique_id
        self.email = email

    def __repr__(self):
        return '{0} bought by {1}'.format(self.product.name, self.email)
