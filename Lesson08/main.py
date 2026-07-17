



def print_game2(game):

    for key, data in game.items():
        print(f"{key}: {data}")
    print()
    
game = {
    "name" : "Rust",
    "price" : 25.0,
    "genre" : "Survival"
}

print_game2(game)

game["price"] = float(input("Enter a new price: "))

print_game2(game)

game["platform"] = input ("Enter the platform from the game: ").strip()

print_game2(game)
