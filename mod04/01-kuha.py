pituus = float(input("Anna kuhan pituus senttimetreinä:\n"))

if pituus < 37:
    puuttuu = 37 - pituus
    print(f"\nKuha täytyy laskea takaisin järveen. Kuha on {puuttuu:.1f} cm alle sallitun pyyntimitan.")
