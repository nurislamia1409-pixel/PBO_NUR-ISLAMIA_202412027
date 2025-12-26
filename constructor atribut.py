class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    # Method to show info
    def info(self):
        return f"{self.merk} - {self.warna} ({self.tahun})"


# Create objects
k1 = Kendaraan("Toyota Avanza", "Hitam", 2020)
k2 = Kendaraan("Honda Beat", "Merah", 2022)

print("=== Instance Attribute ===")
print(k1.info())
print(k2.info())

print("\n=== Class Attribute ===")
print(k1.bahan_bakar)
print(k2.bahan_bakar)
print(Kendaraan.bahan_bakar)