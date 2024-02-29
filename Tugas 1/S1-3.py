nilai_input = input("Masukkan daftar nilai, pisahkan dengan spasi: ")
list_nilai = nilai_input.split()

print(f"Daftar nilai awal", list_nilai)

nilai_baru = int(input(f"Nilai baru: "))
list_nilai.append(nilai_baru)

print("Daftar nilai setelah ditambahkan: ", list_nilai)