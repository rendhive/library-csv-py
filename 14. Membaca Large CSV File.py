import csv

# Membaca file CSV besar dengan chunking (tidak memuat seluruh file ke memori)
with open('large_file.csv', 'r') as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if i < 5:  # Hanya mencetak 5 baris pertama
            print(row)
# Fungsi: Membaca file CSV besar dalam cara yang efisien.
# Kondisi: Ketika Anda bekerja dengan file CSV yang tidak dapat dimuat semuanya ke memori sekaligus.
