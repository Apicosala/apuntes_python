### TUPLES ###
"""
Una tupla son listas de elementos que son inmutables, no se pueden modificar.
Una lista es mutable, en cambio, una tupla no

"""
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (46, 1.78, "Alejandro", "Picó")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[0:2])

# funciona igual que las listas .count() nos dice cunatas veces esta un elemento
print(my_tuple.count(46))

# nos dice en que posición esta el elemento que indicamos, nos dice el indice
print(my_tuple.index("Alejandro"))

# saber si elemento exite en una Tupla
print("Alejandro" in my_tuple)
print(34 in my_tuple)
