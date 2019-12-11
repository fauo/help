print ("\n\tBienvenido al generador de secuencias Fibonacci\n")
numero_ingresado = int(input("Ingrese un número de término: ")) # numero_ingresado = Número de términos que se desea imprimir

a = 0
b = 1
lista = [0] # Lista inicial con un valor predeterminado '0', al que posteriormente se le agregarán más datos

for i in range(numero_ingresado):
    # print (i+1, a) # Verificación que 'i' recorre correctamente el for
    a, b = b, a + b # Cálculo de Fibonacci
    lista = lista + [a] # Actualización de la lista, se agrega el resultado del cálculo

print ("\n\t|== SERIE SOLICITADA ==|\n")
print (lista)
