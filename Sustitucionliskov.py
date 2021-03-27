"""
3. Principio de sustitución de Liskov
La idea principal detrás del principio de subtitulación de Liskov es que, para cualquier clase,
un cliente debería poder usar cualquiera de sus subtipos de manera indistinguible, sin siquiera
darse cuenta y, por lo tanto, sin comprometer el comportamiento esperado en tiempo de ejecución.
Esto significa que los clientes están completamente aislados y desconocen los cambios en la
jerarquía de clases.

En términos más simples, significa que una subclase, hijo o especialización de un objeto o clase
debe ser adecuada para su padre o superclase.
"""


class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrarNombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.nombre, self.apellido, self.edad)

    def datos(self):
        print(self.mostrarNombreCompleto())


class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, profesion):
        super().__init__(nombre, apellido, edad)
        self.profesion = profesion

    def datos(self):
        super().datos()
        print("Profesion: {0}.format(self.profesion)")


estu1 = Estudiante("Jhon", "Palacios", 31, "Estudiante")
estu2 = Estudiante("Sara", "Muñoz", 18, "Estudiante")

print(estu1.mostrarNombreCompleto())
print(estu1.profesion)
print(estu2.mostrarNombreCompleto())
print(estu2.profesion)
