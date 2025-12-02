import csv
import json

json_data = '[{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]'
data = json.loads(json_data)

with open('json_to_csv.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'age'])
    writer.writeheader()
    writer.writerows(data)

print("Data JSON berhasil dikonversi ke CSV.")
# Fungsi: Mengonversi data JSON menjadi format CSV.
# Kondisi: Ketika Anda ingin merepresentasikan data JSON dalam format yang lebih berdasarkan tabular.
