from flask import Flask, request, make_response, jsonify
from jsonschema.validators import validate
from jsonschema.exceptions import ValidationError

from products import get_product, products, insert_product

app = Flask(__name__)


@app.get("/product")
def get_products():
    return jsonify({"store_products": products})


@app.get("/product/<id>")
def get_id_product(id):
    '''/product/<id> -- <id> - подставляем номер id
    '''
    return get_product(id)


@app.post("/product/v1/insert")
def post_insert_product():
    '''{"name_product": "Монитор", "product_price": 5000}
    '''
    jsonproduct = request.get_json()
    schema = {"type": "object",
              "minProperties": 2,
              "maxProperties": 2,
              "properties": {
                  "name_product": {"type": "string"},
                  "product_price": {"type": "number"}
              }, "required": ["name_product", "product_price"]
              }

    try:
        validate(instance=jsonproduct, schema=schema)
    except ValidationError as err:
        return {
            "errors": err.message
        }, 400

    return insert_product(jsonproduct)


if __name__ == "__main__":
    app.run(debug=True)
