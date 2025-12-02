import csv

data = [['Product', 'Price'], ['Laptop', '1000'], ['Smartphone', '500']]

with open('products.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Membaca kembali data
with open('products.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# Fungsi: Menggunakan data numerik dalam file CSV dan membaca kembali.
# Kondisi: Ketika Anda perlu menyimpan dan memproses data produk.
