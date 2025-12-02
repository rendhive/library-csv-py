import csv

with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# Fungsi: Membaca data dari file CSV dan menampilkan setiap baris.
# Kondisi: Ketika Anda ingin memproses data yang tersimpan dalam file CSV.
