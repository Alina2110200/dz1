number1 = int (input('введите число'))
number2 = int (input('введите второе число'))
number3 = int (input('введите третье число'))

action = input('какое число вы хотите узнать? самое большое / самое маленькое / среднее')
if action == 'самое большое':
    if number1 > number2 and number1 > number3:
        print(number1)
    elif number2 > number1 and number2 > number3:
        print(number2)
    else:
        print(number3)
elif action == 'самое маленькое':
    if number1 < number2 and number1 < number3:
        print(number1)
    elif number2 < number1 and number2 < number3:
        print(number2)
    else:
        print(number3)
elif action == 'среднее':
    average = (number1 + number2 + number3) / 3
    print(average)


