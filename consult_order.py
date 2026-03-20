# user_db = {
#     1: {
#         "user_name": "pepe",
#         "user_email": "pepe@gmail.com"
#         },
#     2: {
#         "user_name": "Andres",
#         "user_email": "andres@gmail.com" 
#         }
#     }



# product_db = {
#     1: ("manzana", 3000),
#     2: ("pera", 2000)
# }

# orders_db = {1: {"user_id": 1, "product_id": 1, "quantity": 3}, 
#              2: {"user_id": 1, "product_id": 2, "quantity": 5}
#              }


def check_orders(orders_db, user_db, product_db):
    results = ""
    for order_id, order in orders_db.items():
        user = user_db[order["key"]]
        product = product_db[order["product_id"]]
        
        user_name = user["user_name"]
        product_name = product[0]
        product_quantity = order["quantity"]
        
        results += f"""
    purchase id: {order_id}
    user: {user_name} make an order of:
    product name: {product_name} 
    quantity: {product_quantity}

    """
    
    return results

# print(check_orders(orders_db, user_db, product_db))
