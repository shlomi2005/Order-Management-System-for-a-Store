# from shop import products, order


# # def id_for_order():
# #     idg = idg+1
# #     return idg


# # def add_order():
# #     if total_validation_of_add_order(id_, prod) == True:
# #         for produc in products:
# #             order = {
# #                 "id": gg,
# #                 "items": [{"product_id": id_, "quantity": prod},
# #                           {"product_id": 3, "quantity": 1}],
# #                 "total": 1026.0,
# #                 "status": "OPEN"
# #             }

# #     print(order)


# # {
# #     "id": 1,
# #     "items": [{"product_id": 1, "quantity": 2},
# #               {"product_id": 3, "quantity": 1}],
# #     "total": 1026.0,
# #     "status": "OPEN"
# # }


# # def get_order_id():
# #     id_of_a_product = int(input("enter a id of a product: "))
# #     return int(id_of_a_product)


# # def get_order_products():
# #     quantity_of_products = int(input("enter a quantily of products: "))
# #     return int(quantity_of_products)


# # def total_validation_of_add_order(id_, prod):
# #     if validation_of_id(id_) == True and validation_of_quantity(prod) == True:
# #         return True
# #     return False


# # def validation_of_id(id_of_a_product):
# #     for produdk in products:
# #         if produdk["id"] != id_of_a_product:
# #             print("the product does not exist, please select another product: ")
# #         return False
# #     return True


# # def validation_of_quantity(quantity_of_products):
# #     if quantity_of_products < 0:
# #         print("please enter number legal: ")
# #     if type(quantity_of_products) != int:
# #         print("please enter number int: ")
# #         return False
# #     return True


# # gg = id_for_order()
# # id_ = get_order_id()
# # prod = get_order_products()

# # # add_order()

# # ===================================================================


# def get_order_products_id():
#     price = 0
#     while True:
#         id_of_ = int(input("enter a id of a product: "))
#         quantity_of_ = int(input("enter a quantily of products: "))
#         for produc in products:
#             if produc["id"] == id_of_:
#                 price += produc["price"]*quantity_of_
#                 order.append("items"["product_id"], id_of_,
#                              "items"["quantity", quantity_of_])

#         enter = input(
#             int("If you would like another product, press 1; to exit, press 2: "))
#         if enter == 2:
#             break
#     return price


# get_order_products_id()
