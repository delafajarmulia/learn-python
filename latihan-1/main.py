# greeting = 'Hello World'
# print(greeting)

# additiion = 1+1
# result = additiion -1
# print(result)

# name = input("Masukkan nama anda : ")
# print(name)

# age = 17
# salary = 5000000.0

# print(type(age))
# print(type(salary))

# x = 1+2j
# print(type(x))

# multi_line = """Hallo!
# Kapan terakhir kali kita bertemu
# cmiiw"""

# print (multi_line)

# x = 'Dicoding'
# print(x[2:])

# name = 'Dela Fajar Mulia'
# print(f"Nama saya {name}")
# print("nama saya %s"%(name))

# varList = [1, 'Dicoding', True, 9]
# print(varList[2])

# sequence[start:stop:step]

alatTempur = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(alatTempur[0])
print(alatTempur[2])
print(alatTempur[-1])
print(alatTempur[-3])

print(alatTempur[0:5:2])
print(alatTempur[1:])
print(alatTempur[:3])

varTuple = (1, "Dicoding", 1+3j)
print(type(varTuple))
print(varTuple[0])
print(varTuple[0:3])

varSet = {1, 2, 7, 2, 3, 13, 3}
print(varSet)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)

varList = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
print(varList['name'])
varList['job'] = 'Web Developer' # add new data
del varList['isMarried'] # delete data
varList['age'] = 21 #edit data

# int to float
print(float(5))
#float to int
print(int(3.4))
print(int(-3.4))

# Konversi dari-dan-ke String
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))

# Konversi Kumpulan Data
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))

# Konversi ke Dictionary
print(dict([[1,2],[3,4]]))

data_diri = { 'firstName':'Dela', 'lastName': 'Fajar Mulia', 'age':16, 'isMarried': False }


kata = 'dicoding'
print(kata.upper()) # DICODING

kata2 = 'DICODING'
print(kata.lower()) # dicoding

# Metode rstrip() menghapus whitespace pada sebelah kanan atau akhir string.
print("Dicoding          ".rstrip())

# lstrip() bertugas untuk menghapus whitespace pada sebelah kiri atau awal string. 
print("           Dicoding".lstrip())

# Metode ini bertugas untuk menghapus whitespace pada bagian awal dan akhir string.
kata3 = 'CodeCodeDicodingCodeCode'
print(kata3.strip("Code"))

# Metode startswith() bertujuan untuk menemukan suatu kata pada awal string. Metode ini mengembalikan nilai True.
print('Dicoding Indonesia'.startswith('Dicoding'))

# Metode endswith() bertujuan untuk menemukan suatu kata pada akhir string. Metode ini juga mengembalikan nilai True jika menemukannya, sedangkan jika tidak menemukan kata yang diinginkan, nilai False dikembalikan.
print('Dicoding Indonesia'.endswith('Dicoding'))

#join
print(' '.join(['Dicoding','Indonesia', '!'])) # Dicoding Indonesia !

print('123'.join(['Dicoding','Indonesia'])) # Dicoding123Indonesia

# split
print('Dicoding Indonesia !') # ['Dicoding','Indonesia','!']
print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n')) # ['Halo,', 'aku ikan,', 'aku suka sekali menyelam', 'aku tinggal di perairan.', 'Badanku licin dan renangku cepat.', 'Senang berkenalan denganmu.']

#replace
string = 'Ayo belajar Coding di Dicoding'
print(string.replace('Coding', 'Pemrograman')) # Ayo belajar Pemrograman di Dicoding