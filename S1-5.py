input_buah = input("Set 1: ")
list_buah_1 = input_buah.split()
list_buah_1 = set(list_buah_1)

input_buah = input("Set 2: ")
list_buah_2 = input_buah.split()
list_buah_2 = set(list_buah_2)

buah_dikedua_list = list_buah_1.intersection(list_buah_2)

print("Buah yang ada dikedua set: ", buah_dikedua_list)