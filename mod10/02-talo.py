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

class Talo():
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []

        while len(self.hissit) < hissien_lkm:
            self.hissit.append(Hissi(self.alin_kerros, self.ylin_kerros))

    def aja_hissiä(self, hissin_nro, kohde_kerros):
        self.hissit[hissin_nro-1].siirry_kerrokseen(kohde_kerros)

hökkeli = Talo(1, 7, 3)
hökkeli.aja_hissiä(1, 4)