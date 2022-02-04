print("escriba el año actual")
año_actual  = int(input())
print("escriba un año cualquiera")
año_cualquiera = int(input())
if año_actual > año_cualquiera:
    años_pasados = año_actual - año_cualquiera
    print("han pasado " + str(años_pasados))
elif año_actual < año_cualquiera:
    años_pasados = año_cualquiera - año_actual
    print("faltan " + str(años_pasados))

