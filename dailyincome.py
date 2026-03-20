
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

