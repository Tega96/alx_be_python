num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
        print("The result is", result)
    case "-":
        result = num1 - num2
        print("The result is ", result)
    case "*":
        result = num1 * num2
        print("The result is", result)
    case "/":
        if num1 == 0 or num2 == 0:
            print("Please, insert an number above zero")
        else:
            result = num1 / num2
            print("The result is ", result)
    case _:
        print("Please, enter a valid operator")