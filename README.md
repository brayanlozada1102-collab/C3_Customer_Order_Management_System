# 📦 Sistema de Gestión de Pedidos - Python Challenge

## 📝 Descripción del Proyecto
Este sistema automatiza el registro y procesamiento de pedidos para una empresa distribuidora que actualmente opera de forma manual. El objetivo es centralizar la información de clientes, productos y ventas para calcular totales automáticamente y generar reportes de ingresos diarios.

El proyecto está diseñado bajo un modelo colaborativo, donde cada integrante del equipo desarrolla un módulo específico que se integra en un flujo de trabajo unificado.

## 🏗️ Arquitectura y Estructuras de Datos
De acuerdo con las *restricciones técnicas* obligatorias del desafío, el sistema utiliza exclusivamente *Diccionarios* y *Tuplas*. El uso de listas ([], .append()) está estrictamente prohibido.

### Variables Generales y Estructuras Compartidas
Para asegurar la conexión entre los diferentes módulos y las ramas (branches) de los desarrolladores, se han definido las siguientes estructuras globales:

```python
# =================================================================
# ESTRUCTURAS DE DATOS GLOBALES (COMPARTIDAS)
# =================================================================

# 1. Base de Datos de Clientes (Dictionary)
# Estructura: { id_cliente: (nombre, correo) }
# Justificación: Búsqueda rápida por ID y datos inmutables en tupla.
customers_db = {} 

# 2. Catálogo de Productos (Dictionary de Tuplas)
# Estructura: { id_producto: (nombre_producto, precio_unitario) }
# Justificación: Evita cambios accidentales en precios o nombres.
products_db = {} 

# 3. Registro de Pedidos (Nested Dictionaries)
# Estructura: { id_pedido: {"cliente_id": id, "producto_id": id, "cantidad": int, "total": float} }
# Justificación: Permite almacenar múltiples atributos por transacción sin usar listas.
orders_db = {} 

# 4. Métricas de Control de la Jornada
# Estas variables deben ser actualizadas por el módulo de ventas y leídas por el de reportes.
total_ingresos_dia = 0.0
conteo_pedidos_totales = 0

## 🛠️ Organización del Código y Funciones

El programa se divide en 6 funcionalidades clave. Cada función debe recibir parámetros, procesar la información y retornar los resultados:

1. *Registro de Clientes:* Captura y valida ID, nombre y correo electrónico.
2. *Registro de Productos:* Gestiona el catálogo de productos disponibles.
3. *Creación de Pedidos:* Relaciona un cliente con un producto y calcula el subtotal.
4. *Consulta de Pedidos:* Permite buscar y mostrar el historial de ventas.
5. *Cálculo de Ingresos:* Procesa el total recaudado de todos los pedidos del día.
6. *Generación de Reporte Final:* Muestra un resumen detallado para la administración.

## 📋 Reglas de Sustentación y Evaluación

El equipo comienza con *100 puntos*. El éxito depende de la claridad y el dominio técnico:

* *Sin Listas:* El uso de cualquier estructura de lista ([]) anula los criterios de evaluación de datos.
* *Modularización:* Cada funcionalidad debe estar aislada y ser llamada desde el flujo principal.
* *Penalización por Ayuda:* Si un compañero debe intervenir para ayudar al sustentador, se restan *10 puntos*.
* *Preguntas Técnicas:* Cada respuesta incorrecta sobre la lógica o algoritmos resta *20 puntos*.
* *Idioma:* Aunque este manual es de apoyo interno, el código final y los comentarios en GitHub deben estar en *inglés*.

## 🚀 Instrucciones para el Equipo

* *Git Flow:* Trabajen en ramas separadas por funcionalidad y realicen el merge a la rama principal una vez probada la función.
* *Validación:* Asegúrense de que cada función retorne el diccionario o tupla actualizada.
* *Comentarios:* Documenten cada bloque de código explicando su propósito (en inglés).
*
