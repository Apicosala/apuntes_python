## Funciones (va intentar resolver un problema concreto) ###
def my_funcion():
    print("esto es una función")


my_funcion()  # tengo que llamar a la funcion para que me ejcute lo que le indico antes
"""
si llamara 3 veces la funcion:
my_funcion()
my_funcion()
my_funcion()
me ejecutaría 3 veces lo que le indique
en este caso imprime tres veces "esta es mi función"

"""


def sum_dos_valores(primer_numenro, segundo_numero):
    print(primer_numenro + segundo_numero)


sum_dos_valores(5, 7)
sum_dos_valores(121, 14)
sum_dos_valores(-12, 44)
print("seguimos")


def doble(num):
    print(2 * num)


doble(8)
doble(122)
print("uno más")


# retorna un valor de lo que indiquemos, antes teniamos que poner un print ahora no
# asignamos nuestra funcion a una variable
def suma_xy_return(x, y):
    return x + y


result_1 = suma_xy_return(10, 10)
result_2 = suma_xy_return(21, 3)
print(result_1)
print(result_2)


def print_name(nombre, apellido):
    # f me permite dar formato que se escriban los valores
    print(f"{nombre} {apellido}")


print_name(apellido="Picó",  nombre="Alex")


def name_default(nombre, apellido, alias="sin alias"):
    print(f"{nombre} {apellido} {alias}")


# al no poner un parametro en alias saldra el parametro asignado "sin alias"(Alex Picó sin alias)
name_default("Alex", "Picó")
# al poner un alias saldra el alias.(Jorge Soi Jorgito)
name_default("Jorge", "Soi", "Jorgito")


def print_textos(*text):  # al poner * nos permite escribir los textos que queramos
    print(text)


print_textos("Hola", "Python", "Textos", "Adios")
print_textos("a", "b", "c", "d", "e", "f", "g")
print_textos("hola")

# podemos incluir un for y nos lo imprime cada uno en una linea


def mas_textos(*texts):
    for texto in texts:
        # recordatorio: podemos indicar que me imprima todo mayusculas con .upper() o minuscula .lower()
        print(texto.upper())


mas_textos("Hola", "Python", "Textos", "Adios")
mas_textos("a", "b", "c", "d", "e", "f", "g")
