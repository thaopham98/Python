def display_menu(menu):
  """Prints the menu items and their prices."""
  print("--- Menu ---")
  for item, price in menu.items():
    print(f"{item}: ${price:.2f}")  # f-string for formatted output

def edit_menu(number, menu):
  """Edits the menu based on the user's choice."""
  if number == 1:
    # Insert new item
    item = input("\nEnter a new item: ")
    price = float(input("Enter a new price: "))
    menu[item] = price
    display_menu(menu)
  elif number == 2:
    # Edit item price
    item = input("\nEnter the item's name: ")
    if item in menu:
      price = float(input("Enter a new price: "))
      menu[item] = price
      display_menu(menu)
    else:
      print(f"Item '{item}' not found in the menu.")
  elif number == 3:
    # Delete an item (not implemented yet)
    print("\n**Deleting functionality not implemented yet**")
  else:
    print("\nInvalid choice.")

# Create the menu dictionary
menu = {
  "Cheesecake": 6.99,
  "Croissant": 1.99,
  "Strawberry Short Cake": 6.99,
  "Cupcake": 1.99,
}

def main():
    display_menu(menu)

    # Owner menu interaction
    choice = input("\nDo you want to change anything in the menu? (y/n): ").lower()
    while choice == 'y':
        print("\nWhat do you want to change?")
        print("\n1. Insert new item.")
        print("\n2. Change an item price.")
        print("\n3. Delete an item (not implemented yet).")
        number = int(input("\nPlease select a number: "))

        edit_menu(number, menu)

        choice = input("\n\nDo you want to change anything else in the menu? (y/n): ").lower()

    # Customer menu interaction (not implemented yet)
    # print("\nPlease select a number: ")
# ... (customer interaction logic here)

if __name__ == "__main__":
    main()