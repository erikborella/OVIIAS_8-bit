from flask import Blueprint, redirect, url_for, flash, request
from extensions import db
from models import Product, User, Buy

import session

cart = Blueprint('cart', __name__)


@cart.route('/cart/add', methods=['POST'])
def add_to_cart():
    if not session.is_logged():
        flash("Voce precisa estar logado para fazer isso")
        return redirect(url_for('auth.login'))
    else:
        product_id = int(request.form['product_id'])
        quant = int(request.form['quant'])

        if not product_id or not quant:
            flash("Informações faltantes")
            return redirect(url_for('store.index'))
        else:
            product: Product = Product.query.filter_by(
                id=product_id).first_or_404("Produto não encontrado")
            user: User = User.query.filter_by(
                id=session.get()).first_or_404("Usuario invalido")

            if product.stock <= 0 or quant > product.stock:
                flash("Quantidade do produto indisponivel")
                return redirect(url_for('store.product', id=product_id))
            else:
                buy: Buy = Buy.query.filter_by(
                    user_id=session.get(), product_id=product_id).first()

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

                flash("Produto adicionado com sucesso ao seu carinho")
                return redirect(url_for('store.showcase'))


@cart.route('/cart/remove', methods=['POST'])
def remove_to_cart():
    if not session.is_logged():
        flash("Voce precisa estar logado para fazer isso")
        return redirect(url_for('auth.login'))
    else:
        product_id = int(request.form['product_id'])
        quant = int(request.form['quant'])

        if not product_id or not quant:
            flash("Informações faltantes")
            return redirect(url_for('store.index'))
        else:
            buy: Buy = Buy.query.filter_by(user_id=session.get(
            ), product_id=product_id).first_or_404("Voce nao possui essa compra")

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
