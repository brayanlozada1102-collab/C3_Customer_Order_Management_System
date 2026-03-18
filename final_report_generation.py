import pandas as pd
false_user_db = {
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

false_product_db = {
    1: (1, "manzana", 3000),
    2: (2, "pera", 2000),
}

customers_db = {
    
} 
products_db = {
    
} 
orders_db = {} 
total_ingresos_dia = 0.0
conteo_pedidos_totales = 0

#Total number of orders registered
def show_register_orders():
    df = pd.DataFrame()
#Total revenue generated
datos = {'a': 1, 'b': 2}
for clave, valor in datos:
    print(f"Clave: {clave}, Valor: {valor}")

#orders grouped by customer

#Products sold during the day