ika = float(input("Kerro ikäsi:\n"))
laji = input("Oletko ihminen, tonttu, robotti vai jokin muu?\n")

print("\nVoit tilata:\nkahvia")

if ika >= 18 and laji == "ihminen":
    print("viiniä")

if ika >= 100 and laji == "tonttu":
    print("olutta")

if laji == "robotti":
    print("öljyä")