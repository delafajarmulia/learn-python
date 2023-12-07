data = []
print("Aplikasi Sederhana Statistika")
countData = int(input("Berapa data yang ingin anda masukkan? "))

def average(countData):
    totalAll = 0
    for i in range(countData):
        value = int(input(f'data ke {i+1} '))
        data.append(value)
        totalAll += value
    result = value / countData
    return result

print(average(countData = countData))
print(data)

def minValue(data):
    min = data[0]
    for i in range(len(data)):
        if( data[i] < min):
            min = data[i]
    return min

print(minValue(data=data)) 

def maxValue(data):
    max = data[0]
    for i in range(len(data)):
        if(data[i] > max):
            max = data[i]
    return max

print(maxValue(data=data))

def findRange(data):
    result = maxValue(data=data) - minValue(data=data)
    return result

print(findRange(data=data))

def median(data):
    countData = len(data)
    result = 0
    if(countData % 2 == 0):
        result = (data[int(countData / 2 - 1)] + data[int(countData / 2)]) / 2
        return result
    else:
        result = data[int(countData / 2)]
        return result
    
print(median(data=data))

# def kuartilBawah(data):
