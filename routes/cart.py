from flask import Blueprint, redirect, url_for, flash, render_template
from extensions import db

from models import Product, User, Buy

import session

cart = Blueprint('cart', __name__)


@cart.route("/cart/add/<int:id>/<int:quant>")
def add_to_cart(id: int, quant: int):
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
            buy = Buy.query.filter_by(user_id=session.get(), product_id=id).first()

            # Check if alredy have the buy with this product
            if buy is None:
                buy = Buy(user, product, quant)
                db.session.add(buy)
            else:
                buy.n_items += quant

            user.n_items += quant
            user.subtotal += product.price * quant

            product.stock -= quant

            db.session.commit()

            flash("Produto adicionado com sucesso ao carinho")
            return redirect(url_for("store.showcase"))


@cart.route("/cart/remove/<int:id>/<int:quant>")
def remove_to_cart(id: int, quant: int):
    if not session.is_logged():
        flash("Voce precisa estar logado para fazer isso")
        return redirect(url_for('auth.login'))
    else:
        buy: Buy = Buy.query.filter_by(user_id=session.get(
        ), product_id=id).first_or_404("Voce não possui essa compra")
        
        if quant >= buy.n_items:
            quant = buy.n_items
            db.session.delete(buy)
        else:
            buy.n_items -= quant
        
        buy.user.n_items -= quant
        buy.user.subtotal -= quant * buy.product.price
        buy.product.stock += quant

        db.session.commit()
        
        flash("Produto removido do seu carinho")
        return redirect(url_for('store.showcase'))

            