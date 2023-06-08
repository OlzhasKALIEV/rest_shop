from flask import Flask, request, make_response

from products import delete_products, get_product

app = Flask(__name__)


@app.route("/")
def root():
    return "Интернет-магазин"


@app.get("/product/<id>")
def get_id_product(id):
    '''/product/<id> -- <id> - подставляем номер id
    '''
    return get_product(id)


@app.delete('/delete')
def delete_product(id):
    return delete_products(id)


if __name__ == "__main__":
    app.run(debug=True)
