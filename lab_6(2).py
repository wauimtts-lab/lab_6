cities1 = input('Введите первый список городов: ').split()
cities2 = input('Введите второй список городов: ').split()

set1=set(cities1)
set2=set(cities2)

if set1 == set2:
    print("ДА")
else:
    print("НЕТ")