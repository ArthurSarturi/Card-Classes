from classes import Card, Location

def create_cards():
    return {
        "sword": Card("Espada", "Vence Escudos e Adagas. Perde para Arco e Espada Grande", 5),
        "shield": Card("Escudo", "Vence Adagas e Arcos. Perde para Espada e Espada Grande", 5),
        "bow": Card("Arco", "Vence Espadas e Adagas. Perde para Escudo", 15),
        "greatsword": Card("Espada Grande", "Vence Espadas e Escudos. Perde para Arco", 30)
    }

def create_starter_decks(cards): 
    return [
        [cards["sword"], cards["shield"]],
        [cards["shield"], cards["sword"]]
    ]

def create_store_cards(cards):
    return [cards["bow"], cards["sword"], cards["shield"], cards["greatsword"]]

def create_locations(cards):
    return [
        Location(
            "Masmorra Sombria",
            "Carrasco Imaculado",
            [cards["sword"], cards["shield"]],
            2,
            10
        ),
        Location(
            "Castelo Sombrio",
            "Rei Perdido",
            [cards["sword"], cards["greatsword"]],
            5,
            40
        ),
        Location(
            "Floresta Negra",
            "Urso Ancião",
            [cards["shield"], cards["sword"]],
            3,
            20
        )
    ]
