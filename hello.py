try:
    a = float(input("Enter a valid number: "))
    b = float(input("Enter another valid number: "))
    x = input("Enter a valid operation (*,/,+,-) : ")
    if x == '-':
        print("The difference between the two given numbers is: ", a-b)
    elif x == '*':
        print("The product of the two given numbers is: ", a*b)
    elif x == '/':
        print("The division of the two given numbers is: ", a/b)
    elif x == '+':
        print("The sum of the two given numbers is: ", a+b)
    else:
        print("Please enter a valid operation")
except ValueError:
    print("Please enter a valid number")
