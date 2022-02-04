import random
import time
 
## Listas de Palabras
frutas = ["fresa","banana","melon","piña","limon","uva","pera", "naranja", "kiwi", "cereza", "frambuesa", "mandarina"]
paises = ["panama","colombia","mexico","españa","costa rica","brasil","argentina","francia","ecuador","canada"]
 
 
print("bienvenido al juego ahorcado")
time.sleep(2)
print("intenta adivinar la palabra secreta letra por letra")
time.sleep(2)
print("tienes 10 vidas, si te equivocas vas perdiendo vida por vida")
time.sleep(2)
print("Si desea adivinar con frutas escriba 1, si desea adivinar con paises escriba 2")

 
while True:
    seleccion = int(input())
    if  seleccion == 1:
        palabra = random.choice(frutas)
        print("escogio frutas")
        break
    elif seleccion == 2:
        palabra = random.choice(paises)
        print("escogio paises")
        break
    else:
        print("esa no es una opcion, porfavor intentelo denuevo")
        time.sleep(2)
        print("Si desea adivinar con frutas escriba 1, si desea adivinar con paises escriba 2")

 
## Es el numero de veces que se puede eqivocar
vidas = 10
 
adivinadas = []
 
## Imprimimos la palabra sin letras
print(" _ " * len(palabra))
 
while True:
 
    while True:
        adivinada = input("Adivina una letra: ").lower()
        if(len(adivinada)!=1 and adivinada.isnumeric()):
            print("Eso no es una letra intenta con una sola letra")
        else:
            if adivinada.lower() in adivinadas:
                print("Ya habias intentado con esa letra intenta denuevo con otra por favor")
            else:
                adivinadas.append(adivinada)
 
                if adivinada.lower() in palabra:
                    print("adivinaste una letra")
                    break
                else:
                    vidas = vidas-1
                    print("Te haz equivocado y perdido una vida")
                    print("Te quedan " + str(vidas) + " vidas")
                    break
 
    if vidas==0:
        print("Haz perdido la palabra secreta era: "+ palabra)
        break
 
 
    estatus_actual = ""
 
    letras_faltantes = 0
    for letra in palabra:
 
 
        if letra in adivinadas:
            estatus_actual = estatus_actual + letra
 
        else:
            estatus_actual = estatus_actual + " _ "
            letras_faltantes = letras_faltantes + 1
 
    ## Imprimir palabra con algunas letras
    print(estatus_actual)
 
 
    if letras_faltantes == 0:
        print("Felicidades haz ganado!!!!")
        print("La palabra secreta es: " + palabra)
        break
