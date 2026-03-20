user_db = {
    1: {
        "user_name": "pepe",
        "user_email": "pepe@gmail.com"
        },
    2: {
        "user_name": "Andres",
        "user_email": "andres@gmail.com" 
        }
    }


## tabla en la pared de los precios 
product_db = {
    1: ("manzana", 3000),
    2: ("pera", 2000)
}


## cuaderno de ordenes de los usuarios incluye producto y quien lo pidio
orders_db = {1: {"user_id": 1, "product_id": 1, "quantity": 3}, 
             2: {"user_id": 1, "product_id": 2, "quantity": 5}}



##DAILY INCOME CALCULATION

def show_daily_sales_total(orders_db, product_db):

    total_day = 0

    print("\n--- DAILY SALES REPORT ---")


    
    for order_id, data in orders_db.items():

        product_name, unit_price = product_db[data["product_id"]]
        

        quantity = data["quantity"]

        subtotal = unit_price * quantity
        

        total_day += subtotal
        
        print(f"Order #{order_id}: {product_name} x{quantity} = ${subtotal}")

    print("-" * 30)
    print(f"INGRESO TOTAL: ${total_day}")
    print("-" * 30 + "\n")

show_daily_sales_total(orders_db, product_db)