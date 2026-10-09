# 1. Tambahkan data ini di bagian paling atas
data = [
    {"nama": "Ani", "kelas": "A", "nilai": 85},
    {"nama": "Budi", "kelas": "B", "nilai": 60},
    {"nama": "Citra", "kelas": "A", "nilai": 90},
    {"nama": "Dodi", "kelas": "C", "nilai": 70},
    {"nama": "Eka", "kelas": "B", "nilai": 88}
]

# 2. Kode Anda yang di bawah tetap sama
nilai = [d["nilai"] for d in data]
rata = sum(nilai) / len(nilai)
print(f"Rata-rata: {rata:.1f}")

lulus = [d["nama"] for d in data if d["nilai"] >= 75]
print("Lulus:", lulus)

top = max(data, key=lambda d: d["nilai"])
print("Tertinggi:", top["nama"])