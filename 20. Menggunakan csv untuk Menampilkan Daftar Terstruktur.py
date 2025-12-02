import csv

data = [['Product', 'Price'], ['Laptop', 1500], ['Smartphone', 500]]

with open('products.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Berikut adalah produk yang berhasil disimpan dalam 'products.csv':")

with open('products.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(" | ".join(row))  # Menampilkan item dalam format terstruktur
# Fungsi: Menyimpan dan menampilkan data produk dalam format CSV.
# Kondisi: Untuk melacak dan mempresentasikan informasi produk secara ringkas.
