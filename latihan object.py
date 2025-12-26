class Dosen:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def perkenalan(self):
        return f"Halo, saya {self.nama} dengan NIM {self.nim}"

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"{self.nama} mengajar mata kuliah {mata_kuliah}"


# Pembuatan object
mhs1 = Dosen("Rianindya chandra hardika,S.T.,M.Eng", "TI001")
mhs2 = Dosen("Ir.Abadi Nugroho, M.Kom", "TI002")

print(mhs1.perkenalan())
print(mhs2.perkenalan())

print(mhs1.ajar_mata_kuliah("sistem basis data"))
print(mhs2.ajar_mata_kuliah("pemikiran desain"))
