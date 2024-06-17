from tugas_akhir import Kendaraan, Kecepatan

class Mobil(Kendaraan, Kecepatan):
    def __init__(self, merek, model, tenaga):
        super().__init__(merek, model)
        self.tenaga = tenaga

    def Mengendarai(self):
        return f"Mobil {self} melaju dengan tenaga {self.tenaga} horspower."

    def Max_kecepatan(self):
        return f"Mobil {self} melaju dengan kecepatan maksimum 400 km/h."

class Motor(Kendaraan, Kecepatan):
    def __init__(self, merek, model, gigi):
        super().__init__(merek, model)
        self.gigi = gigi

    def Mengendarai(self):
        return f"Motor {self} melaju dengan {self.gigi} gigi."

    def Max_kecepatan(self):
        return f"Motor {self} melaju dengan kecepatan maksimum 200 km/h."

def kendaraan_info(kendaraan):
    print(kendaraan.Mengendarai())
    print()
    print(kendaraan.Max_kecepatan())

def main():
    mobil = Mobil("Toyota", "Kijang", 500)
    print()
    motor = Motor("Kawasaki", "ZX-6R", 4)

    kendaraan_info(mobil)
    print()
    kendaraan_info(motor)

if __name__ == "__main__":
    main()
