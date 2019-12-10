# Ejercicio 1
salir = 0

while (salir != 1):
    numero_a = int(input("Ingrese un valor para A: "))
    numero_b = int(input("Ingrese un valor para B: "))

    print ("El número ingresado para A es:", numero_a, "y para B:", numero_b)

    if (numero_a < numero_b):
        salir = 1
        print ("\nDatos guardados con éxito.")

    elif(numero_a >= numero_b):
        salir = 0
        print ("\nDa/tos incorrectos, ingrese un valor para A menor que B.\n")

    else:
        print ("Error")
        salir = 0

numeros_pares = 0
numeros_impares = 0

for i in range(numero_a, numero_b+1):
    # print ("El numero es:", i) # Corroborar si sirve el bucle

    if (i % 2 == 0):
        print ("El número", i, "es par.")
        numeros_pares = numeros_pares + 1
    elif (i % 2 != 0):
        print ("El número", i, "es impar")
        numeros_impares = numeros_impares + 1
    else:
        print ("Error")

print ("\nCantidad de números pares:", numeros_pares)
print ("Cantidad de números impares:", numeros_impares)
print ("\n")
