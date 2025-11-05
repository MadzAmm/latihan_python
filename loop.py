# while loop angka dengan pengkodisian
angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang --> {angka}")
print("selesai")

# for loop str
kata = "Muhammad"
for huruf in kata:
    print(huruf)


# for loop segitiga siku
for huruf in range(1, 9):
    print(kata[:huruf])

# bisa juga dengan memakai len
for huruf in range(1, len(kata) + 1):
    print(kata[:huruf])


# loop str segitiga siku terbalik
for huruf in range(9, 0, -1):
    print(kata[:huruf])

# bisa juga menggunakan len
for huruf in range(len(kata), 0, -1):
    print(kata[:huruf])

# for loop dengan input dari user
# angka1 = int(input("maskuan angka: "))
# for i in range(angka1):
#     i += 1
#     print(f"angka sekarang -->{i}")
# print("Selesai")


# for loop dari komentar yt
for i in range(5, 0, -1):
    print(" " * (i), end="")
    for x in range(i):
        print("*" * (x), end="")

    print()

# for loop segitga siku kanan atas
for i in range(10, 0, -1):
    print(" " * (10 - i), "*" * i)

# for loop segitiga siku kiri bawah
for i in range(0, 10):
    if i % 2 and i <= 10:
        print(" " * (10 - i), "*" * i)

# Menggambar belah ketupat dengan for loop dan if
for i in range(20, 0, -1):
    if i % 2 and i >= 10:
        print(" " * (-10 + i), "*" * (20 - i) * 2)
    elif i == 10:
        for x in range(10, 0, -1):
            if x % 2:
                print(" " * (12 - x), "*" * (x - 2) * 2)


# Menggambar belah ketupat dengan kombinasi while loop, for loop, dan if-elif
x = 0
while x < 20:
    x += 1
    if x % 2 and x <= 10:
        print(" " * (10 - x), "*" * (x) * 2)
    elif x == 10:
        for y in range(0, 8):
            if y % 2:
                print(" " * (y + 2), "*" * (8 - y) * 2)
