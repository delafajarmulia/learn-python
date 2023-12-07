import array

arr1 = [1, 2, 3, 4, 5]
arr2 = array.array("i", [1, 2, 3, 4, 5])

print(arr2)

siswa = [90, 100, 50, 80, 85, 45, 80, 75, 50, 60]
print(siswa[0])

# CARA MENDEKLARASIKAN ARRAY
# Pertama dengan memanfaatkan list dan kedua menggunakan library Python.
var_list = [1, 2, 3]
for element in var_list:
    print(id(element)) # akan menghasilkan lokasi memori setiap elemen yang berada pada list

# mendefinisikan nilai default
var_arr = [0 for i in range(5)] 
print(var_arr) # 0, 0, 0, 0, 0

for i in range(5):
    var_arr[i] = i
print(var_arr) # 0, 1, 2, 3, 4

# mengakses nilai array berdasarkan index tertentu
print(siswa[3]) # 80

# PEMROSESAN SEKUENSIAL PADA ARRAY
# Pemrosesan sekuensial adalah sebuah pemrosesan setiap elemen array yang dimulai dari elemen pada indeks terkecil hingga terbesar. 
# Pemrosesan sekuensial lebih sering menggunakan pengulangan (loop/iterasi) dalam setiap prosesnya.
var_array = [1, 2, "Python asikk", 4, "Dicoding"]

for i in range(len(var_array)):
    current_element = var_array[i]
    next_index = i + 1
    if next_index < len(var_array):
        next_element = var_array[next_index]
    else:
        next_element = None
    print(f"current element {current_element}, next element {next_element}")

# mencari nilai terbesar dalam array
# Untuk memahami algoritma ini, perhatikan beberapa informasi berikut:
#   1. Pointer "left" akan berada pada indeks pertama dan menyatakan bahwa pointer "left" selalu menunjukkan nilai terbesar dalam array.
#   2. Pointer "right" akan selalu berada pada elemen selanjutnya dan membandingkannya dengan elemen pointer "left".
my_arr = [9, 1, 6, 75, 4]
left_pointer = my_arr[0]

for i in range(1, len(my_arr)):
    right_pointer = my_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)