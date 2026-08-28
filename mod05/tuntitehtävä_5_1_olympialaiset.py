vuosi = int(input("Anna vuosi: "))
while vuosi >= 1896:
    if vuosi % 4 == 0 or vuosi == 2021:
        if vuosi == 2020 or vuosi == 1916 or vuosi == 1940 or vuosi == 1944:
            print(f"{vuosi} ei ole olympiavuosi.")
        else:
            print(f"{vuosi} on olympiavuosi.")
    else:
        print(f"{vuosi} ei ole olympiavuosi.")
    vuosi = int(input("Anna uusi vuosi: "))
print("Ohjelma lopetettu, liian pieni vuosi annettu")