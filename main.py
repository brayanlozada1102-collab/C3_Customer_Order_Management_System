
from customer_registration import email_validator,str_validator,create_user,add_to_db
from products_register import register_product, number_validator
from order_creation import check_user_and_key, sell_product
from consult_order import check_orders
from dailyincome import show_daily_sales_total
from final_report_generation import generate_final_report, validate_inputs

def main():
    # Initial data structures (Dictionaries only)
    customers_db = {} 
    products_db = {
        1:('coffe',1500),
        2:('azucar',2000)
    } 
    orders_db = {} 
    order_id = 0
    
    print("--- Sales Registration System ---")
    start = True
    while start :
        print("\n1. Register Customer\n2. Register Product\n3. Create Order\n4. View Orders\n5. Daily Income\n6. Final Report & Exit")
        option = input("Select an option: ")
        
        if option == "1":
            
            name_validated = validate_inputs(str, "name")
            email = input("Enter a new customer email: ")
            email_validated = email_validator(email)
            new_user = create_user(name_validated, email_validated)
            customers_db = add_to_db(new_user, customers_db)
            
            print("Customer registered.")
            
        elif option == "2":
            
            product_name_validated = validate_inputs(str, "name product")
            price_validated = validate_inputs(float,"price",True)
            products_db = register_product(products_db, product_name_validated, price_validated)
            print("Product registered.")
            print(products_db)
            
        elif option == "3":
            if not customers_db or not products_db:
                print("Error: Need customers and products first.")
                continue
            
            orders_db, order_id = sell_product(products_db,customers_db,orders_db,order_id)
            print(">> Sale completed.")
            print(orders_db)
                
        elif option == "4":
            if not customers_db or not products_db or not orders_db:
                print("Error: Need customers, products and orders first.")
                continue
            
            print("\n--- Current Orders ---")
            print(check_orders(orders_db, customers_db, products_db))
           

           
        elif option == "5":
           if not customers_db or not products_db or not orders_db:
                print("Error: Need customers, products and orders first.")
                continue
           
           show_daily_sales_total(orders_db, products_db)
        
        elif option == "6":
            if not orders_db:
                print("No orders were placed today. Closing system...")
                start = False
            else:
                generate_final_report(orders_db, products_db, customers_db)
                start = False

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
