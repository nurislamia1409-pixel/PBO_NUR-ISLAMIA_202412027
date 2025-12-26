from abc import ABC, abstractmethod
import math

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass


class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * (self.jari_jari ** 2)

    def keliling(self):
        return 2 * math.pi * self.jari_jari


class PersegiPanjang(Bentuk):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)


class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

    def keliling(self):
        return 4 * self.sisi


# Contoh penggunaan
lingkaran = Lingkaran(5)
persegi_panjang = PersegiPanjang(4, 3)
persegi = Persegi(6)

print(f"Luas Lingkaran: {lingkaran.luas():.2f}")
print(f"Keliling Lingkaran: {lingkaran.keliling():.2f}")

print(f"Luas Persegi Panjang: {persegi_panjang.luas()}")
print(f"Keliling Persegi Panjang: {persegi_panjang.keliling()}")

print(f"Luas Persegi: {persegi.luas()}")
print(f"Keliling Persegi: {persegi.keliling()}")