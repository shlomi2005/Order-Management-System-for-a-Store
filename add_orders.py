from shop import products

orders = []


def id_for_order():
    return len(orders) + 1


def get_order_id():
    id_of_a_product = input("enter a id of a product: ")
    return id_of_a_product


def get_order_products():
    quantity_of_products = input("enter a quantily of products: ")
    return quantity_of_products


def validation_of_id(id_of_a_product):
    if not id_of_a_product.isdigit():
        print("please enter number int: ")
        return False
    for produdk in products:
        if produdk["id"] == int(id_of_a_product):
            return True
    print("the product does not exist, please select another product: ")
    return False


def validation_of_quantity(quantity_of_products):
    if not quantity_of_products.isdigit():
        print("please enter number int: ")
        return False
    if int(quantity_of_products) <= 0:
        print("please enter number legal: ")
        return False
    return True


def total_validation_of_add_order(id_, prod):
    if validation_of_id(id_) == True and validation_of_quantity(prod) == True:
        return True
    return False


def get_price(id_):
    for produdk in products:
        if produdk["id"] == id_:
            return produdk["price"]


def add_order():
    order = {
        "id": id_for_order(),
        "items": [],
        "total": 0,
        "status": "OPEN"
    }
    while True:
        id_ = get_order_id()
        prod = get_order_products()

        if total_validation_of_add_order(id_, prod) == True:
            id_ = int(id_)
            prod = int(prod)

            order["items"].append({"product_id": id_, "quantity": prod})
            order["total"] += get_price(id_) * prod

            enter = input(
                "If you would like another product, press 1; to exit, press 2: ")
            if enter == "2":
                break

    orders.append(order)
    return order


# new_order = add_order()


def discount_percentages():
    new = add_order()

    if new["total"] >= 1500:
        new["total"] = new["total"]*0.85
    elif new["total"] >= 700:
        new["total"] = new["total"]*0.90
    elif new["total"] >= 300:
        new["total"] = new["total"]*0.95
    else:
        new["total"] = new["total"]
    return new
