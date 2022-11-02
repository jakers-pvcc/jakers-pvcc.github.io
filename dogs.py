# Joshua C. Akers
# PP: DOOGSLAYER

dogs = ["Sadie", "Molly", "Ella", "Milo", "Buddy", "Rocky", "AnnaBelle", "Gonzo", "Sweetie-Pie", "Diego"]

dogs2 = []

def main():
    how_many = len(dogs)
    print("\nNumber of doggos in the list: " + str(how_many))
    print("\nOriginal list of doggo names:")
    print(dogs)

    dogs.reverse()
    print("\nList from last to first:")
    print(dogs)

    dogs.sort()
    print("\nAlphabetized List:")
    print(dogs)

    dogs.sort(reverse = True)
    print("\nList in reverse alphabetized order:")
    print(dogs)

    dogs.append("Ranger")
    print("\nAdd a doggo to the end of the list:")
    print(dogs)

    doggo = dogs.pop(0)
    print("\nPop a doggo off from the front of the list:")
    print(dogs)
    print(Doggo + "was removed from the front of the list.")

    another_dog = dogs.pop(3)
    print("\nNote: Position numbers in a list begin with 0, not with 1.")
    print("Pop a doggo off from position 3 (which is the 4th doggo) on the list:")
    print(dogs)
    print(another_dog + "was removed from position 3 of the list.")

    dogs.remove('AnnaBelle')
    print("\nRemove a doggo by name rather than the list:")
    print(dogs)

    dogs2 = dogs
    print("\nA list can be copied into another list by setting one equal to the other:")
    print(dogs)
    print(dogs2)

    print("\nUse a FOR LOOP to give each doggo in the list the same last name:")
    for i in range(len(dogs)):
        dogs[i] = dogs[i] + " Akers"

# Execution
main()
