#Escribe un programa que te pida primero un número y luego te pida números hasta/
#que la suma de los números introducidos coincida con el número inicial. /
#El programa termina escribiendo la lista de números.
#Escribe límite: 50
#Escribe un valor: 10
#Escribe otro valor: 45
#45 es demasiado grande. Escribe otro valor: 1
#Escribe otro valor: 39
#El límite a alcanzar es 50. La lista creada es: 10, 1, 39
limite=int(input("Escribe límite: "))
num=int(input("Escribe un valor: "))
lista_valor=[num]
while num>limite:
    lista_valor.remove(num)
    print(f"{num} es demasiado grande. ",end="")
    num=int(input("Escribe un valor: "))
    num=num
    lista_valor.append(num)
while sum(lista_valor) != limite:
    num_2=int(input("Escribe otro valor: "))
    lista_valor.append(num_2)
    while sum(lista_valor)>limite:
        lista_valor.remove(num_2)
        print(f"{num_2} es demasiado grande.", end="")
        num_2=int(input("Escribe otro valor: "))
        lista_valor.append(num_2)
print(f"El limite a alcanzar es {limite}. La lista creada es: ",end="")
for i in range (len(lista_valor)):
    if i==len(lista_valor)-1:
        print(lista_valor[i])
    else:
        print(lista_valor[i],end=", ")


