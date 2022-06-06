# name = input("Hola! Ingresa tu nombre: ")
# print(f"Hola {name}" + "!")

# res = (((3+2)/(2*5))**2)
# print(res)

# horas = float(input("Horas trabajadas: "))
# cph = float(input("Coste por hora: "))
# res = horas*cph
# print(res)

# pes = float(input("Ingresa tu peso: "))
# est = float(input("Ingresa tu estatura en metros: "))
# res = round(pes/(est**2))
# print(f"El indice de masa corporal es {res}")

# chano = str(input("Ingrese una cancion: "))
# if chano == "chano":
#     print("mecha mechaaaaaaaaaaaaaaaaa")
# else:
#     print("liiibertaaaaaaaaaaaaaaad")

user = str(input("Ingresa tu usuario: "))
pw = str(input("Ingresa tu contraseña: "))
if pw == "rodriguito13":
    print(f"Hola, {user}, has ingresado correctamente al sistema.")
else:
    pw = str(input("La contrasena es incorrecta, ingresala de nuevo: "))
    if pw == "rodriguito13":
        print(f"Hola, {user}, has ingresado correctamente al sistema.")
    else:
        print("Error, intenta mas tarde.")


