input_buah = input("Tuple buah: ")
list_buah_1 = input_buah.split()

tuple_nama_buah = tuple(sorted(list_buah_1))

print("Tuple buah setelah diurutkan: ", tuple_nama_buah)