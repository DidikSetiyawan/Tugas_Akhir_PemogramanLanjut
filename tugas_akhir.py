from abc import ABC, abstractmethod

# Kelas Abstrak
class Kendaraan(ABC):
    def __init__(self, merek, harga):
        self.merek = merek
        self.harga = harga

    @abstractmethod
    def Mengendarai(self):
        pass

    def __str__(self):
        return f"{self.merek} {self.harga}"

# Kelas Interface
class Kecepatan(ABC):
    @abstractmethod
    def Max_kecepatan(self):
        pass
