korkeus = int(input("Anna korkeus: "))

i = 0
while i < korkeus:
    print(" "*(korkeus-i) + 2*"*"*i + "*")
    i = i+1