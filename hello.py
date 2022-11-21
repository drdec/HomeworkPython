import math

print("Задание 1")
print()

print("Введите номер дня недели")
day_of_the_week = int(input())

if day_of_the_week != 6 and day_of_the_week != 7:
    print("no")

else:
    print("yes")

print()
print("Задание 2")
print()

print(True)  # всегда будет True, ибо это булевая алгебра, раскрыв скобки будет два одинаковых выражения

print()
print("Задание 3")
print()

print("Введите x")
x = int(input())

print("Введите y")
y = int(input())

print()

if x != 0 and y != 0:
    if x > 0 and y > 0:
        print(1)

    if x > 0 and y < 0:
        print(4)

    if x < 0 and y > 0:
        print(2)

    if x < 0 and y < 0:
        print(3)

else:
    print("X или Y не должны равняться нулю!!!!!")

print()
print("Задание 4")
print()

print("Введите номер четверти")

quarter = int(input())

if quarter == 1:
    print("0 < x < infinity and 0 < y < infinity")
elif quarter == 2:
    print("minus infinity < x < 0 and 0 < y < infinity")
elif quarter == 3:
    print("minus infinity < x < 0 and minus infinity < y < 0")
elif quarter == 4:
    print("0 < x < infinity and minus infinity < y < 0")
else:
    print("Номер четверти должен быть в промежутке 0 < x < 5, где x - номер четверти")

print()
print("Задание 5")
print()

print("Введите Ax")
ax = int(input())

print("Введите Ay")
ay = int(input())

print("Введите Bx")
bx = int(input())

print("Введите By")
by = int(input())

res = math.sqrt((bx - ax) ^ 2 + (by - ay) ^ 2)

print(f"Расстояние между точками равно = {res}")
