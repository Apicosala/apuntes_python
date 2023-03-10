# Operadores en PYTHON aritmeticos

print(2 + 4)
print(3 - 4)
print(1 - 6)
print(3 * 3)
print(12 / 4)
# a continuación nos dara como resultado un float
print(3 / 4)
"""
si queremos que el resultado de la division
solo nos de el numero utilizaremos 
        //
"""
print(18 // 5)
"""
si queremos obtener solo el resto de la division
o saber si es multiplo
o divisible utilzaremos 
    %
"""
print(19 % 5)  # nos dara como resultado 4

# exponentes y raices cuadradas
print(5 ** 3)  # seria 5 elevado a tres
print(16 ** (1/2))  # raiz cuadrada de 16
print(121 ** (1/3))  # raiz cubica de 121

# unimos cadenas str estos simbolos tambien unen palabras
print("hola " + "python " + "que tal? " + str(5))
# indicamos que el 5 es un str y no un entero para que no nos de error tambien podemos poner "5"
# pondría 5 veces hola, pondremos espacio despues de hola, si no lo pondría junto (holahola)
print("hola " * 5)

"""

comparativos

"""
print(3 > 4)
print(3 < 4)
print(3 == 4)
print(3 != 4)
print(3 >= 4)
print(3 <= 4)

### Operadores Lógicos ####
"""
"and"  si los dos son True es True si los dos son False son False, uno False y otro True = False
"or" si alguno operando es True entonces será True aunque los otros operandos sean False
"""

print(3 > 4 and "Hola" > "Python")  # false
print(3 > 4 or "Hola" > "Python")  # false
print(3 < 4 and "Hola" < "Python")  # True
# Aunque un operando sea false al haber uno True = True
print(3 < 4 or "Hola" > "Python")
