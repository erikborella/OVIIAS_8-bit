from Control import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Float(3), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.String(1000))

    def __init__(self, name: str, description: str, price: float, stock: int, image_path: str):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.image_path = image_path

    def __repr__(self):
        return "<Product %r>" % self.name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # personal information columns
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    email = db.Column(db.String(1000), nullable=False)
    # cart columns
    n_items = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Float(3), nullable=False)

    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = password
        self.email = email

        self.n_items = 0
        self.subtotal = 0

    def __repr__(self):
        return "<User %r>" % self.username


class Buy(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('users', lazy=True))

    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False)
    product = db.relationship(
        'Product', backref=db.backref('products', lazy=True))

    def __init__(self, user, product):
        self.user = user
        self.product = product

    def __repr__(self):
        return "<Buy %r:%r>" % (user, product)
