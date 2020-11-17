#Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero./
# El programa termina escribiendo los dos números tal y como se pide:
#Escribe un número: 6
#Escribe un número mayor que 6: 6
#6 no es mayor que 6. Vuelve a introducir un número: 1
#1 no es mayor que 6. Vuelve a introducir un número: 8
#Los números que has escrito son 6 y 8
numero=int(input("Dame un número "))
numero2=int(input(f"Escribe un numero mayor que {numero}: "))
while (numero>=numero2):
    print(f"{numero2} no es mayor que {numero}.")
    numero2=int(input("Vuelve a introducir un numero. "))
print(f"Los números que has escrito son {numero} y {numero2}")

    
