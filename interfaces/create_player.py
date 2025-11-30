import os
from classes import Player

def create_player(starter_decks):
    os.system('cls')
    print("Bem-vindo ao Card RPG!")

    while True:
        name = input("Insira seu nome: ")
        if not name.isdigit():
            break
        print("Nome inválido!")
    
    print("Escolha seu deck inicial:")
    for i, deck in enumerate(starter_decks, 1):
        print(f"{i} - {deck}")

    while True:
        choice = input("Deck: ")
        if choice.isdigit() and 1 <= int(choice) <= len(starter_decks):
            chosen_deck = starter_decks[int(choice) - 1]
            break
        print("Escolha inválida!")

    player = Player(name, chosen_deck)
    print(f"Bem-vindo, {player.name}!")
    return player
