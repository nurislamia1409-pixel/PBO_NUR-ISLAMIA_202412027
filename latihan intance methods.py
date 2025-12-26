class ManajerInventori:
    """
    Class untuk mengelola inventori barang.
    Setiap barang disimpan sebagai pasangan (nama_barang: jumlah).
    """

    def __init__(self):
        # Instance attribute: menggunakan dictionary untuk menyimpan inventori {nama_barang: jumlah}
        self.inventori = {}

    def tambah_barang(self, nama_barang, jumlah):
        """
        Method untuk MENAMBAH jumlah barang ke inventori.
        Jika barang sudah ada, stoknya diperbarui. Jika belum, barang ditambahkan.
        """

        if jumlah > 0:
            # Menggunakan .get() untuk mendapatkan jumlah stok saat ini (atau 0 jika barang baru)
            self.inventori[nama_barang] = self.inventori.get(nama_barang, 0) + jumlah
            print(f"Berhasil menambahkan {jumlah} unit {nama_barang}. Stok saat ini: {self.inventori[nama_barang]}")
        else:
            print("Jumlah barang yang ditambahkan harus positif.")

    def hapus_barang(self, nama_barang, jumlah):
        """
        Method untuk MENGURANGI jumlah barang (mengambil/menjual) dari inventori.
        Melakukan pengecekan ketersediaan stok.
        """

        if nama_barang not in self.inventori:
            print(f"Barang {nama_barang} tidak ada dalam inventori.")
            return

        if jumlah > 0:
            stok_saat_ini = self.inventori[nama_barang]

            if stok_saat_ini >= jumlah:
                self.inventori[nama_barang] -= jumlah
                print(f"Berhasil mengurangi {jumlah} unit {nama_barang}. Stok tersisa: {self.inventori[nama_barang]}")

                # Opcional: Hapus item dari dictionary jika stoknya menjadi nol
                if self.inventori[nama_barang] == 0:
                    del self.inventori[nama_barang]
                    print(f"Barang {nama_barang} habis dan dihapus dari inventori.")
            else:
                print(f"Gagal mengurangi. Stok {nama_barang} tidak mencukupi. Tersedia: {stok_saat_ini}")
        else:
            print("Jumlah barang yang dihapus harus positif.")

    def lihat_inventori(self):
        """Menampilkan semua barang dan jumlahnya di inventori."""

        if not self.inventori:
            print("\nInventori kosong.")
            return

        print("\n--- Daftar Inventori ---")
        for barang, jumlah in self.inventori.items():
            print(f"- {barang}: {jumlah} unit")
        print("------------------------")

# Tambahan: Contoh Penggunaan (Opsional)
if __name__ == '__main__':
    gudang = ManajerInventori()

    print("\n--- TEST PENAMBAHAN ---")
    gudang.tambah_barang("Laptop", 15)
    gudang.tambah_barang("Mouse", 50)
    gudang.tambah_barang("Laptop", 5) # Menambah stok yang sudah ada
    gudang.lihat_inventori()

    print("\n--- TEST PENGURANGAN ---")
    gudang.hapus_barang("Laptop", 20) # Habis dan dihapus
    gudang.hapus_barang("Mouse", 10)
    gudang.hapus_barang("Mouse", 50) # Stok tidak cukup
    gudang.hapus_barang("Keyboard", 5) # Barang tidak ada
    gudang.hapus_barang("Mouse", -1) # Jumlah negatif

    gudang.lihat_inventori()