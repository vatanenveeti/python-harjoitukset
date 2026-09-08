luvut = []
luku = input("Anna luku: ")

while luku != "":
    luku = float(luku)
    luvut.append(luku)
    luku = input("Anna uusi luku: ")

luvut.sort(reverse=True)
for i in range(5):
    print(luvut[i])