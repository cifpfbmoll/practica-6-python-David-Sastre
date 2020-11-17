#Escribir un programa para jugar a adivinar un número (el usuario piensa un número y el programa lo ha de adivinar)./
# El programa empieza pidiendo entre qué números está el número a adivinar y luego intenta adivinar de qué número se trata. /
# El usuario va diciendo si el número que ha dicho el programa es menor, mayor o igual al que se ha buscado.
#Valor mínimo: 0
#Valor máximo: 100
#Piensa un número entre 0 y 100 a ver si lo puedo adivinar.
#Es 50 ?: mayor
#Es 75 ?: menor
#Es 62 ?: menor
#Es 56 ?: mayor
#Es 59 ?: igual
#Gracias por jugar!!
#Mejoras (opcionales):
    #• que al principio el programa se asegure de que el valor máximo es superior al valor mínimo.
    #• Que el programa detecte "trampas", por ejemplo, si cuando dices "25" le decimos "mayor" y al decir "26" le decimos "menor", /
    # el programa debe decir que estamos haciendo trampas y debe dejar de jugar con nosotros.
import random
minimo=int(input("Valor mínimo: "))
maximo=int(input("Valor máximo: "))
print(f"Piensa un número entre {minimo} y {maximo} a ver si lo puedo adivinar.")
intento=random.randint(minimo, maximo)
respuesta=(input(f"Es {intento} ?: "))
while respuesta !='igual' and respuesta !='Igual':
    while respuesta == 'mayor' or respuesta =='Mayor':
        minimo=intento
        intento=random.randint(minimo, maximo)
        respuesta=input(f"Es {intento} ?: ")
    while respuesta == 'menor' or respuesta == 'Menor':
        maximo=intento
        intento=random.randint(minimo, maximo)
        respuesta=input(f"Es {intento} ?: ")    
print("Gracias por jugar!!")

