import csv

total_age = 0
count = 0

with open('people_with_header.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_age += int(row['age'])
        count += 1

average_age = total_age / count if count > 0 else 0
print("Average age:", average_age)
# Fungsi: Menghitung rata-rata umur dari data dalam file CSV.
# Kondisi: Ketika Anda ingin melakukan analisis lebih lanjut pada data yang didapatkan.
