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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''
temperatura_Maxima = float
temperatura_minima = float
Promedio_temperatura = float

print("Ingrese la primer temperatura :")
temperatura_1 = float(input())
temperatura_Maxima = temperatura_1
temperatura_minima = temperatura_1

print("Ingrese la segunda temperatura :")
temperatura_2 = float(input())

if (temperatura_2 > temperatura_1) :
    temperatura_Maxima = temperatura_2 # esta mal escribir los IFs entre inputs?

if (temperatura_2 < temperatura_minima) :
    temperatura_minima = temperatura_2

print("Ingrese la tercer temperatura :")
temperatura_3 = float(input())

if (temperatura_3 > temperatura_Maxima) :
    temperatura_Maxima = temperatura_3

if (temperatura_3 < temperatura_minima) :
    temperatura_minima = temperatura_3

Promedio_temperatura = temperatura_1 + temperatura_2 + temperatura_3 / 3

print("La temperatura maxima registrada fue de : " ,temperatura_Maxima,"Grados")
print("La temperatura minima registrada fue de : " ,temperatura_minima,"Grados")
print("El promedio de temperaturas fue de :" ,Promedio_temperatura, "Grados")







print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
