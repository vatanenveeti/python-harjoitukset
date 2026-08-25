lampo = float(input("Syötä lämpötila:\n"))

if lampo < 0:
    print("\nKylmä\n")
    sää_lampo = "kylmä"
else:
    print("\nLämmin\n")
    sää_lampo = "lämmin"

pisteet = float(input("Syötä opintopisteet:\n"))

if pisteet >= 150:
    print("\nPaljon pisteitä\n")
else:
    print("\nVähän pisteitä\n")

sää = input("Onko sää pilvinen tai aurinkoinen?\n")

if sää_lampo == "lämmin" and sää == "pilvinen":
    print("\nJee\n")
else:
    print("\nHöh\n")

kala_ika = float(input("Kalan ikä:\n"))
kalan_koko = float(input("\nKalan koko(cm):\n"))
if 10 < kala_ika <= 65 or kala_ika > 10:
    print("\nKala on sopiva ja/tai vanha\n")
else:
    print("\nEi hyvä\n")

