import csv

data = [
    ['City', 'Country'],
    ['Paris', 'France'],
    ['Tokyo', 'Japan'],
]

with open('cities.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data kota berhasil ditulis ke 'cities.csv'.")
# Fungsi: Menulis list of lists ke dalam file CSV.
# Kondisi: Ketika Anda memiliki data terstruktur dalam format list yang ingin disimpan.
