# PRODUCTS: dictionary with (name, price)
products = {
    1: ("apple", 3000),
    2: ("pear", 2000),
    3: ("orange", 4000)
}

# USERS: basic user database
user_db = { 
    1: {"user_id": 1, "user_name": "pepe"}, 
    2: {"user_id": 2, "user_name": "Andres"} 
}

def sell_product(products, user_db):

    # ===== USER VALIDATION =====
    # Ask for user ID and repeat until it exists
    user_id = int(input("Enter user ID: "))

    while user_id not in user_db:
        print("User does not exist")
        user_id = int(input("Enter a valid ID: "))

    # Get user name and welcome message
    user_name = user_db[user_id]["user_name"]
    
    print("-------------------------------")
    print("Welcome", user_name)
    print("-------------------------------")


    # ===== INITIALIZE TOTAL =====
    # Variable to accumulate all purchases
    total = 0  

    # Control variable to continue buying
    continue_buying = "si"


    # ===== MAIN LOOP (SHOPPING PROCESS) =====
    # Loop runs until user types "no"
    while continue_buying != "no":

        # ----- SHOW PRODUCTS -----
        print("Available products:")
        for product_id in products:
            print(product_id, products[product_id][0], products[product_id][1])

        # ----- SELECT PRODUCT -----
        # Ask for product ID and validate it
        product_id = int(input("Enter product ID: "))

        while product_id not in products:
            print("Product does not exist")
            product_id = int(input("Enter a valid ID: "))

        # ----- ASK QUANTITY -----
        quantity = int(input("Quantity: "))

        # ----- CALCULATE SUBTOTAL -----
        price = products[product_id][1]
        subtotal = price * quantity
        print("Subtotal:", subtotal)

        # ----- ADD TO TOTAL -----
        total += subtotal 

        # ----- ASK TO CONTINUE -----
        continue_buying = input("Do you want to add another product? (si/no): ").lower()


    # ===== FINAL TOTAL =====
    print("Total to pay:", total)

    return total


# ===== FUNCTION CALL =====
sell_product(products, user_db)
