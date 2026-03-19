user_db = {
    1: {
        "user_name": "pepe",
        "user_email": "pepe@gmail.com"
        },
    2: {
        "user_name": "Andres",
        "user_email": "andres@gmail.com" 
        }
    }


## tabla en la pared de los precios 
false_product_db = {
    1: ("manzana", 3000),
    2: ("pera", 2000)
}


## cuaderno de ordenes de los usuarios incluye producto y quien lo pidio
orders_db = {1: {"user_id": 1, "product_id": 1, "quantity": 3}, 
             2: {"user_id": 1, "product_id": 2, "quantity": 5}}



##DAILY INCOME CALCULATION

def mostrar_total_ventas_diarias():

    total_dia = 0

    print("\n--- REPORTE DE VENTAS DEL DÍA ---")


    
    for order_id, datos in orders_db.items():

        producto_nombre, precio_unitario = false_product_db[datos["product_id"]]
        

        cantidad = datos["quantity"]

        subtotal = precio_unitario * cantidad
        

        total_dia += subtotal
        
        print(f"Orden #{order_id}: {producto_nombre} x{cantidad} = ${subtotal}")

    print("-" * 30)
    print(f"INGRESO TOTAL: ${total_dia}")
    print("-" * 30 + "\n")

mostrar_total_ventas_diarias()