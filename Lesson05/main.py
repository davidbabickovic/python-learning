

shopping_list =["Bread", "Apple", "Rice"]

new_item = input("What do you want to add? ").strip()
shopping_list.append(new_item)

print("\nShoppinglist:")

for number, item in enumerate(shopping_list, start=1):
    print(f"{number}. {item}")

item_to_remove = input("What do you want to remove? ").strip()

found_item = None

for item in shopping_list:
    if item.casefold() == item_to_remove.casefold():
        found_item = item
        break

if found_item is not None:
    shopping_list.remove(found_item)

    print("\nUpdated shoping list:")

    for number, item in enumerate(shopping_list, start=1):
        print(f"{number}. {item}")
else:
    print(f"{item_to_remove} is not in the list.")

