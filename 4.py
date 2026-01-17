meters = float(input('введите количество метров: '))

print("Виберіть варіант:")
print("1 - одна одиниця (мілі, дюйми, ярди)")
print("2 - всі три одиниці (мілі, дюйми, ярди)")
print("3 - кілометри та сантиметри")

choice = input("Введіть номер варіанту: ")

if choice == "1":
    choice1 = input('выберите единицу: мили, дюймы, ярды: ')

    if choice1 == 'мили':
        print(meters * 0.000621371)
    elif choice1 == 'дюймы':
        print(meters * 39.3701)
    elif choice1 == 'ярды':
        print(meters * 1.09361)

elif choice == "2":
    print("Мили:", meters * 0.000621371)
    print("Дюймы:", meters * 39.3701)
    print("Ярды:", meters * 1.09361)

elif choice == "3":
    print("Километры:", meters / 1000)
    print("Сантиметры:", meters * 100)
