# Escribe un programa que pida notas y los guarde en una lista. /
# Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10./
# El programa termina escribiendo la lista de notas.
# Escribe una nota: 7.5
# Escribe una nota: 0
# Escribe una nota: 10
# Escribe una nota: -1
# Las notas que has Escrito son [7.5, 0.0, 10.0]
list=[]
print("Para terminar escribe una nota que no este entre 0 y 10: ")
notas=float(input("Escribe una nota: "))
while notas>0 and notas<=10:
    list.append(notas)
    notas=float(input("Escribe una nota: "))
print("Las notas que has escrito son: ", list[:])