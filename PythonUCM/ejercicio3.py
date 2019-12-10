numero_factorial = int(input("Ingrese un número entero positivo: "))
num = numero_factorial

if (numero_factorial <= 0):
    print ("Resultado = 1")

elif (numero_factorial > 1):
    i = 1
    resultado_factorial = 1

    while numero_factorial > i:
        resultado_factorial = resultado_factorial * numero_factorial
        numero_factorial = numero_factorial - 1

    print ("Resultado de", num, "factorial (", num,"!), es =", resultado_factorial)

else:
    print ("Error")
