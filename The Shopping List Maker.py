def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"'{item}' has been added to the list.")

# Task 2: 

def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the list.")
    else:
        print(f"'{item}' is not in the list.")

# Task 3:

def print_list(shopping_list):
    if shopping_list:
        print("\nShopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("The shopping list is empty.")
        
def shopping_list_program():
    shopping_list = []
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Quit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(shopping_list, item)
        
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(shopping_list, item)
        
        elif choice == '3':
            print_list(shopping_list)
        
        elif choice == '4':
            print("Thanks for using the shopping list program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    shopping_list_program()