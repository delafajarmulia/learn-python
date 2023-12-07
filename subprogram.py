# cara membuat function di python
def mencariLuasPersegiPanjang(panjang, lebar):
    luasPersegiPanjang = panjang * lebar
    return luasPersegiPanjang

pp1 = mencariLuasPersegiPanjang(8, 5)
print(pp1)

# Docstring adalah akronim dari documentation string, bertujuan untuk membuat dokumentasi terhadap fungsi yang dibuat. 
# Umumnya, dokumentasi yang dijelaskan berupa argumen, return, deskripsi fungsi, dan sebagainya.
def mencari_luas_persegi_panjang(panjang,lebar):
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.

    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """

    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

# Anda bisa bayangkan parameter seperti black box yang akan menampung nilai dan nilai tersebut adalah argumen.
def greeting(name, pesan):
    return "Hello.. " + name + "! " + pesan

# dibawah ini work all
# pesan1 = greeting(pesan="Selamat sore", name="Dela")
# print(pesan1)
# pesan2 = greeting("Fajar", "oiii") 
# print(greeting("Fajar", "oiii")) # tapi bisa kek gini

# MACAM MACAM PARAMETER
# 1. Positional-or-Keyword
def greetingLagi(nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greetingLagi("Dicoding", "Selamat pagi!"))
print(greetingLagi(pesan="Selamat sore!", nama="Dicoding"))

# 2. Positional-Only
def penjumlahan(a, b, /):
    return a + b

print(penjumlahan(8, 50))

# 3. Keyword-Only "*" asterisk
def greetingManing(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greetingManing(pesan="Selamat sore!",nama="Dicoding"))

# 4. Var-Positional (Variadic Positional Parameter) "*args"
def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))

# 5. Var-Keyword (Variadic Keyword Parameter)
# Parameter ini ditentukan dengan menggunakan sintaks **kwargs yang berperan sebagai dictionary (seperti tipe datanya). 
# Argumen pada pemanggil fungsi akan berperan sebagai value dan parameter (identifier) berperan sebagai key.
def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))

# Fungsi Anonim (Lambda Expression)
hitungLuasLayang2 = lambda d1, d2: 1/2 * d1 * d2
print(hitungLuasLayang2(8, 45))

# global and local variable 
global_var = 5
def add(b):
    lokal_var = 5
    result = global_var + b - lokal_var
    return result

# modul and import
import hello
persegiPanjang1 = hello.mencari_luas_persegi_panjang(4, 9)
print(hello.name)

# bisa juga spt ini
# from hello import mencari_luas_persegi_panjang, nama
 
# persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
# print(persegi_panjang_pertama)
 
# print(nama)