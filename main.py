from classes import Store
from seed import create_cards, create_locations, create_starter_decks, create_store_cards
from interfaces.create_player import create_player
from interfaces.manage_deck import manage_deck
from interfaces.locations import start_location

class Game:
    def __init__(self):
        self.cards = create_cards()
        self.starter_decks = create_starter_decks(self.cards)
        self.store = Store(create_store_cards(self.cards))
        self.locations = create_locations(self.cards)
        self.player = None

    def start(self):
        self.player = create_player(self.starter_decks)

        while True:
            print("\nEscolha: GERENCIAR | AVENTURA | SAIR")
            choice = input("> ").upper()
            if choice == "GERENCIAR":
                manage_deck(self.player, self.store)
            elif choice == "AVENTURA":
                start_location(self.player, self.locations)
            elif choice == "SAIR":
                break

game = Game()
game.start()
