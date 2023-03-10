### Loops (Bucles o ciclos) ###
###  while (mientras sea True haz algo) ###
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # es opcional
    print("Mi condicion es mayor o igual que 10 y se detiene mi loop")

"""
el resultado seria: (mientras que my_condition < 10 imprime my_condition)
0 
2 (pq my_cpndition incrementa de 2 en 2, ya no es cero)
4
6
8
Mi condicion es mayor o igual que 10 y se detiene mi loop (else: me permite que cuando la 
condicion no se cumpla indicarle que queremos hacer o decir)
se acabaria pq 10 no es menor que 10
"""
my_cond = 10
while my_cond < 20:
    # escribirá Mi cond es menor que 20 5 veces (los pasos hasta llegar a ser = o mayor 20)
    print("Mi cond es menor que 20")
    my_cond += 2
if my_cond == 15:
    print("Mi condicion es 15")

while my_cond < 20:
    my_cond += 1
    if my_cond == 15:
        print("Se detiene la ejecución del loop")
        break  # el break me para el ciclo aunque 15 < 20 le indicamos parar
print("seguimos")

x = 20
while x < 35:
    print(x)
    x += 4  # se incrememta hasta que deja de ser True X<35
print("adelante")

"""
para para un ciclo infinito, imaginemos que no ponemos una condion que haga detener 
el ciclo y lo ejecutamos
control + c
y paramos la ejecución del loop infinito
"""
### For (para iterar un listado (listas, dicc, sets, tuple) de elementos, repetirlos las veces que queramos)  ###

my_list = [35, 24, 62, 52, 30, 30, 17]
for element in my_list:
    print(element)
# me imprime todos los elementos de my_list de arriba a abajo

my_tuple = (46, 1.78, "Alejandro", "Picó")
for element in my_tuple:
    print(element)

my_set = {"Alejandro", "Pico", 46}
for elemento in my_set:
    print(elemento)

my_dict = {"Nombre": "Alex", "Apellido": "Picó", "Edad": 46,
           1: "Python"}  # asi solo imprime Claves y no su valor
for element in my_dict:
    print(element)
for element in my_dict.values():  # asi nos imprime los valores
    if element == "Picó":
        break  # paramos el ciclo for, lo interrumpimos
    print(element)
else:  # opcional este else
    # en este caso hemos parado el ciclo for con el break y no se muestyra else sino se mostraria
    print("Mi ciclo for para dict ha terminado")

my_dict = {"Nombre": "Alex", "Apellido": "Picó", "Edad": 46,
           1: "Python"}  # asi solo imprime Claves y no su valor
for element in my_dict.values():
    if element == "Picó":
        continue
    # habia parado en picó con Break y ahora le hemos dado la orden de continuar
    print(element)

# hemos utilizado la palabra element pero podiamos haber utilizado cualquiero otra, ejemplo en el set que hemos puesto elemento

my_list = [35, 24, 62, 52, 30, 30, 17]
for variable_control in range(1, 3):  # escribira my_list 2 veces
    print(my_list)

for variable_control in range(4):
    print(my_list)  # escribe 4 veces la lista, si no ponemos inicio por defecto es 0
