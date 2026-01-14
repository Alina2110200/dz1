number1 = int (input('введите число'))
number2 = int (input('введите второе число'))
number3 = int (input('введите третье число'))

action = input('выберите действие + или * ')
if action == '+' :
    print(number1 + number2 + number3)
else:
    print(number1 * number2 * number3) 