
from customer_registration import email_validator,str_validator,create_user,add_to_db
from products_register import register_product, number_validator

def main():
    # Initial data structures (Dictionaries only)
    customers_db = {} 
    products_db = {
        1:('coffe',1500),
        2:('azucar',2000)
    } 
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
            
            product_name = input("Product Name: ")
            product_name_validated = str_validator(product_name,"product name")
            price = input("Unit Price: ")
            price_validated = number_validator(price,float)
            products_db = register_product(products_db, product_name_validated, price_validated)
            print("Product registered.")
            print(products_db)
            
        elif option == "3":
            if not customers_db or not products_db:
                print("Error: Need customers and products first.")
                continue
            
            customer_id = int(input("Customer ID: "))
            product_id = int(input("Product ID: "))
            quantity = int(input("Quantity: "))
            
            if customer_id in customers_db and product_id in products_db:
                print(customer_id)
                print(product_id)
                
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
