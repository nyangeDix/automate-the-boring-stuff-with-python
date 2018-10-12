def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1: 
        return 3 * number + 1

while True:
    try:
        num_input = int(input("Please enter a number: "))
    except ValueError:
        print ("Please enter a integer")
    else:
        collatz_sequence = collatz(num_input)
        if collatz_sequence == 1:
            print(collatz_sequence)
            break
        else:
            print(collatz_sequence)