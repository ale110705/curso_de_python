print("ingrese un numero")
numero1 = int(input())
print("ingrese un segundo numero")
numero2 = int(input())
print("ingrese un tercer numero")
numero3 = int(input())

if numero1 == numero2: 
    if numero1 == numero3:
        print("los tres numeros son iguales")
    else:
        print("el primer y segundo numero son iguales y el tercero es diferente")
elif numero2 == numero3:
    print("el segundos y tercer numeros son iguales y el primero es diferente")
elif numero1 == numero3:
    print("el primer y tercer numero son iguales y el segundo es diferente")
else:
    print("todos los numeros son diferentes")


    