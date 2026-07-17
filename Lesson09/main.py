

def print_game(game):
    for key, data in game.items():
        print(f"{key}: {data}")
    print()

games = [
    {
        "name" : "Rust",
        "price" : 25.0,
        "platform" : "PC"
    },
        {
        "name" : "Forza6",
        "price" : 40.0,
        "platform" : "All"
    },
        {
        "name" : "GtaV",
        "price" : 30.0,
        "platform" : "All"
    },

]
for game in games:
    print_game(game)


choice = input("Which game do you want to change? ").strip()
found = None
old_price = 0
for game in games:
    if game["name"].casefold() == choice.casefold():
        found = game
        old_price = game["price"]
        game["price"] = float(input("What's the new price? "))
        break
    

if found is None:
    print("Game is not found")
else:
    print(f"{found['name']}'s price was changed from {old_price} to {found['price']} Euro.")
    for game in games:
        print_game(game)
        

