"""
Principio de inversión de la dependencia
La dependencia debe estar en abstracciones, no en concreciones. Los módulos de alto nivel no deben 
depender de módulos de bajo nivel. Tanto las clases de nivel bajo como las de alto nivel deberían depender 
de las mismas abstracciones. 

Las abstracciones no deberían depender de los detalles. Los detalles deben depender de abstracciones.
"""

from abc import ABC, abstractmethod


class Comida(ABC):
    @abstractmethod
    def hornear(self, tiempo): pass


class Production():
    def __init__(self):
        self.pan = Pan()

    def produccion(self):
        self.pan.hornear(True)


class Pan(Comida):
    def hornear(self, tiempo: bool):
        print("El pan fue Horneado")
