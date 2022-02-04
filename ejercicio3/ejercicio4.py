


print("ingrese un numero")
numero = int(input())
print("ingrese el segundo numero")
numero2 = int(input())
print("seleccione una operacion")
print("1 suma")
print("2 resta")
print("3 division")
print("4 multiplicacion")
opcion = int(input())
if opcion == 1:
   resultado = numero + numero2
   print("el resultado de la suma es: " + str(resultado))
elif opcion == 2:
    resultado = numero - numero2
    print("el resultado de la resta es: " + str(resultado))
elif opcion == 3:
    resultado = numero / numero2
    print("el resultado de la division es: " + str(resultado))
    cociente = numero % numero2
    if cociente == 0:
        print("exacta")
    else:
        print("no exacta")


elif opcion == 4:
    resultado = numero * numero2
    print("el resultado de la division es:  " + str(resultado))


