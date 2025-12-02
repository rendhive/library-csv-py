import csv

with open('quotes.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[1])  # Menampilkan hanya kolom kedua
# Fungsi: Membaca data dari file CSV dan menampilkan kolom tertentu.
# Kondisi: Ketika Anda hanya memerlukan informasi spesifik dari file CSV.
