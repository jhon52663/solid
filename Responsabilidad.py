"""
1. Principio de responsabilidad única
El principio de responsabilidad única requiere que una clase solo tenga un trabajo.
Entonces, si una clase tiene más de una responsabilidad, se acopla.
Un cambio en una responsabilidad da como resultado la modificación de la otra responsabilidad.

"""

class Usuario:
    def __init__(self, nombre: str):
            self.nombre = nombre
    
    def get_nombre(self):
        pass

class UsuarioDB:
    def get_usuario(self, id) -> Usuario:
       pass
    def save(self, user: Usuario):
        pass