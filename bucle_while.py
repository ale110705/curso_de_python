print("ingrese un numero del 1 al 10")
numeros = int(input())
while numeros !=5:
    print("intentelo otra vez")
    numeros = int(input())
    if numeros == 5:
        print("numero encontrado")
        break
    