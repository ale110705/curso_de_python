import random
opciones = ["piedra", "papel", "tijera"]
while True: 
    print("elija una opcion")
    eleccion_pc = random.choice(opciones)

    eleccion_user = input()
    print("la computadora eligio " + eleccion_pc)
    if eleccion_user == eleccion_pc:
        print("Empate!!!")

    elif eleccion_pc == "piedra" and eleccion_user == "papel":
        print("has ganado!!!")
    elif eleccion_pc == "piedra" and eleccion_user == "tijeras":
        print("has perdido")
    elif eleccion_pc == "papel" and eleccion_user == "piedra":
        print("has perdido")
    elif eleccion_pc == "papel" and eleccion_user == "tijeras":
        print("has ganado!!!")
    elif eleccion_pc == "tijeras" and eleccion_user == "piedra":
        print("has ganado!!!")
    else:
        print("has ganado")
       
    print("quieres seguir jugando? Si o No")
    respuesta = input()
    if respuesta == "si": 
       pass
    else:
        print("gracias por jugar")
        break
