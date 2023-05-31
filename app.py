from flask import Flask, request

from products import id_product, products, name_product, id_producta

app = Flask(__name__)


@app.route("/")
def root():
    return "Интернет-магазин"


@app.route('/product', methods=['GET', 'POST'])
def get_post_product():
    if request.method == 'GET':
        return id_product()
    else:
        '''{"id":"4", "name_product" : "Наушники", 
        "product_price":"20000"}
        '''
        request_data = request.get_json()
        products.append(request_data)
        return "Товар добавлен в магазин"


@app.get('/product/<id>')
def get_id(id):
    product = id_producta(id)
    if not product:
        return "Такого продукта нет"

    return f"Вы добавили в корзину продукт {product['name_product']}"


if __name__ == "__main__":
    app.run()
