from classes import Location, Combat
from typing import List

def choose_location(locations : List[Location]):
    print("\nLocais disponíveis:")
    for i, location in enumerate(locations, 1):
        print(f"{i} - {location.name}")

    while True:
        try:
            choice = int(input("Escolha o local: "))
            return locations[choice - 1]
        except (ValueError, IndexError):
            print("Escolha inválida!")


def start_location(player, locations):
    location = choose_location(locations)
    combat = Combat(player, location)
    combat.start()
