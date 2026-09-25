class Hissi:
    def __init__(self, alin_kerros, ylin_kerros, hissi_nro):
        self.hissi_nro = hissi_nro
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        self.nykyinen_kerros += 1
        if self.nykyinen_kerros > self.ylin_kerros:
            self.nykyinen_kerros = self.ylin_kerros
        print(f"Hissi {self.hissi_nro} on kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        if self.nykyinen_kerros < self.alin_kerros:
            self.nykyinen_kerros = self.alin_kerros
        print(f"Hissi {self.hissi_nro} on kerroksessa {self.nykyinen_kerros}")


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

        i = 1
        while len(self.hissit) < hissien_lkm:
            self.hissit.append(Hissi(self.alin_kerros, self.ylin_kerros, i))
            i += 1

    def aja_hissiä(self, hissin_nro, kohde_kerros):
        self.hissit[hissin_nro-1].siirry_kerrokseen(kohde_kerros)

    def palohälytys(self):
        i = 1
        for hissi in self.hissit:
            self.aja_hissiä(i, self.alin_kerros)
            i += 1

hökkeli = Talo(1, 7, 3)
hökkeli.aja_hissiä(1, 4)
hökkeli.aja_hissiä(2, 7)
hökkeli.aja_hissiä(3, 5)

hökkeli.palohälytys()