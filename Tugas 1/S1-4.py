nilai_input = input("Masukkan daftar nilai, pisahkan dengan spasi: ")
list_nilai = nilai_input.split()

list_nilai = [int(nilai) for nilai in list_nilai]

print(f"Daftar nilai awal: ", list_nilai)

nilai_baru = int(input(f"Nilai baru: "))

if nilai_baru not in list_nilai:
    list_nilai.append(nilai_baru)
    print("Nilai ", nilai_baru, "berhasil ditambahkan.")
    print("Daftar nilai setelah ditambahan: ", list_nilai)
else:
    print("Nilai sudah ada.")