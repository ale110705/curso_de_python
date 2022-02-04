print("escriba el año actual")
año_actual  = int(input())
print("escriba un año cualquiera")
año_cualquiera = int(input())
if año_actual > año_cualquiera:
    años_pasados = año_actual - año_cualquiera
    if años_pasados == 1:
        print("ha pasado un año desde " + str(año_cualquiera))
    else:
        print("han pasado " + str(años_pasados)+ " años desde el año " + str(año_cualquiera))
elif año_actual < año_cualquiera:
    años_pasados = año_cualquiera - año_actual
    if años_pasados == 1:
        print("falta un año para el " + str(año_cualquiera))
    else: 
        print("faltan " + str(años_pasados)+ " años hasta el año " + str(año_cualquiera))
elif año_actual == año_cualquiera:
    print("los años son iguales")




    




#mejorar cambie la oracion para singular
#mejorar las igualdad d los años