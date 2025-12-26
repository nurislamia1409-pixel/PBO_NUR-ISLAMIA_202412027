# Class induk
class Bentuk:
    def luas(self):
        return 0

# Class turunan Persegi
class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

# Class turunan Lingkaran
class Lingkaran(Bentuk):
    def __init__(self, r):
        self.r = r

    def luas(self):
        return 3.14 * self.r * self.r

# Uji pemanggilan
b = Bentuk()
p = Persegi(4)
l = Lingkaran(7)

print("Luas Bentuk =", b.luas())
print("Luas Persegi =", p.luas())
print("Luas Lingkaran =", l.luas())