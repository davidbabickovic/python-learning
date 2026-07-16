def print_list(items):
    for number, item in enumerate(items, start=1):
        print(f"{number}. {item}")

shopping_list = ["Bread", "Apple", "Rice"]
print("\nShopping List")
print_list(shopping_list)

new_item = input("\nAdd a new item: ").strip()

shopping_list.append(new_item)

print("\nNew List")
print_list(shopping_list)

item_to_remove = input("\nWhat do you want to delete? ").strip()


found_item = None
for item in shopping_list:
    if item.casefold() == item_to_remove.casefold():
        found_item = item
        break
    
if found_item is not None:
    shopping_list.remove(found_item)
    print("\nNew List")
    print_list(shopping_list)
else:
    print(f"{item_to_remove} is not in the list.")










