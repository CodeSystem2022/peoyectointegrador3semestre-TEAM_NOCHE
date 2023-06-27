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
    print("        |_| || || || || || || || || |__|         by TEAM NOCHE")
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











#Código agregado por Maria del carmen Gonzalez (Maru)
# Función para verificar si una opción es válida
def es_opcion_valida(opcion, max_opcion):
    try:
        opcion_num = int(opcion)
        return opcion_num >= 1 and opcion_num <= max_opcion
    except ValueError:
        return False
