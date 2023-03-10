### Condicionales ###
"""
Si IF se cumple una <condición>: ejecuta "x" sino ELSE haz "y" 
Despues del IF en la linea de abajo se pone indentado (separicon de cuatro espacios)
si se cumple varias condiciones dentro de una utilizamos ELIF
el IF se ejecutabsi nuestra condione es True
"""
my_condition = True
if my_condition:  # es lo mismo que poner "if my_condition == True:"
    print("Se ejecuta la condición de if")

other_cond = [2, 4, 6, 8, 10]
if 2 in other_cond:
    print("ok")
else:
    print("no valid")

# si es 10 se ejecuta el if, si es mayor que 10(false) y si no imprime es menor o igual a 10
my_condition = 5 * 2
if my_condition == 10:
    print("Se ejecuta if al ser True")
if my_condition > 10:
    print(" es mayor que 10")
else:
    print("es menor o igual a 10")
"""
if <condicion 1>: (Si es True se ejecuta si es False probamos otra condición)
elif <condicion 2>: (Si es True se ejecuta si es False probamos otra condición)
else: (Si ambas son False entonces:  )
"""
if my_condition > 10 and my_condition < 20:
    print("es mayor que 10 y menor que 20")
elif my_condition < 2 and my_condition < 4:
    print("es menor que 4 y 2")
elif my_condition == 1:
    print("es igual a 1")
else:
    print("sigue buscando")
# Iportante: Hay un orden de jerarquia: primero comprueba el IF luego va comprobando los Elif hasta que encuentra el True y si no entonces ya recuure al ELSE

my_string = ""
# al no poner texto "" Python entiende que no es una cadena y que es False, por ello pondremos if not (si no es una cadena)
if not my_string:
    print("Mi cadena de texto esta vacia")
if my_string == "Esta cadena no esta vacia":
    print("esta cadena no  esta vacia")
