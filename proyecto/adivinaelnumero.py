import random

num = random.randint(1,10)
intentos = 3


while True:
    print("te quedan " + str(intentos) + " intentos")
    print("ingrese un numero")
    usernumber = int(input())
    
    if num == usernumber:
        print("has ganado")
        break

    else:
        print("intentlo denuevo")
        intentos -= 1

    if intentos == 0:
        print("has perdido")
        break