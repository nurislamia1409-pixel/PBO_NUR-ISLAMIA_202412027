import tkinter as tk
from tkinter import messagebox


class AplikasiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi GUI Sederhana")
        self.root.geometry("300x200")

        # a. Label
        self.label = tk.Label(
            root,
            text="Masukkan Teks:",
            font=("Arial", 12)
        )
        self.label.pack(pady=10)

        # a. Entry
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        # a & b. Button tampilkan isi Entry
        self.button_tampil = tk.Button(
            root,
            text="Tampilkan",
            command=self.tampilkan_teks
        )
        self.button_tampil.pack(pady=5)

        # c. Button hapus isi Entry
        self.button_hapus = tk.Button(
            root,
            text="Hapus",
            command=self.hapus_teks
        )
        self.button_hapus.pack(pady=5)

    # b. Fungsi menampilkan isi Entry
    def tampilkan_teks(self):
        teks = self.entry.get()
        if teks:
            messagebox.showinfo("Pesan", teks)
        else:
            messagebox.showwarning(
                "Peringatan",
                "Entry masih kosong!"
            )

    # c. Fungsi menghapus isi Entry
    def hapus_teks(self):
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiGUI(root)
    root.mainloop()