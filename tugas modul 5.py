import tkinter as tk
from tkinter import ttk, messagebox, filedialog


# =======================
# CLASS MAHASISWA
# =======================
class Mahasiswa:
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk

    def info(self):
        return f"{self.nim} | {self.nama} | {self.jurusan} | IPK: {self.ipk}"

    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru


# =======================
# APLIKASI GUI
# =======================
class AplikasiMahasiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Manajemen Mahasiswa")
        self.root.geometry("800x500")

        # Dictionary mahasiswa (NIM sebagai key)
        self.data_mahasiswa = {}

        # =======================
        # FRAME INPUT
        # =======================
        frame_input = tk.LabelFrame(root, text="Input Data Mahasiswa", padx=10, pady=10)
        frame_input.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(frame_input, text="NIM").grid(row=0, column=0)
        tk.Label(frame_input, text="Nama").grid(row=0, column=2)
        tk.Label(frame_input, text="Jurusan").grid(row=1, column=0)
        tk.Label(frame_input, text="IPK").grid(row=1, column=2)

        self.entry_nim = tk.Entry(frame_input)
        self.entry_nama = tk.Entry(frame_input)
        self.entry_jurusan = tk.Entry(frame_input)
        self.entry_ipk = tk.Entry(frame_input)

        self.entry_nim.grid(row=0, column=1, padx=5)
        self.entry_nama.grid(row=0, column=3, padx=5)
        self.entry_jurusan.grid(row=1, column=1, padx=5)
        self.entry_ipk.grid(row=1, column=3, padx=5)

        # =======================
        # FRAME BUTTON
        # =======================
        frame_button = tk.Frame(root, pady=5)
        frame_button.pack()

        tk.Button(frame_button, text="Tambah", command=self.tambah).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_button, text="Update IPK", command=self.update).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_button, text="Hapus", command=self.hapus).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_button, text="Tampilkan Semua", command=self.tampilkan_semua).pack(side=tk.LEFT, padx=5)

        # =======================
        # FRAME SEARCH & FILTER
        # =======================
        frame_search = tk.LabelFrame(root, text="Cari & Filter", padx=10, pady=5)
        frame_search.pack(fill=tk.X, padx=10)

        tk.Label(frame_search, text="Cari (NIM / Nama):").grid(row=0, column=0)
        self.entry_cari = tk.Entry(frame_search)
        self.entry_cari.grid(row=0, column=1, padx=5)

        tk.Button(frame_search, text="Cari", command=self.cari).grid(row=0, column=2, padx=5)

        tk.Label(frame_search, text="Filter Jurusan:").grid(row=0, column=3)
        self.entry_filter = tk.Entry(frame_search)
        self.entry_filter.grid(row=0, column=4, padx=5)

        tk.Button(frame_search, text="Filter", command=self.filter_jurusan).grid(row=0, column=5, padx=5)

        # =======================
        # TREEVIEW
        # =======================
        frame_table = tk.Frame(root)
        frame_table.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.tree = ttk.Treeview(
            frame_table,
            columns=("NIM", "Nama", "Jurusan", "IPK"),
            show="headings"
        )
        self.tree.heading("NIM", text="NIM")
        self.tree.heading("Nama", text="Nama")
        self.tree.heading("Jurusan", text="Jurusan")
        self.tree.heading("IPK", text="IPK")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # =======================
        # FRAME FITUR TAMBAHAN
        # =======================
        frame_extra = tk.Frame(root, pady=5)
        frame_extra.pack()

        tk.Button(frame_extra, text="Rata-rata IPK", command=self.rata_ipk).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_extra, text="IPK Tertinggi", command=self.ipk_tertinggi).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_extra, text="Export ke TXT", command=self.export_txt).pack(side=tk.LEFT, padx=5)

    # =======================
    # METHOD CRUD
    # =======================
    def tambah(self):
        nim = self.entry_nim.get()
        nama = self.entry_nama.get()
        jurusan = self.entry_jurusan.get()

        try:
            ipk = float(self.entry_ipk.get())
        except ValueError:
            messagebox.showerror("Error", "IPK harus berupa angka!")
            return

        if not nim or not nama or not jurusan:
            messagebox.showwarning("Peringatan", "Semua data wajib diisi!")
            return

        if nim in self.data_mahasiswa:
            messagebox.showerror("Error", "NIM sudah terdaftar!")
            return

        self.data_mahasiswa[nim] = Mahasiswa(nim, nama, jurusan, ipk)
        self.tampilkan_semua()

    def update(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data!")
            return

        nim = self.tree.item(selected[0])["values"][0]
        try:
            ipk_baru = float(self.entry_ipk.get())
        except ValueError:
            messagebox.showerror("Error", "IPK harus angka!")
            return

        self.data_mahasiswa[nim].update_ipk(ipk_baru)
        self.tampilkan_semua()

    def hapus(self):
        selected = self.tree.selection()
        if selected:
            nim = self.tree.item(selected[0])["values"][0]
            del self.data_mahasiswa[nim]
            self.tampilkan_semua()

    def cari(self):
        keyword = self.entry_cari.get().lower()
        self.tree.delete(*self.tree.get_children())

        for mhs in self.data_mahasiswa.values():
            if keyword in mhs.nim.lower() or keyword in mhs.nama.lower():
                self.tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    def filter_jurusan(self):
        jurusan = self.entry_filter.get().lower()
        self.tree.delete(*self.tree.get_children())

        for mhs in self.data_mahasiswa.values():
            if jurusan in mhs.jurusan.lower():
                self.tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    def tampilkan_semua(self):
        self.tree.delete(*self.tree.get_children())
        for mhs in self.data_mahasiswa.values():
            self.tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    # =======================
    # FITUR TAMBAHAN
    # =======================
    def rata_ipk(self):
        if not self.data_mahasiswa:
            return
        rata = sum(m.ipk for m in self.data_mahasiswa.values()) / len(self.data_mahasiswa)
        messagebox.showinfo("Rata-rata IPK", f"Rata-rata IPK: {rata:.2f}")

    def ipk_tertinggi(self):
        mhs = max(self.data_mahasiswa.values(), key=lambda m: m.ipk)
        messagebox.showinfo("IPK Tertinggi", mhs.info())

    def export_txt(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt")
        if file:
            with open(file, "w") as f:
                for mhs in self.data_mahasiswa.values():
                    f.write(mhs.info() + "\n")
            messagebox.showinfo("Sukses", "Data berhasil diexport!")


# =======================
# MAIN
# =======================
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiMahasiswa(root)
    root.mainloop()
