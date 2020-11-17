#Desarrolla de nuevo el ejercicio de la práctica anterior de los números primos, con while./
#Reflexiona y escribe en el propio programa en forma de comentario, qué opción es mejor y por qué.
num=int(input("Dame un numero mayor que 0: "))
if num <= 0:
    print("Error. Dame un numero mayor que 0: ")
else:
    divisor = 0
    i = 2
    while (i < num):
        if num % i==0:
            divisor += 1
        i += 1
    if divisor == 0 and num > 1:
        print ("El numero es primo")
    else:
        print ("No es un numero primo")
    
