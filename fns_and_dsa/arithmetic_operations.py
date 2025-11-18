
def perform_operation(num1, num2, operation):
    if operation == 'add':
        num1 + num2
    elif operation == 'subtract':
        num1 - num2
    elif operation == 'multiply':
        num1 * num2
    elif operation == 'divide':
        if num1 == 0 or num2 == 0:
            print('input a number greater than zero')
        else:
            num1 / num2

