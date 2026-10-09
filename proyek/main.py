def rata_rata(data):
    return sum(data) / len(data)

import sys
import os

# Baris ini otomatis mencari tahu lokasi folder proyek Anda agar tidak error import
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.hitung import rata_rata

# Tambahkan kode pengujian di bawah ini untuk melihat hasilnya
print("Hasil rata-rata adalah:", rata_rata([80, 90, 70]))

# Karena main.py dan folder utils sudah sama-sama di dalam folder proyek,
# Anda cukup memanggilnya seperti ini:
from utils.hitung import rata_rata

# Tambahkan print di bawah ini untuk menguji hasilnya
print("Program berhasil jalan!")