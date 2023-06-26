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


class Bebida:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Margarita(Bebida):
    def __init__(self):
        super().__init__("Margarita", 12.0)


class Gaseosa(Bebida):
    def __init__(self):
        super().__init__("Gaseosa", 5.0)


class Cerveza(Bebida):
    def __init__(self):
        super().__init__("Cerveza", 6.0)


class Tequila(Bebida):
    def __init__(self):
        super().__init__("Tequila", 10.0)


class Agua(Bebida):
    def __init__(self):
        super().__init__("Agua", 2.0)
