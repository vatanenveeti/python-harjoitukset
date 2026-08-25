import random

luku = random.randint(1,10)
arvaus = int(input("Arvaa luku väliltä 1-10:\n"))

while luku != arvaus:
    if arvaus > luku:
        print("\nLiian suuri arvaus")
    else:
        print("\nLiian pieni arvaus")
    arvaus = int(input("Arvaa uudelleen\n"))
else:
    print("Oikein")
