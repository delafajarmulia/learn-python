# one linear 
w = 1
z = 2
w, z = z, w # value w dan z ditukar

# if
ketersediaan = "Daging ayam"

if ketersediaan == "Daging ayam":
    print("Ibu membeli dan memasak ayam")
else:
    print("Ibu membeli dan memasak tempe")

score = 100
if score == 100: print("skor sempurna") # one linear version

# elif 
nilai = 90
perilaku = 'baik'

if nilai >= 80 : 
    print("Anda mendapatkan nilia A")
elif nilai >= 70 : 
    print("Anda mendapatkan nilai B")
elif nilai >= 60 :
    print("Anda mendapatkan nilai C")
else :
    print("Waduh nilai anda D")
    print("belajar lagi yukk")


if nilai>=80 and perilaku == 'baik':
   print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
   print("Pertahankan!")
elif nilai>=80 and perilaku != 'baik':
   print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
   print("Perbaiki lagi ya!")
else:
   print("Yuk belajar lebih giat lagi!")

# ternary
lulus = True
print("Selamat") if lulus else print("perbaiki")
# ternary tuples
kelulusan = ("Perbaiki, Anda belum lulus", "Selamat Anda lulus")[lulus]
print(kelulusan)

# looping
# for
var_list = [4, 9, 8, 7]
for i in var_list:
    print(i)

for i in range(3):
    print(f"hello {i}")

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i) # 0, 2, 4, 6, 8

# while -> Indefinite iteration adalah sebuah proses iterasi yang akan berhenti ketika memenuhi kondisi tertentu
counter = 1
while counter <= 5:
    print(counter)
    counter += 1

# nested loop
for i in range(1,3):
    for j in range(1, 5):
        print(i,j)

for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1

# Output:
# Perulangan luar: 0
# Perulangan dalam: 0
# Perulangan dalam: 1
# Perulangan luar: 1
# Perulangan dalam: 0
# Perulangan dalam: 1

for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print("huruf saat ini {}".format(huruf))

for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print("huruf saat ini {}".format(huruf))

# else stelah for
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")

# else setelah while
count = 0

while count < 3:
    print("Dicoding Indonesia", count)
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")

# List Comprehension
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)

# mending spt ini
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)