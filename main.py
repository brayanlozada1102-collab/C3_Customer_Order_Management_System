
from customer_registration import email_validator,str_validator

def main():
    # Initial data structures (Dictionaries only)
    customers_db = {} 
    products_db = {} 
    orders_db = {} 
    
    order_counter = 1
    
    print("--- Sales Registration System ---")
    
    while True :
        print("\n1. Register Customer\n2. Register Product\n3. Create Order\n4. View Orders\n5. Final Report & Exit")
        option = input("Select an option: ")
        
        if option == "1":
            
            name = input("Enter a new customer name: ")
            name_validated = str_validator(name,"name")
            email = input("Enter a new customer email: ")
            email_validated = email_validator(email)
            new_user = create_user(name_validated, email_validated)
            customers_db = add_to_db(new_user, customers_db)
            
            print("Customer registered.")
            
        elif option == "2":
            p_id = input("Product ID: ")
            p_name = input("Product Name: ")
            price = float(input("Unit Price: "))
            products = add_product(p_id, p_name, price, products)
            print("Product registered.")
            
        elif option == "3":
            if not customers or not products:
                print("Error: Need customers and products first.")
                continue
            
            c_id = input("Customer ID: ")
            p_id = input("Product ID: ")
            qty = int(input("Quantity: "))
            
            if c_id in customers and p_id in products:
                o_id = f"ORD-{order_counter}"
                orders = create_order(o_id, c_id, p_id, qty, customers, products, orders)
                order_counter += 1
                print(f"Order {o_id} created.")
            else:
                print("Invalid Customer or Product ID.")
                
        elif option == "4":
            print("\n--- Current Orders ---")
            for oid, data in orders.items():
                c_name = customers[data[0]][0]
                p_name = products[data[1]][1]
                print(f"ID: {oid} | Client: {c_name} | Product: {p_name} | Qty: {data[2]} | Total: ${data[3]}")
                
        elif option == "5":
            count, revenue = get_formatted_report(customers, products, orders)
            print("\n============================")
            print("      FINAL DAILY REPORT     ")
            print("============================")
            print(f"Total Orders: {count}")
            print(f"Total Income: ${revenue}")
            print("============================")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
