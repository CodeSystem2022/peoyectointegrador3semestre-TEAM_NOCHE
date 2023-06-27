# Realizado por Carlos Hernan Suarez
class Pedido:
    def __init__(self, nombre):
        self.nombre = nombre
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)


class Comida:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Quesadillas(Comida):
    def __init__(self):
        super().__init__("Quesadillas", 10.0)


class Tacos(Comida):
    def __init__(self):
        super().__init__("Tacos", 8.0)


class Tamales(Comida):
    def __init__(self):
        super().__init__("Tamales", 12.0)


class Botanas(Comida):
    def __init__(self):
        super().__init__("Botanas", 15.0)


class Burritos(Comida):
    def __init__(self):
        super().__init__("Burritos", 10.0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Realizado por Florencia Pons 
#Incorporamos la clase bebida al menú
class Bebida:
    def _init_(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Margarita(Bebida):
    def _init_(self):
        super()._init_("Margarita", 12.0)


class Gaseosa(Bebida):
    def _init_(self):
        super()._init_("Gaseosa", 5.0)


class Cerveza(Bebida):
    def _init_(self):
        super()._init_("Cerveza", 6.0)


class Tequila(Bebida):
    def _init_(self):
        super()._init_("Tequila", 10.0)


class Agua(Bebida):
    def _init_(self):
        super()._init_("Agua", 2.0)
____________________________________________________________________________________________________________________________________________________________________________
