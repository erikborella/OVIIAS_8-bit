from flask import Blueprint, redirect, url_for, flash
from extensions import db

from models import Product, User

import session

cart = Blueprint('cart', __name__)


@cart.route("/cart/add/<id>/<int:quant>")
def add_to_cart(id, quant):
    if not session.is_logged():
        flash("Voce precisa estar logado para fazer isso")
        return redirect(url_for('auth.login'))
    else:
        product: Product = Product.query.filter_by(
            id=id).first_or_404("Produto nao encontrado")
        user: User = User.query.filter_by(
            id=session.get()).first_or_404("Usuario invalido")

        if product.stock <= 0 or quant > product.stock:
            flash("Quantidade do produto indiponivel")
            return redirect(url_for('store.product', id=id))
        else:
            user.n_items += quant
            user.subtotal += product.price * quant

            product.stock -= quant

            db.session.commit()
            return "sim"
