"""
Try:
Vamos a ejecutar un código, si este falla o se produce un error en la ejecución:
except (se iria a except:)

si no se produce error:
else: (se va al bloque de else)

y pase lo que pase error o no:
finally: (corre el bloque de finallly)
"""
num_1 = 5
num_2 = 1
num_2 = "1"  # probocamos el error poniendo una suma entre un int y una str

try:
    print(num_1 + num_2)
    # esta linea no se ejecuta pq da un error, salta al except
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
# nos indica que hay un error pero no nos pra el programa

### Try, Except y Else ###
try:
    print(num_1 + num_2)
    # esta linea no se ejecuta pq da un error, salta al except
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:  # es opcional
    print("La ejecución continua correctamente")
finally:  # es opcional
    print("Continuamos!!")
# finally se ejecuta siempre

### Captura de excepciones por tipo ###
try:
    print(num_1 + num_2)
    print("No se ha producido un error")
except TypeError:  # solo se va a ejecutar si es un error de Type; hay muchos tipos de errores, le estoy diciendo que solo capture errores de
    print("Se ha producido un error")

try:
    print(num_1 + num_2)
    print("No se ha producido un error")
# al no ser un error de valor (value) se dentendra todo me dara error y no se ejecuta el except, dado que es error de Type
# solo captura errores de value
except ValueError:
    print("Se ha producido un error")

try:
    print(num_1 + num_2)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un error")
except TypeError:
    print("Se ha producido un error")
# podemos controlar varios tipos de errores, en este caso al haber un error Type se ejecuta
"""
 si queremos capturar el tipo de error, vamos a dejar que se ejecute except si 
 hay erres de Type o Value
 pero luego queremos saber que tipo de error existe
 """
try:
    print(num_1 + num_2)
    print("No se ha producido un error")
except ValueError as error_valor:
    print("Se ha producido un error")
    print(error_valor)
except TypeError as error_type:
    print("Se ha producido un error")
    print(error_type)
except Exception as excepción:  # excepciones genericas
    print(excepción)
# me indica: unsupported operand type(s) for +: 'int' and 'str'
