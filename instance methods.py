class ManajerInventori:
    def __init__(self):
        self.inventori = {}

    def tambah_barang(self, nama, jumlah):
        if jumlah > 0:
            self.inventori[nama] = self.inventori.get(nama, 0) + jumlah
            return f"Berhasil menambah {jumlah} {nama}. Total: {self.inventori[nama]}"
        return "Jumlah harus positif"

    def hapus_barang(self, nama, jumlah):
        if nama in self.inventori and jumlah > 0:
            if jumlah <= self.inventori[nama]:
                self.inventori[nama] -= jumlah
                return f"Berhasil menghapus {jumlah} {nama}. Sisa: {self.inventori[nama]}"
            return "Jumlah yang dihapus melebihi stok"
        return "Barang tidak ditemukan"

    def lihat_inventori(self):
        return self.inventori


# Testing
inv = ManajerInventori()

print("=== Tambah Barang ===")
print(inv.tambah_barang("Pensil", 10))
print(inv.tambah_barang("Buku", 5))

print("\n=== Hapus Barang ===")
print(inv.hapus_barang("Pensil", 3))

print("\n=== Lihat Inventori ===")
print(inv.lihat_inventori())