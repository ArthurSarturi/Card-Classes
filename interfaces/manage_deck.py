def manage_deck(player, store):
    while True:
        print("\nGerenciar Deck: LISTAR | DISCARTAR | LOJA | SAIR")
        choice = input("> ").upper()

        if choice == "SAIR":
            break

        elif choice == "LISTAR":
            player.show_deck()

        elif choice == "DISCARTAR":
            player.show_deck()
            choice = input("Qual carta descartar? ")
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(player.deck.cards):
                    card = player.deck.remove_card(idx)
                    print(f"Você recebeu {card.price} coins.")
                    player.coins += card.price

        elif choice == "LOJA":
            store.show()
            buy = input("Comprar qual carta? (numero ou SAIR): ").upper()
            if buy.isdigit():
                index = int(buy) - 1
                if 0 <= index < len(store.cards):
                    player.buy_card(store, index)
