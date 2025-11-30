import os
from classes import Player

def create_player(starter_decks):
    os.system('cls')
    print("Bem-vindo ao Card RPG!")

    name = _ask_player_name()
    chosen_deck = _choose_starter_deck(starter_decks)

    player = Player(name, chosen_deck)
    print(f"Bem-vindo, {player.name}!")
    return player

def _ask_player_name():
    while True:
        name = input("Insira seu nome: ").strip()
        if name and not name.isnumeric():
            return name
        print("Nome inválido!")

def _choose_starter_deck(starter_decks):
    print("\nEscolha seu deck inicial:")
    for i, deck in enumerate(starter_decks, 1):
        print(f"{i} - {deck}")

    while True:
        try:
            choice = int(input("Deck: "))
            return starter_decks[choice - 1]
        except (ValueError, IndexError):
            print("Escolha inválida!")
