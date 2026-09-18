class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        self.nykyinen_kerros += 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")


    def siirry_kerrokseen(self, haluttu_kerros):
        while self.nykyinen_kerros != haluttu_kerros:
            if self.nykyinen_kerros < haluttu_kerros:
                self.kerros_ylös()
            else:
                self.kerros_alas()

h = Hissi(1,10)
h.siirry_kerrokseen(8)
h.siirry_kerrokseen(1)