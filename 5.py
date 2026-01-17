number1 = int (input('введите число '))
number2 = int(input('введите второе число '))
operation = input('выберите операцию: додавання, віднімання, множення, ділення, знаходження залишку, піднесення до степеня')
if operation == ' додавання':
    addition = (number1 + number2)
    print(addition)
elif operation == ' віднімання':
    subtraction = (number1 - number2)
    print(subtraction)
elif operation == ' множення':
    multiplication = (number1 * number2)
    print(multiplication)
elif operation == ' ділення':
    division = (number1 / number2)
    print(division)
elif operation == ' знаходження залишку':
    rest = (number1 % number2)
    print(rest)
elif operation == ' піднесення до степеня':
    degree = (number1 ** number2)
    print(degree)
