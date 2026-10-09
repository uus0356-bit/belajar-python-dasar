import csv

data = []
with open("nilai.csv") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

print(len(data), "baris")
print(data[0])

import csv

data = []
# 1. Buka file nilai.csv, otomatis ditutup setelah blok selesai
with open("nilai.csv") as f:
    # 2. Baca isi file dan ubah setiap baris menjadi dictionary
    reader = csv.DictReader(f)
    for baris in reader:
        # 3. Konversi nilai dari teks (string) menjadi angka (integer)
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

# 4. Cetak total baris dan data pertama untuk pengujian
print(len(data), "baris")
print(data[0])