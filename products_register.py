


def number_validator(number,type):
    try: 
        type(number)
    except ValueError:
        print("Invalid number!")
        number = input("Enter a valid number: ")
        return number_validator(number)
    return number

#A funtion to allow the user to add a new tuple in the dictionary, assing it the ID
def register_product(products: dict, name: str, price: float) -> dict:
    product_id = len(products) + 1
    product = (name, price)
    products[product_id] = product
    return products

##ask the client for the user for thebinformation of the new product
# name = input("enter the product name: ")
# price = float(input("enter the product price: "))
## we call the funtion and we save the result that it returns
# products = register_product(products,name, price )
# print(products)

 
