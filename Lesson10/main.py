
text = None
with open("games.txt","r") as file:
    text = file.read()

games = text.split("\n")
print(games)


gameadding = input("Add a new Game: ").strip()

with open("games.txt","a") as file:
    file.write(f"\n{gameadding}")
print("Succes")

with open("games.txt","r") as file:
    text = file.read()
print(text)