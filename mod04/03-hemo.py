sukupuoli = input("Oletko mies vai nainen?\n")
h_arvo = float(input("\nMikä on hemoglobiiniarvosi(g/l)?\n"))
print()

if sukupuoli == "nainen":
    if h_arvo > 175:
        print("Hemoglobiiniarvosi on korkea.")
    elif h_arvo >= 117:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on alhainen.")
elif sukupuoli == "mies":
    if h_arvo > 195:
        print("Hemoglobiiniarvosi on korkea.")
    elif h_arvo >= 134:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on alhainen.")
else:
    print('Kirjoita sukupuoli muodossa "mies" tai "nainen"')

            