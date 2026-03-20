# PRODUCTS: dictionary with (name, price)
#products = {
 #   1: ("apple", 3000),
  #  2: ("pear", 2000),
  #  3: ("orange", 4000)
#}

# USERS: basic user database
#user_db = {
 #   1: {
  #      "user_name": "pepe",
   #     "user_email": "pepe@gmail.com"
    #    },
   # 2: {
   #     "user_name": "Andres",
    #    "user_email": "andres@gmail.com" 
     #   }
    #}



def check_user_and_key(user_db):
    for key, value in user_db.items():
        print(f"the id is {key} and the user is: {value['user_name']}")

def sell_product(products, user_db,orders_db,order_id):

    print("Available users:")
    print("---------------------------------")
    check_user_and_key(user_db)
    print("---------------------------------")
    
    key = int(input("Enter user ID: "))

    while key not in user_db:
        print("User does not exist")
        key = int(input("Enter a valid ID: "))

    user_name = user_db[key]["user_name"]
    print("====================================")
    print("Welcome", user_name)
    print("====================================")

    total = 0
    op = "si"

    while op != "no":
        print("-----------------------------------------")
        print("Available products:")
        for product_id, data in products.items():
            print(product_id, data[0], data[1])
        print("-----------------------------------------")

        product_id = int(input("Enter product ID: "))

        while product_id not in products:
            print("Product does not exist")
            product_id = int(input("Enter a valid ID: "))

        quantity = int(input("Quantity: "))

        price = products[product_id][1]
        subtotal = price * quantity

        print("Subtotal:", subtotal)

        total += subtotal

        order_id += 1
        orders_db[order_id] = {
            "key": key,
            "product_id": product_id,
            "quantity": quantity
        }

        op = input("Do you want to add another product? (si/no): ").lower()

    print("------------ summary --------------")

    for order_id, order in orders_db.items():
        print(f"order: {order_id} | user id: {order['key']} | product id: {order['product_id']} | quantity: {order['quantity']}")

    print("=======================")
    print("Total to pay:", total)
    print("=======================")

    return orders_db

# ===== FUNCTION CALL =====
#sell_product(products, user_db)
