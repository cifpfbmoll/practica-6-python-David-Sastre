#Escribe un programa que te pida números y los guarde en una lista./
# Para terminar de introducir número, simplemente escribe “Salir”. /
#   El programa termina escribiendo la lista de números.
list=[]
print("Escribe 'salir' para terminar.")
numero=(input("Escribe un número: "))
while numero !="salir":
    list.append(numero)
    numero=(input("Escribe otro número: "))
print ("Los números que has escrito son: ", list[:])
