import csv

# Menghapus baris dengan kondisi tertentu
rows_to_keep = []

with open('people_with_header.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row['age']) >= 25:  # Hanya simpan yang berusia >= 25
            rows_to_keep.append(row)

# Menyimpan kembali ke file
with open('filtered_people.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'age'])
    writer.writeheader()
    writer.writerows(rows_to_keep)

print("Row berhasil difilter dan disimpan ke 'filtered_people.csv'.")
# Fungsi: Menghapus baris dari file CSV berdasarkan kondisi tertentu.
# Kondisi: Ketika Anda ingin mengurangi data yang tidak relevan dari dataset.
