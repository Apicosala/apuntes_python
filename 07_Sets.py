### Sets ###
"""
Los Sets nos permiten guarda cojuntos de elementos desordenados
pero con la caracterisrica que no pueden haber repetidos
"""
my_set = set()
my_other_set = {}
print(type(my_set))
print(type(my_other_set))  # Inicialmente me dice qu es un diccionario

my_other_set = {"Alejandro", "Pico", 46}
# nos da como valor un set y no diccionario y es pq los sets no llevan Clave:Valor ("A": 45, "B": 32)
print(type(my_other_set))
# recordatorio: len nos dice los elementos de nuestra lista, set, tupla, ...
print(len(my_other_set))
print(my_other_set)
my_other_set.add("Sala")
# un set NO es una estructura ordenada, no hay indice ni está ordenado
print("Resultado de mi set tras add:", my_other_set)
# le volvemos a decir que nos añada Sala, pero al estar ya en un set NO se añade, no admite repetidos.
my_other_set.add("Sala")
print(my_other_set)

# saber si un elemento es parte de nuestro set
print("Sala" in my_other_set)  # True
print(144 in my_other_set)  # False

# remove borra del set el elemento que indiquemos en el parametro
my_other_set.remove("Sala")
print(my_other_set)

my_set.clear()  # borra los elementos del set
del my_set  # borra tambien los elementos del set

my_other_set.update()
print(my_other_set)  # actualiza nuestro set y nos da el resultado
my_other_set.difference(my_other_set)  # diferencias entre set
print(my_other_set)

my_list = list(my_other_set)
print(my_list)  # hemos convertido set en una lista en la variante my_list
# me daria como resultado el elemto en en indice 0 de los elemntos del set covertidos en lista.
print(my_list[0])

my_set1 = {"kotlin", "Swift", "Python"}
my_new_set = my_other_set.union(my_set1)
print("este es el resultado de la unión de 2 set:", my_new_set)
my_new_set1 = my_other_set.union(my_new_set).union({"Javascript", "C#"})
print(my_new_set1)
# se unen ambos sets de forma desordenada, dado que un set no es ordenado.

"""
Recordatorio:
Al unir dos set o varios set, todos los elementos repetidos se omiten, los set NO admiten 
elementos repetidos.
"""

print(my_other_set.difference(my_new_set1))
# diferencias entre sets
