umur, ktp = 20, True
if umur >= 17:
    if ktp:
        print("Boleh memilih")
    else:
        print("Buat KTP dulu")

#ternary-if dalam satu baris
s = "dewasa" if umur >= 17 else "anak"
print(s)