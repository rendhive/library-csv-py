import csv

try:
    with open('non_existing_file.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File tidak ditemukan.")
# Fungsi: Menangani error saat mencoba membaca file CSV.
# Kondisi: Ketika Anda ingin memastikan aplikasi Anda tidak berhenti jika file tidak ada.
