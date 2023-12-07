class Mobil:
    #attribute
    warna = "Biru"

Mobil.warna = 'ijo'
mobilDela = Mobil()
print(mobilDela.warna)
mobilDela.warna = 'Hitam'
print(mobilDela.warna)

class MobilSaya : 
    def __init__(self) -> None: # constructor
        self.warna = 'Hitam'

mobilLagi = MobilSaya()
mobilLagi.warna = 'Putih'
print(mobilLagi.warna)

class MobilTetangga :
    def __init__(self, warna, merk, kecepatan) -> None:
        self.warna = warna
        self.merk = merk
        self.kecepatan = kecepatan

    def tambah_kecepatan(self): # metode dari objek(object method)
        self.kecepatan += 10
    
    # Metode secara Statis (Static Method)
    @staticmethod
    def intro_mobil():
        print("ini adalah metode dari kelas mobil tetangga")

    # Metode dari Kelas (Class Method)
    @classmethod
    def ngenggg(cls): # cls itu wajib bolooo
        print("ngenggg")

mobilFajar = MobilTetangga('Hitam', 'BMW', 250)
print(mobilFajar.warna)
print(mobilFajar.merk)
print(mobilFajar.kecepatan)

mobilFajar.tambah_kecepatan()
print("setelah tambah kecepatan ")
print(mobilFajar.kecepatan)

mobilFajar.intro_mobil()
mobilFajar.ngenggg()

# method
# def my_decorator(func):
#     def wrapper():
#         print("Sebelum fungsi dieksekusi.")
#         func()
#         print("Setelah fungsi dieksekusi.")
#     return wrapper

# # Dekorasi fungsi dengan decorator
# @my_decorator
# def say_hello():
#     print("Hello, world!")

# # Memanggil fungsi yang sudah didekorasi
# say_hello()
"""
Output:
Sebelum fungsi dieksekusi.
Hello, world!
Setelah fungsi dieksekusi.
"""