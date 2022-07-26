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
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''



print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio


print("ingrese el primer numero")
numero_1 = float(input())   # esta mal ponerlo como float por si la persona ingresa numeros con decimales?
print("ingrese el segundo numero") 
numero_2 = float(input())
print("ingrese el tercer numero")
numero_3 = float(input())

if numero_1 % 2 == 0 :
    print(numero_1, "Es un numero par")
else :
    print(numero_1, "Es un numero impar")
    
if numero_2 % 2 == 0 :
    print(numero_2, "Es un numero par")
else :
    print(numero_2, "Es un numero impar")

if numero_3 % 2 == 0 :
    print(numero_3, "Es un numero par")
else :
    print(numero_3, "Es un numero impar")

