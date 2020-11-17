#Escribe un programa que pida primero dos números (máximo y mínimo) y que después te pida números intermedios./
#  Para terminar de escribir números, escribe un número que no esté comprendido entre los dos valores iniciales. /
# El programa termina escribiendo la lista de números.
#Escribe un número: 6
#Escribe un número mayor que 6: 4
#4 no es mayor que 6. Vuelve a probar: 50
#Escribe un número entre 6 y 50: 45
#Escribe otro número entre 6 y 50: 13
#Escribe otro número entre 6 y 50: 4
#Los números situados entre 6 y 50 que has escrito son: 45, 13 

minimo=int(input("Escribe un numero: "))
maximo=int(input(f"Escribe un numero mayor que {minimo}: "))
lista_numero=[]
while minimo>maximo:
    print(f"{maximo} no es mayor que {minimo}", end=".")
    maximo=int(input("Vuelve a probar: "))
    maximo=maximo
numero=int(input(f"Escribe un numero entre {minimo} y {maximo}: "))
while minimo<numero<maximo:
    lista_numero.append(numero)
    numero=int(input(f"Escribe otro numero entre {minimo} y {maximo}: "))
    numero=numero
print(f"Los numeros situados entre {minimo} y {maximo} que has escrito son: ", end="")
for i in range (len(lista_numero)):
    if i==len(lista_numero)-1:
        print(lista_numero[i])
    else:
        print(lista_numero[i],end=", ")
