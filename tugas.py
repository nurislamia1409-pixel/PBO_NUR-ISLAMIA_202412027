class Mahasiswa:

    universitas = "STITEK Bontang"

    def __init__(self, nama, nim, jurusan, ipk=0.0):
        
        self.nama, self.nim, self.jurusan, self.ipk = nama, nim, jurusan, ipk

    
    def perkenalan_diri(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan} di {Mahasiswa.universitas}")
        print(f"IPK saat ini: {self.ipk:.2f}")

    
    def update_ipk(self, ipk_baru):
        if 0.0 <= ipk_baru <= 4.0:
            self.ipk = ipk_baru
            print(f"SUCCESS: IPK {self.nama} berhasil diupdate menjadi {self.ipk:.2f}")
        else:
            print("ERROR: Nilai IPK tidak valid (harus antara 0.0 hingga 4.0)")


    def predikat_kelulusan(self):
    
        if self.ipk >= 3.5: predikat = "Cum Laude"
        elif self.ipk >= 3.0: predikat = "Sangat Memuaskan"
        elif self.ipk >= 2.5: predikat = "Memuaskan"
        elif self.ipk >= 2.0: predikat = "Lulus"
        else: predikat = "Belum Lulus"

        print(f"Predikat Kelulusan untuk {self.nama}: {predikat} (IPK: {self.ipk:.2f})")
        return predikat


print("---------------------------------------------")
print("DEMONSTRASI PROGRAM MAHASISWA OOP")
print("---------------------------------------------")

mhs_mia = Mahasiswa("mia", "202412027", "Teknik Informatika", 3.75)
mhs_sarah = Mahasiswa("sarah", "202412045", "Teknik Mesin", 2.89)
mhs_nana = Mahasiswa("nana", "202412050", "Teknik Elektro") 


print("\n--- Mahasiswa mia ---")
mhs_mia.perkenalan_diri()
mhs_mia.predikat_kelulusan()

print("\n--- Mahasiswa sarah (Update IPK) ---")
mhs_sarah.perkenalan_diri()
mhs_sarah.update_ipk(3.15) 
mhs_sarah.predikat_kelulusan()

print("\n--- Mahasiswa nana ---")
mhs_nana.perkenalan_diri() 
mhs_nana.predikat_kelulusan()
mhs_nana.update_ipk(2.65) 
mhs_nana.predikat_kelulusan()
print("---------------------------------------------")