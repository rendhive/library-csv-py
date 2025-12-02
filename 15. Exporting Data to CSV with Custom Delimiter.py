import csv

data = [['Name', 'Age'], ['Alice', 30], ['Bob', 25]]

with open('people_pipe.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(data)

print("Data berhasil ditulis ke 'people_pipe.csv' dengan delimiter '|'.")
# Fungsi: Menyimpan data CSV dengan pemisah khusus.
# Kondisi: Ketika Anda ingin menggunakan pemisah yang berbeda dari koma.
