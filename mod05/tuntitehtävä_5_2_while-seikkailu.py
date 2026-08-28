print("Olet menossa autokilpailuun.")
kulkuneuvo = input("Valitse kulkuneuvo: ")
kulkuneuvo = kulkuneuvo.lower()
valinnat = 0

while kulkuneuvo != "formula":

    print("Ootko nyt ihan varma päätöksestäsi?")
    valinnat = valinnat + 1
    if valinnat >= 5:
        print("Et osannut valita sopivaa kulkuneuvoa, joten juokset.\nHäviät kilpailun.")
        break
    kulkuneuvo = input("Valitse nyt kuitenkin uudestaan: ")
    kulkuneuvo = kulkuneuvo.lower()
else:
    print("Hyvä! Formulalla voittaa varmasti.")

    kaasu = input("Painatko kilpailussa kaasua? Valitse kyllä tai ei: ")
    while not (kaasu == "kyllä" or kaasu == "ei"):
        kaasu = input('Anna vastaus muodossa "kyllä" tai "ei" ')
    if kaasu == "kyllä":
        print("Voitit kilpailun.")
    else:
        print("Hävisit kilpailun.")
