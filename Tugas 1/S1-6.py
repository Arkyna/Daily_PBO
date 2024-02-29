input_buah = input("Set 1: ")
list_buah_1 = input_buah.split()
list_buah_1 = set(list_buah_1)

input_buah = input("Set 2: ")
list_buah_2 = input_buah.split()
list_buah_2 = set(list_buah_2)

buah_dikedua_list = list_buah_1.intersection(list_buah_2)

get_for_a = {get_for_a for get_for_a in buah_dikedua_list if 'a' in get_for_a}

print("Buah yang ada di kedua set dan mengandung huruf 'a': ", get_for_a)
