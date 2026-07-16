
games = [
    "League of Legends",
    "Forza Horizon 6",
    "Grand Theft Auto 6",
    "Meccha Chameleon"
 ]

for game in games:
    print(f"I like {game}.")

new_game = input("Enter another game: ")

games.append(new_game)

print("\nUpdated game list:")

for game in games:
    print(f"I like {game}.")