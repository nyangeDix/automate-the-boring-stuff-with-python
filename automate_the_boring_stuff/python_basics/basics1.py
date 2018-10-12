#Here we are only going to deal with two numbers
def add_nums(num1, num2):
    total = int(num1) + int(num2)
    return int(total)

def sub_num(num1, num2):
    sub = int(num1) - int(num2)
    return int(sub)

def num_power(num1, expo_num):
    expo = int(num1) ** int(expo_num)
    return int(expo)

def multi_nums(num1, num2):
    multi = int(num1) * int(num2)
    return int(multi)

def mod_nums(num1, num2):
    mod_num = int(num1) % int(num2)
    return int(mod_num)

def int_div(num1, num2):
    int_div_num = int(num1) // int(num2)
    return int(int_div_num)

#Check for the round function and practise here

numbers1 = add_nums(20, 10)
print(numbers1)
numbers2 = sub_num(20,10)
print(numbers2)
numbers3 = num_power(2,10)
print(num_power)
numbers4 = multi_nums(40,2)
print(numbers4)
numbers5 = mod_nums(24, 8)
print(numbers5)
numbers6 = int_div(23, 7)
print(numbers6)