empty_dictionary = {}

usia_keluarga = {'Budi': 30, 'Andi': 25, 'Cindy': 20, 'Deni': 18}
print(usia_keluarga)

total_usia = 0
jumlah_anggota = 0

for nama, usia in usia_keluarga.items():
    if usia > 20:
        total_usia += usia
        jumlah_anggota += 1
rata_rata_usia = total_usia / jumlah_anggota

print(f"Usia rata-rata anggota keluarga Budi yang usianya lebih dari 20
tahun adalah {rata_rata_usia} tahun.")