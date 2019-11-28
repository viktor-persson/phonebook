def print_meny():
    print('1. lista alla nummer')
    print('2. lägg till nummer')
    print('3. ta bort nummer')
    print('4. kolla upp ett nummer')
    print('5. avsluta')
    print()

nummer = {}
meny_val = 0
print_meny()
while meny_val != 5:
    meny_val = int(input("skriv in nummer (1-5): "))
    if meny_val == 1:
        print("Telefon Nummer:")
        for x in nummer.keys():
            print("Namn: ", x, "\tNummer:", numbers[x])
        print()
    elif meny_val == 2:
        print("lägg till namn och nummer")
        namn = input("Namn: ")
        telefonnummer = input("Nummer: ")
        nummer[namn] = telefonnummer
    elif meny_val == 3:
        print("Remove Name and Number")
        namn = input("Name: ")
        if namn in nummer:
            del nummer[namn]
        else:
            print(namn, "hittades inte")
    elif meny_val == 4:
        print("kolla upp nummer")
        namn = input("Namn: ")
        if namn in nummer:
            print("nummret är", nummer[namn])
        else:
            print(namn, "hittades inte")
    elif meny_val != 5:
        print_meny()