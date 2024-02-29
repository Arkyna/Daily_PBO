def jika_prima(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
    i += 6
    return True

def count_numbers(n):
    total = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            if jika_prima(i):
                total += i - 1
    else:
        total += i

    return total

n = int(input("Masukkan nilai: "))
print("Jumlah bilangan yang habis dibagi 3 atau 5 dan bukan prima dalam rentang 1 hingga", n, "adalah", count_numbers(n))