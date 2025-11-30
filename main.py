from classes import Store, Card, Location, Player, Combat, Deck
from seed import create_cards, create_locations, create_starter_decks, create_store_cards
import os

class Game:
    def __init__(self):
        self.cards = create_cards()
        self.starter_decks = create_starter_decks(self.cards)
        self.store = Store(create_store_cards(self.cards))
        self.locations = create_locations(self.cards)
        self.player = None

    def create_player(self):
        os.system('cls')
        print("Bem-vindo ao Card RPG!")

        while True:
            name = input("Insira seu nome: ")
            if not name.isdigit():
                break
            print("Nome inválido!")
        
        print("Escolha seu deck inicial:")
        for i, deck in enumerate(self.starter_decks, 1):
            print(f"{i} - {deck}")

        while True:
            choice = input("Deck: ")
            if choice.isdigit() and 1 <= int(choice) <= len(self.starter_decks):
                chosen_deck = self.starter_decks[int(choice) - 1]
                break
            print("Escolha inválida!")

        self.player = Player(name, chosen_deck)
        print(f"Bem-vindo, {self.player.name}!")
    
    def manage_deck(self):
        while True:
            print("\nGerenciar Deck: LISTAR | DISCARTAR | LOJA | SAIR")
            choice = input("> ").upper()

            if choice == "SAIR":
                break
            elif choice == "LISTAR":
                self.player.show_deck()
            elif choice == "DISCARTAR":
                self.player.show_deck()
                choice = input("Qual carta descartar? ")
                if choice.isdigit():
                    idx = int(choice) - 1
                    if 0 <= idx < len(self.player.deck.cards):
                        card = self.player.deck.remove_card(idx)
                        print(f"Você recebeu {card.price} coins.")
                        self.player.coins += card.price
            elif choice == "LOJA":
                self.store.show()
                buy = input("Comprar qual carta? (numero ou SAIR): ").upper()
                if buy.isdigit():
                    index = int(buy) - 1
                    if 0 <= index < len(self.store.cards):
                        self.player.buy_card(self.store, index)

    def choose_location(self):
        print("\nLocais disponíveis:")
        for i, loc in enumerate(self.locations, 1):
            print(f"{i} - {loc.name}")

        while True:
            choice = input("Escolha o local: ")
            if choice.isdigit() and 1 <= int(choice) <= len(self.locations):
                return self.locations[int(choice) - 1]
            print("Escolha inválida!")

    def start_location(self):
        location = self.choose_location()
        combat = Combat(self.player, location)
        combat.start()

    def start(self):
        self.create_player()

        while True:
            print("\nEscolha: GERENCIAR | AVENTURA | SAIR")
            choice = input("> ").upper()

            if choice == "GERENCIAR":
                self.manage_deck()
            elif choice == "AVENTURA":
                self.start_location()
            elif choice == "SAIR":
                break


# Rodar o jogo
game = Game()
game.start()
