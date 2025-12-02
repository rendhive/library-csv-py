import csv

data = [['Name', 'Age'], ['Alice', 30], ['Bob', 25]]

with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data berhasil ditulis ke 'people.csv'.")
# Fungsi: Menulis data ke dalam file CSV.
# Kondisi: Ketika Anda ingin menyimpan data terstruktur ke dalam format CSV.
