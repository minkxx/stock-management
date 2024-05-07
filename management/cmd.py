import colorama

from management.store import add_data, update_data, delete_data, display_all_data

colorama.init(autoreset=True)

while True:
    print(f"{colorama.Fore.MAGENTA}***** Welcome to Stock Management Software *****")
    print(
        f"""{colorama.Fore.BLUE}
1. Add Items          2. Update Quantity
3. Display Items      4. Delete Item     
5. Exit"""
    )
    choice = int(input(": "))
    if choice == 1:
        name = input("Enter Item Name : ")
        quant = int(input("Enter Item Quantity : "))
        add_data(item_name=name, quantity=quant)
    elif choice == 2:
        pass
    elif choice == 3:
        display_all_data()
    elif choice == 4:
        name = input("Enter Item Name : ")
        delete_data(item_name=name)
    elif choice == 5:
        exit()
    else:
        print("Invalid choice!")
        break
