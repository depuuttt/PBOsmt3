class Mobil:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def jalan(self):
        print(f"Mobil {self.merk} sedang berjalan.")


class SUV(Mobil):
    def __init__(self, merk, tahun, jumlah_roda):
        super().__init__(merk, tahun)
        self.jumlah_roda = jumlah_roda

    def jalan(self):
        print(f"SUV {self.merk} dengan {self.jumlah_roda} roda sedang berjalan.")


mobil = Mobil("Honda", 2020)
mobil.jalan()
# Output: Mobil Honda sedang berjalan.

suv = SUV("Toyota", 2021, 4)
suv.jalan()
# Output: SUV Toyota dengan 4 roda sedang berjalan.
