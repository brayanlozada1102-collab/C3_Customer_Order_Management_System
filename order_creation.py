# productos falsos (diccionario con tuplas)
productos = {
    1: ("manzana", 3000),
    2: ("pera", 2000)
}

user_db = {
    1: {
        "user_id": 1,
        "user_name": "pepe",
        "user_email": "pepe@gmail.com" 
    },

    2: {
        "user_id": 2,
        "user_name": "Andres",
        "user_email": "andres@gmail.com" 
    }
}


def vender_producto(product_id):
#Función reutilizable: recibe el id del producto, pide la cantidad y calcula el total

    while user_id == True:
        user_id = int(input("ingresa id del cliente: "))

        if user_id not in user_db:
            print("El usuario no existe")
            return
        
    if product_id not in productos:
        print("Producto no existe")
        return

    cantidad = int(input("Ingrese la cantidad a vender: "))
    precio = productos[product_id][1]
    total = precio * cantidad
    print("Total a pagar:", total)
    return total


# ===== PRUEBA =====

vender_producto(1)