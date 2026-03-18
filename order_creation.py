# productos falsos (diccionario con tuplas)
productos = {
    1: ( "manzana", 3000),
    2: ("pera", 2000)
}


def vender_producto(product_id):
#Función reutilizable: recibe el id del producto, pide la cantidad y calcula el total
    
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