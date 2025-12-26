class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def info_gaji(self):
        return f"Karyawan: {self.nama}, Gaji Pokok: {self.gaji_pokok}"


class Manager(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan

    def info_gaji(self):
        total = self.gaji_pokok + self.tunjangan
        return f"Manager: {self.nama}, Total Gaji: {total}"


class Programmer(Karyawan):
    def __init__(self, nama, gaji_pokok, bonus):
        super().__init__(nama, gaji_pokok)
        self.bonus = bonus

    def info_gaji(self):
        total = self.gaji_pokok + self.bonus
        return f"Programmer: {self.nama}, Total Gaji: {total}"


class Departemen:
    def __init__(self, nama_dept):
        self.nama_dept = nama_dept
        self.karyawan_list = []

    def tambah_karyawan(self, karyawan):
        self.karyawan_list.append(karyawan)

    def tampilkan_karyawan(self):
        print(f"Daftar Karyawan di Departemen {self.nama_dept}:")
        for k in self.karyawan_list:
            print(k.info_gaji())


# Instansiasi
m1 = Manager("Mia", 5000000, 2000000)
m2 = Manager("Nana", 5500000, 2500000)

p1 = Programmer("Sarah", 4500000, 1500000)
p2 = Programmer("Ainun", 4800000, 1200000)

dept = Departemen("Teknologi Informasi")

dept.tambah_karyawan(m1)
dept.tambah_karyawan(m2)
dept.tambah_karyawan(p1)
dept.tambah_karyawan(p2)

dept.tampilkan_karyawan()