products = [
    dict(
        id="1",
        name_product="Телефон",
        product_price='10 000'
    ),
    dict(
        id="2",
        name_product="Мышка",
        product_price='500'
    ),
    dict(
        id="3",
        name_product="Телевизор",
        product_price='40 000'
    ),
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
