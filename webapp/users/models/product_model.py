from users.models.db import db

class Products(db.Model):
    code = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), unique=True, nullable=False)
    amount = db.Column(db.String(100), unique=True, nullable=False)
    bag = db.Column(db.String(100), nullable=False)

    def __init__(self, product, price, amount, bag):
        self.product = product
        self.price = price
        self.amount = amount
        self.bag = bag
