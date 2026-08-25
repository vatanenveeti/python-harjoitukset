oikea_tunnus = "python"
oikea_salasana = "rules"
yritykset = 0
tunnus = input("Syötä käyttäjätunnus: ")
salasana = input("Syötä salasana: ")

while tunnus != oikea_tunnus and salasana != oikea_salasana:
    yritykset = yritykset + 1
    if yritykset >= 5:
            print("Pääsy evätty")
            break
    
    print("Yritä uudelleen\n")
    tunnus = input("Syötä käyttäjätunnus: ")
    salasana = input("Syötä salasana: ")
    
else:
    print("Tervetuloa")
