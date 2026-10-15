n = int(input("Введіть число N: "))
s = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        s = s + i

print("Сума парних чисел:", s)