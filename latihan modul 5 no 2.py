# a. Class Pelanggan
class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

    def info(self):
        return f"ID: {self.id_pelanggan}, Nama: {self.nama}, Email: {self.email}"


# b. Dictionary untuk menyimpan objek pelanggan
data_pelanggan = {}


# c. Fungsi menambah pelanggan
def tambah_pelanggan(id_pelanggan, nama, email):
    if id_pelanggan in data_pelanggan:
        print("ID pelanggan sudah ada.")
    else:
        data_pelanggan[id_pelanggan] = Pelanggan(id_pelanggan, nama, email)
        print("Pelanggan berhasil ditambahkan.")


# c. Fungsi menghapus pelanggan
def hapus_pelanggan(id_pelanggan):
    if id_pelanggan in data_pelanggan:
        del data_pelanggan[id_pelanggan]
        print("Pelanggan berhasil dihapus.")
    else:
        print("Pelanggan tidak ditemukan.")


# c. Fungsi mencari pelanggan
def cari_pelanggan(id_pelanggan):
    if id_pelanggan in data_pelanggan:
        return data_pelanggan[id_pelanggan]
    else:
        return None


# d. Menampilkan seluruh daftar pelanggan
def tampilkan_semua_pelanggan():
    print("\n=== Daftar Pelanggan ===")
    if not data_pelanggan:
        print("Data pelanggan kosong.")
    else:
        for pelanggan in data_pelanggan.values():
            print(pelanggan.info())


# ------------------ UJI PROGRAM ------------------
tambah_pelanggan("C001", "Andi", "andi@email.com")
tambah_pelanggan("C002", "Budi", "budi@email.com")
tambah_pelanggan("C003", "Siti", "siti@email.com")

tampilkan_semua_pelanggan()

hasil = cari_pelanggan("C002")
if hasil:
    print("\nPelanggan ditemukan:")
    print(hasil.info())
else:
    print("\nPelanggan tidak ditemukan.")

hapus_pelanggan("C001")

tampilkan_semua_pelanggan()