
def validate_inputs(type, message, is_number= False): 
    """
    Validate the inputs to ensure they are in the correct format
    If it's a number, set the last argument to true.
    """
    warning = ""
    while message:
        try:
            a = type(input(f"Enter {message}{warning}: "))
            if is_number:
                if a <= 0:
                    print("Enter a positive number")
                    warning = " positive"
                    continue
            return a
        except:
            print(f"Enter a valid {'number' if is_number else 'letter'}")
            warning = " again"

#name = validate_inputs(str, "name") #--> If the input is going to be a str we do not place True this is just when is a number
#age = validate_inputs(int, "age", True)
# cantidad = validate_inputs(float, "quantity", True)

def generate_final_report(orders_db: dict, product_db: dict, user_db: dict) -> tuple:
    """
    Generate the final report based on the provided dictionaries.
    """
    total_orders = len(orders_db)
    total_income = 0.0
    
    # Auxiliary dictionaries
    orders_by_customer = {} # format:  {customer_name: total_spent}
    sold_products = {}      # format: {product_name: total_qty}

    print("\n","="*30)
    print("         FINAL SALES REPORT         ")
    print("="*30)

    if not orders_db:
        print("No transactions recorded today.")
    else:
        for order_id, order_info in orders_db.items():
            # Extract IDs from the orders_db format
            u_id = order_info["key"]
            p_id = order_info["product_id"]
            qty = order_info["quantity"]

            # Get names from user_db and product_db, and unit price from product_db
            customer_name = user_db[u_id]["user_name"]
            product_name = product_db[p_id][0]
            unit_price = product_db[p_id][1]
            
            # Calculations
            subtotal = unit_price * qty
            total_income += subtotal

            # Grouping by Customer
            current_cust_total = orders_by_customer.get(customer_name, 0)
            orders_by_customer[customer_name] = current_cust_total + subtotal

            # Grouping by Product
            current_prod_qty = sold_products.get(product_name, 0)
            sold_products[product_name] = current_prod_qty + qty

            print(f"Order #{order_id}: {customer_name} bought {qty} {product_name}(s) - Subtotal: ${subtotal}")

    # --- FINAL CONSOLIDATED SUMMARY ---
    print("\n" + "-"*45)
    print(f"Total Orders: {total_orders}")
    print(f"Total Daily Income: ${total_income}")
    
    print("\nOrders Grouped by Customer:")
    for name, spent in orders_by_customer.items():
        print(f" > {name}: Total spent ${spent}")

    print("\nTotal Products Sold Today:")
    for p_name, total_qty in sold_products.items():
        print(f" > {p_name}: {total_qty} units")

    print("="*30 + "\n")

    return total_orders, total_income

