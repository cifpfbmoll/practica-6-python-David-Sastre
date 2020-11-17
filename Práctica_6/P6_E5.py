# Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista./ 
# Para acabar de escribir los números, escribe un número que no sea mayor que el anterior./
# El programa termina escribiendo la lista de números:
#Escribe un número: 6
#Escribe un número mayor que 6: 10
#Escribe un número mayor que 10: 12
#Escribe un número mayor que 12: 25
#Escribe un número mayor que 25: 9
#Los números que has escrito son: 6, 10, 12, 25 
numero=int(input("Escribe un número: "))
numero2=int(input(f"Escribe un numero mayor que {numero}: "))
lista_numero=[numero]
while numero<numero2:
    numero=numero2
    lista_numero.append(numero)
    numero2=int(input(f"Escribe un numero mayor que {numero2}: "))
print("Los numeros que has escrito son: ",end="")
for i in range (len(lista_numero)):
    if i==len(lista_numero)-1:
        print(lista_numero[i])
    else:
        print(lista_numero[i],end=", ")