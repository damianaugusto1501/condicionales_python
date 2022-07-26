# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

Orden_Alfabetico_1 = str
Orden_Alfabetico_2 = str
Orden_Alfabetico_3 = str
Orden_de_longitud_1 = str
Orden_de_longitud_2 = str
Orden_de_longitud_3 = str

print("Ingrese la primer palabra")
palabra_1 = str(input())

Orden_Alfabetico_1 = palabra_1
Orden_de_longitud_1 = palabra_1

print("Ingrese la segunda palabra")
palabra_2 = str(input())

if palabra_2[0] < Orden_Alfabetico_1[0]:
    Orden_Alfabetico_1 = palabra_2
else :
    Orden_Alfabetico_2 = palabra_2

if len(palabra_2) > len(Orden_Alfabetico_1) :
    Orden_de_longitud_1 = palabra_2
else :
    Orden_de_longitud_2 = palabra_2


print("Ingrese la tercer palabra")
palabra_3 = str(input())


if palabra_3[0] < Orden_Alfabetico_2 [0] :
    Orden_Alfabetico_2 = palabra_3
    Orden_Alfabetico_3 = palabra_2
else :
    Orden_Alfabetico_3 = palabra_3

if palabra_3[0] < Orden_Alfabetico_2[0] and palabra_3[0] < Orden_Alfabetico_3[0] :
    Orden_Alfabetico_3 = Orden_Alfabetico_2
    Orden_Alfabetico_2 = Orden_Alfabetico_1
    Orden_Alfabetico_1 = palabra_3

if len(palabra_3) > len(Orden_de_longitud_2) :
    Orden_de_longitud_2 = palabra_3
    Orden_de_longitud_3 = palabra_2
else :
    Orden_de_longitud_3 = palabra_3

if len(palabra_3) > len(palabra_2) and len(palabra_3) > len(palabra_1) :
    Orden_de_longitud_3 = Orden_Alfabetico_2
    Orden_de_longitud_2 = Orden_de_longitud_1
    Orden_de_longitud_1 = palabra_3




print("Ingrese como quiere ordenar , Alfabeticamente : 1 , Por cantidad de letras : 2 ")
Opcion_para_elegir = int(input())

if Opcion_para_elegir == 1 :
    print("el orden alfabetico es : {} ,{} ,{}" .format(Orden_Alfabetico_1,Orden_Alfabetico_2,Orden_Alfabetico_3))
else :
    print("El Orden por longitud de palabra es {} , {} , {}:" .format(Orden_de_longitud_1,Orden_de_longitud_2,Orden_de_longitud_3))
