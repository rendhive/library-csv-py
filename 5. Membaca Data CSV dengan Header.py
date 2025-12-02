import csv

with open('people_with_header.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
# Fungsi: Membaca data dari file CSV dengan header.
# Kondisi: Ketika Anda ingin mengakses data dengan nama kolom.
