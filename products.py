from flask import make_response

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


def id_product():
    return products


def name_product():
    prod = list()
    for i in range(len(products)):
        for j, y in products[i].items():
            if j == 'name_product':
                prod.append(y)
    return prod


def id_producta(id):
    for p in products:
        if p.get("id") == id:
            return p

    return None


def insert_products(insert_product):
    count = 0
    for value in products:
        if insert_product["id"] == value["id"]:
            count += 1
            return make_response(f'Продукт с {insert_product["id"]} уже существует', 409)
    if count == 0:
        products.append(insert_product)
    return make_response("Продукт успешно добавлен", 200)


def delete_products(id):
    if id.isdigit() == True:
        for i in products:
            if id == str(i["id"]):
                products.remove(i)
                return make_response("Продукт удален", 200)
    else:
        return make_response("Необходимо ввести целое число", 400)
