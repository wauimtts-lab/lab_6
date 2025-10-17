s = input("Введите группы чисел: ")

groups = s.split(";")
otrezok = []
treug = []
chetireh = []
other = []

for group in groups:
    nums = group.split()
    length = len(nums)
    nums_tuple = tuple(map(int, nums))

    if length ==1:
        otrezok.append(nums_tuple)
    elif length == 3:
        treug.append(nums_tuple)
    elif length == 4:
        chetireh.append(nums_tuple)
    else:
        other.append(nums_tuple)

print("Отрезки: ", otrezok)
print("Треугольники: ", treug)
print("Четырехугольники: ", chetireh)
print("Другие фигуры", other)