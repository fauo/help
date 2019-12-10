numero_base = int(input("Ingrese un número para la base: "))
numero_exponente = int(input("Ingrese un número para elevar: "))

print ("Numero base:", numero_base)
print ("Numero exponente:", numero_exponente)

i = 1
resultado = 1

while (i <= numero_exponente):
    resultado = resultado * numero_base
    i = i + 1

print ("Resultado final:", resultado)
