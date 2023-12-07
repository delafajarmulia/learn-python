var_array = []
jumlah = 0

for i in range(0, 101):
    var_array.append(i)
    jumlah += i

result = jumlah / len(var_array)
print(result)