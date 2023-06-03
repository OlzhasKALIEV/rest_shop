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
            return f'Ошибка {400}: продукт с id {insert_product["id"]} уже существует'
    if count == 0:
        products.append(insert_product)
    return f'{200}: Продукт успешно добавлен'


def delete_products(id):
    id = int(id)
    for i in products:
        if id == i["id"]:
            products.remove(i)
            return f'Ответ {200}: продукт {i} был успешно удален'
        else:
            return f'Ответ {409}: данного продукта не существует'

