data = [{"nama": "Ani", "kelas": "A", "nilai": 85},
    {"nama": "Budi", "kelas": "B", "nilai": 60},
    {"nama": "Citra", "kelas": "A", "nilai": 90},
    {"nama": "Dodi", "kelas": "C", "nilai": 70},
    {"nama": "Eka", "kelas": "B", "nilai": 88}
]
rekap = {}
for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(d["nilai"])

print(f"{'Kelas':<6}{'Jumlah':>8}{'Rata':>8}")
for k, v in sorted(rekap.items()):
    rata = sum(v) / len(v)
    print(f"{k:<6}{len(v):>8}{rata:>8.1f}")