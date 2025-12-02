import csv
import glob

filenames = glob.glob('*.csv')
with open('combined.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    
    for fname in filenames:
        with open(fname, 'r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                writer.writerow(row)
print("Semua file CSV berhasil digabungkan ke 'combined.csv'.")
# Fungsi: Menggabungkan beberapa file CSV menjadi satu file.
# Kondisi: Ketika Anda memiliki data yang tersebar di banyak file dan ingin menyusunnya menjadi satu.
