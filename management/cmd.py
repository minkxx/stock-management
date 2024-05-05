import colorama

colorama.init(autoreset=True)

while True:
    print(f"{colorama.Fore.MAGENTA}***** Welcome to Stock Management Software *****")
    print(f'''{colorama.Fore.BLUE}
1. Add Items          2. Remove Items
3. Display Items      4. Exit''')
    choice = int(input(": "))
    if choice == 4:
        exit()