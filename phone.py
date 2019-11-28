def print_menu():
    print('1. lista alla nummer')
    print('2. lägg till nummer')
    print('3. ta bort nummer')
    print('4. kolla upp ett nummer')
    print('5. avsluta')
    print()

numbers = {}
menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("skriv in nummer (1-5): "))
    if menu_choice == 1:
        print("Telefon Nummer:")
        for x in numbers.keys():
            print("Namn: ", x, "\tNummer:", numbers[x])
        print()
    elif menu_choice == 2:
        print("lägg till name och nummer")
        name = input("Namn: ")
        phonenumber = input("Nummer: ")
        numbers[name] = phonenumber
    elif menu_choice == 3:
        print("Remove Name and Number")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "hittades inte")
    elif menu_choice == 4:
        print("kolla upp nummer")
        name = input("Namn: ")
        if name in numbers:
            print("nummret är", numbers[name])
        else:
            print(name, "hittades inte")
    elif menu_choice != 5:
        print_menu()