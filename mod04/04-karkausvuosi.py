vuosi = int(input("Kerro vuosiluku:\n"))
print()

if vuosi%4 == 0:
    if vuosi%100 == 0:
        if vuosi%400 == 0:
            print("Vuosi on karkausvuosi.")
        else:
            print("Vuosi ei ole karkausvuosi.")
    else:
        print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")

