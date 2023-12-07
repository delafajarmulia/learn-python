import matplotlib.pyplot as plt

# Data
x = [6, 4, 3, 6]
y = [2, 4, 6, 5]

# membuat plot garis
plt.plot(x, y)

# menambahkan judul dan label sumbu
plt.title("Contoh plot garis")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")

# menampilkan plot
plt.show()