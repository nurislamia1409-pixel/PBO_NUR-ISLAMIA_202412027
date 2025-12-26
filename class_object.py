class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def perkenalan(self):
        return f"Halo, saya {self.nama} dengan NIM {self.nim}"
    
# Pembuatan object
mhs1 = Mahasiswa("Rianindya chandra hardika,S.T.,M.Eng", "TI001")
mhs2 = Mahasiswa("Ir.Abadi Nugroho, M.Kom", "TI002")

print(mhs1.perkenalan())
print(mhs2.perkenalan())