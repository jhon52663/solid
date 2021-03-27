"""
Principio de segregación de interfaces
Cree interfaces de grano fino que sean específicas del cliente. Los clientes no deberían verse obligados
a depender de interfaces que no utilicen. Este principio se ocupa de las desventajas de implementar grandes
interfaces.

"""


class IForma:
    def dibujar(self):
        raise NotImplementedError


class Cicululo(IForma):
    def dibujar(self):
        pass


class Cuadrado(IForma):
    def dibujar(self):
        pass


class Rectangulo(IForma):
    def dibujar(self):
        pass
