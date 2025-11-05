angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang --> {angka}")
print("selesai")

angka1 = int(input("maskuan angka: "))
for i in range(angka1):
    i += 1
    print(f"angka sekarang -->{i}")
print("Selesai")


for i in range(5, 0, -1):
    print(" " * (i), end="")
    for x in range(i):
        print("*" * (x), end="")

    print()


for i in range(0, 10):
    if i % 2 and i <= 10:
        print(" " * (10 - i), "*" * i)

for i in range(20, 0, -1):
    if i % 2 and i >= 10:
        print(" " * (-10 + i), "*" * (20 - i) * 2)
    elif i == 10:
        for x in range(10, 0, -1):
            if x % 2:
                print(" " * (12 - x), "*" * (x - 2) * 2)

x = 0
while x < 20:
    x += 1
    if x % 2 and x <= 10:
        print(" " * (10 - x), "*" * (x) * 2)
    elif x == 10:
        for y in range(0, 8):
            if y % 2:
                print(" " * (y + 2), "*" * (8 - y) * 2)
