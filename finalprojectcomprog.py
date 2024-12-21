inventory = {}

def get_valid_input(prompt, required=True, input_type=str):
   
    while True:
        user_input = input(prompt).strip()
        if required and not user_input:  # Check for blank input
            print("Input cannot be empty. Please try again.")
            continue
        if not required and not user_input:
            return None  # Allow blank input for optional fields
        try:
            return input_type(user_input)  # Convert to the required type
        except ValueError:
            print(f"Invalid input! Please enter a valid {input_type.__name__}.")
            continue

def add_item(name, quantity, price):
    if name in inventory:
        inventory[name]['quantity'] += quantity  # If item exists, increase the quantity
    else:
        inventory[name] = {'quantity': quantity, 'price': price}  # Add new item
    print(f"Added {quantity} units of {name} at ${price:.2f} each.")

def update_item(name, quantity=None, price=None):
    if name in inventory:
        if quantity is not None:
            inventory[name]['quantity'] = quantity  # Update quantity if provided
        if price is not None:
            inventory[name]['price'] = price  # Update price if provided
        print(f"Updated {name}: {inventory[name]['quantity']} units, ${inventory[name]['price']:.2f} each.")
    else:
        print(f"{name} not found in inventory.")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nInventory List:")
        for item, details in inventory.items():
            print(f"{item}: {details['quantity']} units, ${details['price']:.2f} each")
    print("\n")

def remove_item(name):
    if name in inventory:
        del inventory[name]
        print(f"Removed {name} from inventory.")
    else:
        print(f"{name} not found in inventory.")

def search_item(name):
    if name in inventory:
        print(f"Found {name}: {inventory[name]['quantity']} units, ${inventory[name]['price']:.2f} each")
    else:
        print(f"{name} not found in inventory.")

def main():
    while True:
        print("\nInventory Management Menu:")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Remove Item")
        print("4. Update Item")
        print("5. Search Item")
        print("6. Exit")
        
        choice = get_valid_input("Enter your choice (1-6): ", required=True)

        if choice == '1':
            name = get_valid_input("Enter item name: ", required=True)
            quantity = get_valid_input("Enter quantity: ", required=True, input_type=int)
            price = get_valid_input("Enter price per unit: ", required=True, input_type=float)
            add_item(name, quantity, price)
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            name = get_valid_input("Enter item name to remove: ", required=True)
            remove_item(name)
        elif choice == '4':
            name = get_valid_input("Enter item name to update: ", required=True)
            quantity = get_valid_input("Enter new quantity (press Enter to skip): ", required=False, input_type=int)
            price = get_valid_input("Enter new price (press Enter to skip): ", required=False, input_type=float)
            update_item(name, quantity, price)
        elif choice == '5':
            name = get_valid_input("Enter item name to search: ", required=True)
            search_item(name)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
