import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Adivina un numero entre 1 y {x}: "))
        if guess < random_number:
            print("El numero que elegiste es menor")
        elif guess > random_number:
            print("El numero que elegiste es mayor")

    print(f"Adivinaste el numero! Era {random_number}")
guess(100)