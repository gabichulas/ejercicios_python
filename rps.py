import random
def play():
    user = (input("Cual es tu eleccion? Rock (R), Paper (P) o Scissors (S): "))
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Empate!'

    if win(user, computer):
        return 'Ganaste!'

def win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "p" and opponent == "s") or (player == "s" and opponent == "p"):
        return True

print(play())







