import csv

data = [{'name': 'Charlie', 'age': 28}, {'name': 'Daisy', 'age': 24}]

# Menyimpan data ke CSV
with open('people_another.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'age'])
    writer.writeheader()
    writer.writerows(data)

# Memuat kembali data dari CSV
with open('people_another.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
# Fungsi: Menyimpan dan memuat data ke dalam file CSV.
# Kondisi: Ketika Anda ingin mengelola data dengan sinkronisasi penyimpanan dan pembacaan.
