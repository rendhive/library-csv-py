import csv

data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]

with open('people_with_header.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'age'])
    writer.writeheader()
    writer.writerows(data)

print("Data dengan header berhasil ditulis ke 'people_with_header.csv'.")
# Fungsi: Menulis data ke dalam file CSV dengan menambahkan header.
# Kondisi: Ketika Anda ingin menulis dictionary ke CSV dengan nama kolom.
