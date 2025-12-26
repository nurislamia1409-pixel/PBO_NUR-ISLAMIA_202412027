# Class Laptop
class Laptop:
    def nyalakan(self):
        return "Laptop menyala dan siap digunakan"


# Class Smartphone
class Smartphone:
    def nyalakan(self):
        return "Smartphone menyala dan masuk ke layar utama"


# Fungsi duck typing
def tes_nyala(obj):
    print(obj.nyalakan())


# Demonstrasi duck typing
l = Laptop()
s = Smartphone()

tes_nyala(l)   
tes_nyala(s)