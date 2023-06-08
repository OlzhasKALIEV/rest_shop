from flask import Flask, request, make_response, jsonify

from products import get_product, products

app = Flask(__name__)


@app.get("/product")
def get_product():
    return jsonify({"store_products": products})


@app.get("/product/<id>")
def get_id_product(id):
    '''/product/<id> -- <id> - подставляем номер id
    '''
    return get_product(id)


if __name__ == "__main__":
    app.run(debug=True)
