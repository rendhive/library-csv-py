import csv
import json

with open('people_with_header.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

json_data = json.dumps(data)
print("Data JSON:", json_data)
# Fungsi: Mengonversi data CSV menjadi format JSON.
# Kondisi: Ketika Anda ingin mengubah data yang bersifat tabular menjadi format JSON.
