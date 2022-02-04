contraseña_actual = "alejandra"
print("para restablecer la contraseña ingrese la contraseña actual")
contra = input()
if contraseña_actual == contra:
    print("la contraseña es correcta")
    print("ingrese la nueva contraseña")
    contraseña_nueva = input()
    print("nueva contraseña restablecida :" + contraseña_nueva)
else:
    print("la contraseña es incorrecta")


