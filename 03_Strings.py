# Strings variables
my_string = "Mi String"
my_other_str = "mi otro string"

# si queremos saber cuantos letras y esapios tiene mi str utilizaremos len
print(len(my_string)) # nos dara 9
print(len(my_other_str)) # nos dara 14
print(my_string + " " + my_other_str) # añadimos el espacio para que no se junten

my_new_line_str = "Este es un String\ncon salto de linea" # \n nos hace saltar linea, no dejamos espacio entre \n y la siguiente palabra pq si no apareceria el espacio el la linea de abajo
print(my_new_line_str)

my_tab_str = "\tEste es un String con tabulación"
print(my_tab_str)

my_scape_str = "\tMe tabula esta primera linea \nla seguna linea de abajo no la tabula"
print(my_scape_str)

## Formateo de String
name, surname, age = "Alex", "Picó", 46
print("Mi nombre es {} {} y mi edad es {} ". format(name, surname, age)) 
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # %s formatea str y %d formatea números enteros
# Inferencia de datos
print(f"Mi nombre es {name} {surname} y mi edad {age}") # La f delante de las "" nos permite añadir entre {} variables
"""
lo que hemos relaizado es formatear la infromacion que 
ya existia en el sistema para que coja la informacion de las variables de 
ahora, formatear un valor

"""
## Desempaquetado de Caracteres en String

lenguaje = "Python"
a, b, c, d, e, f = lenguaje
print(a) # pondria P
print(c) # pondria t

##Divison de caracteres
lenguaje_dividido = lenguaje[1:3] # 0 seria la P, 1=y, 2=t, 3=h, 4=o, 5=n, le estmos diciendo que coja los caracteres desde el 1 hasta el 3 sin coger el 3, el ultimo no se coge
print(lenguaje_dividido)
otro_eje = lenguaje[0:4] # me daria Pyth
print(otro_eje)
mas_ejem = lenguaje[0:6:2] # le estamos diciendo que coja los caracteres del 0 al 6 pero que muestre de 2 en 2, Pto como resultado
print(mas_ejem)
## ponerlo al reves Reverse
reverse_lenguaje = lenguaje[::-1]
print(reverse_lenguaje) # lo escribe al reves

#### Funciones en STR #####
print(lenguaje.capitalize()) # me pone la primera letra en Mayuscula
print(lenguaje.upper()) # todo mayuscula
print(lenguaje.lower()) # todo minuscula
print(lenguaje.count("t")) # me cuenta las "t" que hay en la palabra, daria 1
print(lenguaje.isnumeric()) # daria un bool false pq no es numerico
"""
cuando ponemos "IS": isnumeric(preguntamos si es numerico),
isupper(preguntamos si son todo mayusculas),
islower(si es todo minuscula))
Y devuelve un Bool False or True
"""