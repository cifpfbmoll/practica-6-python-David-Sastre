#Escribe un programa que pida un número (límite) y luego te pida números /
# hasta que la suma de los números introducidos supere el límite inicial. /
#El programa termina escribiendo la lista de números.
#Escribe límite: 50
#Escribe un valor: 10
#Escribe otro valor: 25
#Escribe otro valor: 7
#Escribe otro valor: 14
#El límite a superar es 50. La lista creada es 10, 25, 7, 14 ya que la suma de estos números es: 56
limite=int(input("Escribe limite: "))
valor=int(input("Escribe un valor: "))
lista_numero=[valor]
while sum(lista_numero)<limite:
    valor2=int(input("Escribe otro valor: "))
    lista_numero.append(valor2)
print(f"El numeros a superar es {limite}. La lista creada es: ", end="")
for i in range (len(lista_numero)):
    if i==len(lista_numero)-1:
        print(lista_numero[i], end=" ")
    else:
        print(lista_numero[i],end=", ")
print(f"ya que la suma de estos número es: {sum(lista_numero)}")




