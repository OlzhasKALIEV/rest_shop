from flask import Flask, request, make_response

from products import id_product, insert_products, delete_products

app = Flask(__name__)


@app.route("/")
def root():
    return "Интернет-магазин"


@app.route('/product', methods=['GET'])
def get_product():
    return id_product()


@app.route('/insert/product', methods=["POST"])
def get_insert_product():
    insert_product = request.get_json()
    if len(insert_product) == 3:
        return insert_products(insert_product)
    else:
        return make_response("Необходимо заполнить все данные", 413)


@app.delete('/delete/product/<id>')
def delete_product(id):
    return delete_products(id)


if __name__ == "__main__":
    app.run()
