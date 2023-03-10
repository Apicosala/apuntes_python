### Diccionarios {Clave: Valor} ###
"""
Los diccioanrios se componen de una Clave: (Inmutable) y de un Valor (Mutable)
por cada Clave existe un valor, utilizamos las claves para
acceder a un Valor. Relación Clave_Valor
"""

my_dict = dict()
# podemos poner Claves tanto str, como int, float ...
my_other_dict = {"Nombre": "Alex", "Apellido": "Picó", "Edad": 46, 1: "Python"}
my_dict = {
    "Nombre": "Alex",
    "Apellidos": "Picó",
    "Edad": 46,
    "lenguajes": {"Python", "Swift", "Kotlin"},
    "Estudios": ("Eso", "Bat", "Grado"),
    "Hobies": ["Surf", "Paddel", "Escalada", "Skate"]
}
print(my_other_dict)
# hemos añadido en el valor un set, tambien una tupla y una lista en my_dict
print(my_dict)

print(len(my_dict))  # 6 cada Clave/Valor es un elemento
print(len(my_other_dict))  # 4

print(my_dict["Nombre"])
print(my_dict["lenguajes"])
# me imprime los valores: Alex y los tres lenguajes

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])
# Igual que podemos acceder a los valores tambien podemos modificar estos, en este caso modificamos Nombre
# imaginate que hemos cumplido años, modificaremos edad
my_dict["Edad"] = 47
print(my_dict["Edad"])

# si queremos añadir una Clave/Valor a nuestro diccionario, la podemos crear
my_dict["Calle"] = "Plaza del Ayuntamiento"
print(my_dict)
# nos ha añadido al final la Clave/Valor nueva ( en este caso calle)
del my_dict["Calle"]
# y asi nos cargamos un elemento Clave/Valor del Diccionario
print("Asi hemos borrado la CLave_Valor Calle:", my_dict)

### metodos en diccionario ###
my_dict.pop("Nombre")
print(my_dict)  # seria la forma de eliminar Clave/Valor funciona como del

print(my_dict.copy())  # me duplia el diccionario, me crea otro  igual

my_other_dict.clear()  # borra los elemntos del diccionario
print(len(my_other_dict))

my_dict.values()
print(my_other_dict)

# nos dara False pq nos lo cargamos antes con .pop("Nombre"), simepre buscamos por Clave no por Valor
print("Nombre" in my_dict)  # False
print("Estudios" in my_other_dict)
print("Edad" in my_dict)  # True
# dará False pq estamos buscando por valor (47) y no por su Clave "Edad"
print(47 in my_dict)

print(my_dict.items())  # nos retorna un listado de las Clave_Valor
print(my_dict.keys())  # nos retorna un listado de las Claves en forma lista []
# nos retorna un listado de los Valores en forma lista []
print(my_dict.values())

# sirve para crear un diccionario nuevo sin valores
print(my_dict.fromkeys(("Nombre", "Edad")))
my_new_dict = my_dict.fromkeys(("Nombre", "Edad"))
print(my_new_dict)
my_new_dict["Nombre"] = 34
print(my_new_dict)

mis_valores = my_dict.values()
print(type(mis_valores))  # es un diccionario de valores
print(mis_valores)
print(list(mis_valores))  # nos lo pasamos a lista
