def divide_num(num1, num2):
    try:
        divide = num1 / num2
    except ZeroDivisionError:
        return 'Cannot divide by zero'
    else:
        return divide

numeritor = input("Please enter the numeritor: ")
denominator = input("Please enter the denominator: ")
divide = divide_num(int(numeritor), int(denominator))
print(divide)

#Other exceptions include
#TypeError