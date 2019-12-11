import math

tope = int(input("Ingresar número: "))
print ("\n")

suma = 0

for n in range(tope):

    calculo = 1/math.factorial(n)
    suma = suma + calculo

    print ("Cálculo de (1/", n, "!) =", calculo)

print ("\nResultado final =", suma)
