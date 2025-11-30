from classes import Location, Combat

def choose_location(locations):
    print("\nLocais disponíveis:")
    for i, loc in enumerate(locations, 1):
        print(f"{i} - {loc.name}")

    while True:
        choice = input("Escolha o local: ")
        if choice.isdigit() and 1 <= int(choice) <= len(locations):
            return locations[int(choice) - 1]
        print("Escolha inválida!")


def start_location(player, locations):
    location = choose_location(locations)
    combat = Combat(player, location)
    combat.start()
