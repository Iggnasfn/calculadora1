# clculadora.py

from division import division

from suma import sumar

# Código principal.

while(1):

    print("1. Suma\n2. Resta\n3. multiplicación\n4. division\n5. Finalizar\n")
    inicio = int(input("Que operación desea usar (Usa los numeros)? "))


    if inicio == 1:
        num1 = int(input("Ingrese primer número: "))

        num2 = int(input("Ingrese segundo número: "))

        print("Resultado:", sumar(num1, num2))

    if inicio == 4:
        num1 = int(input("Ingrese primer número: "))

        num2 = int(input("Ingrese segundo número: "))

        print("Resultado:", division(num1, num2))

    if inicio == 5:
        print("Termino la operación.")
        break