"""
## Listas ## 
las listas tienen la carateristica
que son mutables, es decir que se pueden modificar.
Ya veremos que las Tuplas son lista no mutables
"""
my_list = []
my_other_list = list()

print(len(my_list))  # nos daria un cero pq en nuestra lista no hay elementos

"""

En las listas los elementos empiezan 
por 0, 1, 2, etc

"""

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
# las listas pueden tener enteros, float, str (siempre entre "")
my_other_list = [46, 1.78, "Alejandro"]
print(my_other_list)
print(type(my_other_list))  # me dira que <class 'list'> que es una lista
# con el indice [] ñe decimos que parte de la lista queremos: del primer elemento 0 hasta el 4 (4 no entra)
print(my_list[0:4])
print(len(my_list))
print(my_list[-1])  # me daria como resultado el ultimo de la lista: 17

"""
#### MÉTODOS EN LAS
LISTAS #####
"""
print("lista original:", my_list)
my_list.sort()
# el método .sort() me ordenada la lista de mayor a menor o alfabeticamente
print("lista ordenada:", my_list)
# .sort(reverse=True) nos ordena la lista de forma descendente o de menor a mayor
my_list.sort(reverse=True)
print("sort de forma descendente:", my_list)

my_list.reverse()
# el método .reverse() me pone la lista al reves.
print("lista al reves:", my_list)

# .count() nos dice cuantas veces está en la lista el parametro que le indiquemos
print("cuantas veces está el elemento 30:", my_list.count(30))

# .index()nos indica en que posicion esta el parametro que indiquemos.
print("En que pisición está 52:", my_list.index(52))

my_list1 = [32, "Esther", 2.5, "Mutxamel"]
my_list.extend(my_list1)  # le estamos indicando que añada my_list1 a my_list
# .extend() añade o extiende nuestra lista con otra lista que añadimos como parametro
print("Ahora tenemos la union de las 2 listas", my_list)

my_list1.clear()  # .clear() elimina todos los elementos de una lista
# nos dejaria una lista sin elementos
print("resultado de clear en una lista", my_list1)

print("la lista original", my_list)
my_list.append("Zoe")  # .append me añade elmentos al final de nuestra lista
print("append me añade el parametro al final:", my_list)

# con .insert() le indico en que indice quiero introducir el elemento
my_list.insert(4, 141)
print("me insertará en la posicion 4 el 141:", my_list)

# me eliminará el primer 30 que encuentre, si tuviera mas 30 NO los elimina
my_list.remove(30)
print("lista despues de remove:", my_list)

my_list.pop()  # .pop() elimina el elemento que indiquemos en el parametro, si no indicamos ninguno normalmente elimina el último
my_list.pop(5)
print(my_list)
my_list.pop(0)
print(my_list)
# me eliminara el ultimo pero me lo enseñará o retornara en la consola, me dice que elemento quita
print(my_list.pop())

### Otra forma de eliminar de las listas seria con del ###
del my_list[2]  # me eliminaria el indice 2
print(my_list)

#### Rebandas de listas ###

print(my_list[2:6])  # me daria los elementos del 2 al 6
print(my_list[0:4])
