import csv

data = [['Name', 'Quote'], ['Alice', 'Hello "World"'], ['Bob', 'Keep it simple!']]

with open('quotes.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    writer.writerows(data)

print("Data dengan quotes berhasil ditulis ke 'quotes.csv'.")
# Fungsi: Menyimpan data dengan tanda kutip untuk teks yang mengandung koma.
# Kondisi: Ketika Anda ingin menghindari kesalahan parsing pada data yang berisi koma.
