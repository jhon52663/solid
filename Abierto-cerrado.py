"""
Principio abierto-cerrado
Las entidades de software (clases, módulos, funciones) deben estar abiertas para extensión, no modificación.


Imaginemos que tienes una tienda y le das un descuento del 10% a tus clientes favoritos usando esta clase: 
Cuando decides ofrecer el 20% de descuento a los clientes VIP.
Puede modificar la clase de esta manera:
"""

class Descuento:
    def __init__(self, cliente, precio):
      self.cliente = cliente
      self.precio = precio
    def get_descuento(self):
      return self.precio * 0.1
  
class VIPDescuento(Descuento):
    def get_descuento(self):
      return super().get_descuento() * 2
     
      
      
