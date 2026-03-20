
from customer_registration import email_validator, create_user,add_to_db
from products_register import register_product
from order_creation import sell_product
from consult_order import check_orders
from dailyincome import show_daily_sales_total
from final_report_generation import generate_final_report, validate_inputs

#This is the user database, it is a dict of dicts, in which the key is a number represent the customer ID.
customers_db = {
    1: {
         "user_name": "pepe",
         "user_email": "pepe@gmail.com"
         }
} 

#This is the products database, it is a dict of tuples, in which the key is a number represent the product ID.
#In the tuple the position 0 is the product name and the 1 is the product price.
products_db = {
    1:('coffe',1500),
    2:('azucar',2000)
} 

#This is the order database, it is a dict of dicts, in which the key is a number represent the order ID.
#In addition this is going to be filled by the customer ID, product ID and quantity, so we can allocate the customer and product based on it. 
orders_db = {} 
order_id = 0

#This is the main in it there are all of the functions working together.
def main(customers_db, products_db, orders_db, order_id):
    
    #This is the introduction message
    print("--- Sales Registration System ---")

    #We run the program In a while loop, so the program only stop when we decide.  
    start = True
    while start :
        #This is the options menu.
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
            
        elif option == "3":
            if not customers_db or not products_db:
                print("Error: Need customers and products first.")
                continue
            
            orders_db, order_id = sell_product(products_db,customers_db,orders_db,order_id)
            print(">> Sale completed.")
                
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
    main(customers_db, products_db, orders_db, order_id)
