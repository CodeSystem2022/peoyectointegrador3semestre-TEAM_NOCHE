#BRUNO MARCHETTI
from pedido import Pedido, Quesadillas, Tacos, Tamales, Botanas, Burritos, Margarita, Gaseosa, Cerveza, Tequila, Agua
from menu import Menu
import psycopg2

# Función para generar y mostrar el logotipo del menu
def logo():
    import time
    time.sleep(0.1)
    print("---------------------------------------------------------------------------------------------------------------------------")
    time.sleep(0.1)
    print("---------------------------------------------------------------------------------------------------------------------------")
    time.sleep(0.1)
    print("    Bienvenidos a ")
    time.sleep(0.1)
    print("---------------------------------------------------------------------------------------------------------------------------")
    time.sleep(0.1)
    print("---------------------------------------------------------------------------------------------------------------------------")
    time.sleep(0.1)
    print("         __   __   __   _  _   __   _           ")
    time.sleep(0.1)
    print("        |  __| |  _  | |  _  | |  \| | |  _  | | |          ")
    time.sleep(0.1)
    print("        | |    | || | | ||| | |\\ | | || | | |         ")
    time.sleep(0.1)
    print("        | |_  |  _  | |  _ \  | | \ | |  _  | | |__      ")
    time.sleep(0.1)
    print("        |____| |_| |_| |_| |_| |_| |_| |_| |_| |_____|         by TEAM NOCHE")
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
    print("---------------------------------------------------------------------------------------------------------------------------")
    time.sleep(0.1)
    print("---------------------------------------------------------------------------------------------------------------------------")
    time.sleep(0.1)
    print("                              Restaurante de comida mexicana.")
    print("")

#codigo agregado por la alumna ANALIA ALVARENGA(Luna)
#Función para crear la tabla en la base de datos
def crear_tabla():      
#Establecer la conexión con la base de datos PostgreSQL

    conexion = psycopg2.connect(
        user='postgres',
        password='admin',
        host='127.0.0.1',
        port='5432',
        database='menu'
    )

    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100),
            total FLOAT
        )
    ''')
    conexion.commit()

    #Cerrar la conexión con la base de datos
    conexion.close()



#Código incorporado por MARLENE SORIANO

# Agregar comidas al menú
menu.agregar_comida(Quesadillas())
menu.agregar_comida(Tacos())
menu.agregar_comida(Tamales())
menu.agregar_comida(Burritos())
menu.agregar_comida(Botanas())




#Código agregado por Maria del carmen Gonzalez (Maru)
# Función para verificar si una opción es válida
def es_opcion_valida(opcion, max_opcion):
    try:
        opcion_num = int(opcion)
        return opcion_num >= 1 and opcion_num <= max_opcion
    except ValueError:
        return False



# Alumno Ezequiel Soria
# Damos la opción de elegir comidas, bebidas o ir a pagar

while True:
    print("Seleccione una opción:")
    print("1 - Comida")
    print("2 - Bebidas")
    print("3 - Pagar")
    opcion = input("Opción: ")

    if es_opcion_valida(opcion, 3):
        if opcion == "1":
            # Mostrar menú de comidas y procesar elección
            menu.mostrar_comidas()
            eleccion_comida = input("Elige una comida por su número: ")

            if es_opcion_valida(eleccion_comida, menu.obtener_cantidad_comidas()):
                comida_seleccionada = menu.obtener_comida(int(eleccion_comida))
                pedido.agregar_item(comida_seleccionada)
                subtotal += comida_seleccionada.precio
                print(f"Has elegido: {comida_seleccionada.nombre}")
                print("")
            else:
                print("Opción inválida. Por favor, elige una opción válida.")
                print("")

        elif opcion == "2":
            # Mostrar menú de bebidas y procesar elección
            menu.mostrar_bebidas()
            eleccion_bebida = input("Elige una bebida por su número: ")

            if es_opcion_valida(eleccion_bebida, menu.obtener_cantidad_bebidas()):
                bebida_seleccionada = menu.obtener_bebida(int(eleccion_bebida))
                pedido.agregar_item(bebida_seleccionada)
                subtotal += bebida_seleccionada.precio
                print(f"Has elegido: {bebida_seleccionada.nombre}")
                print("")
            else:
                print("Opción inválida. Por favor, elige una opción válida.")
                print("")

        elif opcion == "3":
            # Mostrar resumen del pedido y calcular total
            print("Resumen del pedido:")
            print("")

            for item in pedido.items:
                print(f"{item.nombre} - ${item.precio}")

            print(f"\nSubtotal: ${subtotal}")
            total = subtotal + (subtotal * 0.21)  # Aplicar IVA (21%) y redondear a 2 decimales

            print(f"Total (con IVA): ${total}")

            # Guardar el pedido en la base de datos
            import psycopg2

            # Establecer la conexión con la base de datos PostgreSQL
            conexion = psycopg2.connect(
                user='postgres',
                password='admin',
                host='127.0.0.1',
                port='5432',
                database='menu'
            )

            cursor = conexion.cursor()
            cursor.execute("INSERT INTO pedidos (nombre, total) VALUES (%s, %s)", (pedido.nombre, total))
            conexion.commit()

            # Cerrar la conexión con la base de datos
            conexion.close()

            break

    else:
        print("Opción inválida. Por favor, elige una opción válida.")
        print("")
