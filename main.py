
import csv

pokemons = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('pokemon.csv', newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='|')

    for row in file_reader:
        pokemons.append(row[0])

# print(pokemons)

print("Pokemon list command:")

while True:
    print("1. Get pokemon by sequence number")
    print("2. Sort by A-Z")
    print("3. Sort by Z-A")
    print("4. Search by name")
    print("5. Search by length of name")
    print("6 paginaciju")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        x = input("Numuri ieraksti:")
        print(pokemons[int(x)-1])
        pass
    elif choice == '2':
        pokemons.sort()
        print(pokemons)
        pass
    elif choice == '3':
        pokemons.sort(reverse = True)
        print(pokemons)
        pass
    elif choice == '4':
        name = input("Ko meklejat: ")
        newlist = [x for x in pokemons if name in x]
        print(newlist)
        pass
    elif choice == '5':
        name = input("Uzraksti length")
        newlist = [x for x in pokemons if int(name) == len(x)]
        print(newlist)
    elif choice == '6':
        print(pokemons[int(0)-1])
        print(pokemons[int(0)])
        print(pokemons[int(0)+1])
        print(pokemons[int(0)+2])
        print(pokemons[int(0)+3])
        print(pokemons[int(0)+4])
        print(pokemons[int(0)+5])
        print(pokemons[int(0)+6])
        print(pokemons[int(0)+7])
        print(pokemons[int(0)+8])
        x = input("Uzrakstiet n vai q")
        pass
    elif choice == '7':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 6")

    print("==========================")