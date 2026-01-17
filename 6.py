number = int(input('введите трехзначное число'))
number1 = number % 10
number2 = number // 100
number3 = (number // 10) % 10
if number1 == number2 and number2 == number:
    print('Всі цифри однакові')
else:
    print('Цифри різні')