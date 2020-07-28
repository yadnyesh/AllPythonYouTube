number = int(input("Enter number: "))

if number < 0:
    print("The number you entered is -ve")
elif number > 0:
    print("The number you entered is +ve")
elif number == 0:
    print("The number is zero")
else:
    print("Input is not a number")           