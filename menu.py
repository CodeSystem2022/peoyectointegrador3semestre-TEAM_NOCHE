#Alfredo Marino
#vamos a introducir la clase menu del restaurante.

class Menu:
    def _init_(self):
        self.comidas = []
        self.bebidas = []

    def agregar_comida(self, comida):
        self.comidas.append(comida)

    def agregar_bebida(self, bebida):
        self.bebidas.append(bebida)

    def mostrar_comidas(self):
        print("Comidas disponibles:")
        for i, comida in enumerate(self.comidas, start=1):
            print(f"{i}. {comida.nombre} - ${comida.precio}")

    def mostrar_bebidas(self):
        print("Bebidas disponibles:")
        for i, bebida in enumerate(self.bebidas, start=1):
            print(f"{i}. {bebida.nombre} - ${bebida.precio}")

    def obtener_comida(self, opcion):
        return self.comidas[opcion - 1]

    def obtener_bebida(self, opcion):
        return self.bebidas[opcion - 1]

    def obtener_cantidad_comidas(self):
        return len(self.comidas)

    def obtener_cantidad_bebidas(self):
        return len(self.bebidas)
