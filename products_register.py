products={
        1:('coffe',1500),
        2:('azucar',2000)
    }


def register_product(products, name, price):
    product_id = len(products) + 1
    product = (name, price)
    products[product_id] = product
    return products

 
name = input("enter the product name: ")
price = float(input("enter the product price: "))
products = register_product(products,name, price )
print(products)


