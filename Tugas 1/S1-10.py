input_buah = input("set1 buah: ")
list_buah_1 = input_buah.split()
list_buah_1 = set(list_buah_1)

input_buah = input("set2 buah: ")
list_buah_2 = input_buah.split()
list_buah_2 = set(list_buah_2)

union_list_buah = list_buah_1.union(list_buah_2)
tuple_nama_buah = tuple(sorted(union_list_buah))

print("Tuple buah setelah digabung, di hapus duplikat, dan diurutkan: ",
tuple_nama_buah)