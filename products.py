import json

from flask import make_response, jsonify

products = [
    dict(
        id=1,
        name_product="Телефон",
        product_price='10000'
    ),
    dict(
        id=2,
        name_product="Ноутбук",
        product_price='50000'
    )
]


def get_product(id):
    for inproduct_information in products:
        if inproduct_information.get("id") == int(id):
            return jsonify(
                {
                    "name_product": inproduct_information["name_product"],
                    "product_price": inproduct_information["product_price"]
                }
            )
    return make_response("Данного продукта нет", 400)
