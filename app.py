from flask import Flask, request

from products import id_product, insert_products, delete_products

app = Flask(__name__)


@app.route("/")
def root():
    return "Интернет-магазин"


@app.route('/product', methods=['GET', "POST"])
def get_post_product():
    if request.method == 'GET':
        return id_product()
    if request.method == "POST":
        return f"Ошибка {405}: Method Not Allowed"


@app.route('/insert/product', methods=["GET", "POST"])
def get_insert_product():
    if request.method == 'GET':
        get_product = request.get_json()
        return get_product  # возвращает то что мы хотим добавить в магазин
    if request.method == "POST":
        insert_product = request.get_json()
        return insert_products(insert_product)


@app.delete('/delete/product/<id>')
def delete_product(id):
    return delete_products(id)


if __name__ == "__main__":
    app.run()
