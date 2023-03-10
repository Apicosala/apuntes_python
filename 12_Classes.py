### Classes  ###
"""
Nos permite identificar un código
dentro de un ámbito de actuación
(Todo lo realcionado con persona, o animales, ...)
tanto las variables, funciones, etc se escriben en "snake_case"
en cambio las clases se ponen en "CamelCases"

"""


class Person:
    pass


print(Person)
print(Person())


class MyPerson:
    def __init__(self, nombre, apellidos, alias="sin alias"):
        self.nombre = nombre
        self.apellidos = apellidos
        self.alias = alias
        # si quiero que el alias me salga entre () se los pongo aqui ({alias})
        # cunado ponga nombre completo va a salir el nombre en mayusculas .upper
        self.nombre_completo = f"{nombre.upper()} {apellidos} ({alias})"

    def aula_1(self):
        print(f"{self.nombre_completo} esta en aula 1 del Aulario")

    def aula_2(self):
        print(f"{self.nombre_completo} esta en aula 2 del Aulario")

    def get_nombre(self):
        return self.nombre


persona_1 = MyPerson("Alex", "Picó")
persona_2 = MyPerson("Jorge", "Sio", "Jorgito")
persona_3 = MyPerson("Paco", "Gadea", "Pacorro")

print(f"{persona_1.nombre} {persona_1.apellidos}")
print(f"{persona_1.nombre_completo}")
print(f"{persona_3.nombre_completo}")
print(f"{persona_3.alias}")

persona_1.aula_1()
persona_2.aula_1()
persona_3.aula_2()
"""
Alex Picó
ALEX Picó (sin alias)
PACO Gadea (Pacorro)
(Pacorro)
Alex Picó (sin alias) esta en aula 1 del Aulario
Jorge Sio (Jorgito) esta en aula 1 del Aulario
Paco Gadea (Pacorro) esta en aula 2 del Aulario
"""
print(persona_3.get_nombre()
      )  # puedo acceder a nombre completo pero no modificarlo al crear un get
