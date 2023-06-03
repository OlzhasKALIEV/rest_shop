from flask import Flask, request

from products import id_product, products, name_product, id_producta, inser_products

app = Flask(__name__)


@app.route("/")
def root():
    return "Интернет-магазин"


@app.route('/product', methods=['GET', "POST"])
def get_post_product():
    if request.method == 'GET':
        return id_product()
    if request.method == "POST":
        return "405 Method Not Allowed"


@app.route('/insert/product', methods=["GET", "POST"])
def get_insert_product():
    if request.method == 'GET':
        get_product = request.get_json()
        return get_product  # возвращает то что мы хотим добавить в магазин
    if request.method == "POST":
        insert_product = request.get_json()
        return inser_products(insert_product)


@app.get('/product/<id>')
def get_id(id):
    product = id_producta(id)
    if not product:
        return "Такого продукта нет"

    return f"Вы добавили в корзину продукт {product['name_product']}"


if __name__ == "__main__":
    app.run()
