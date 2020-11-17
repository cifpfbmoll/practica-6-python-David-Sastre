#Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras,/
# simplemente pulsa Enter. El programa termina escribiendo la lista de palabras.
list=[]
print("Pulsa enter para terminar.")
palabra=input("Escribe una palabara: ")
while palabra !="" "":
    list.append(palabra)
    palabra=input("Escribe mas palabras: ")
print("Las palabras que has escrito son:", list[:])
