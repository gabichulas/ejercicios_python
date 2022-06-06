# Random Questions Quiz

import random

def quiz():
    question1 = ["Cual es el rio mas largo del mundo?","amazonas"]
    question2 = ["Cual es el oceano mas grande?","pacifico"]
    question3 = ["Cual es el disco mas vendido de la historia?","thriller"]
    question4 = ["Como se llama el himno de Francia?","marsellesa"]
    question5 = ["Como se llama un triangulo con sus 3 lados iguales?","equilatero"]
    qlist = [question1, question2, question3, question4, question5]
    puntos = 0
    cont = 0
    ran = len(qlist)-1
    largo = len(qlist)
    print("Bienvenido!")
    playing = input("Queres jugar? ")
    if playing != "si":
        quit()   
    while cont < largo:
        r = random.randint(0,ran)
        print(qlist[r][0])
        rta = input()
        if rta == qlist[r][1]:
            print("La respuesta es correcta! Ganaste un punto")
            puntos = puntos+1
        elif(rta != qlist[r][1]):
            print("La respuesta es incorrecta")
        cont = cont+1
        ran = ran - 1
        qlist.pop(r)
    print(f"Termino el juego! Conseguiste {puntos} puntos." )

quiz()




