# # Even or odd number
# num = int(input("Enter a random number: "))
# if num % 2 == 0:
#     print(f'{num} is an even number')
# else:
#     print(f"{num} is an odd number")

# # Temperature check
# temp = int(input('What is the temperature value?: '))
# if temp <= 15:
#     print("Cold")
# elif 15 <= temp <= 30:
#     print("Warm")
# else:
#     print("Hot")

# # Password Checker
# correct_password = "python123"
# password = input("Enter your password: ")
# if password == correct_password:
#     print("Access Granted")
# else:
#     print("Access Denied")

# # Counting numbers
# for i in range(1, 11):
#     print(i)


# Login System with Attempts
# correct_password = "password1234"
# for i in range (1, 4):
#     password = input("Enter your password: ")
#     if password == correct_password:
#         print("Login successful")
#         break
#     else:
#         print("Account locked!")

# Countdown Timer with conditions
num = int(input("Enter a number: "))
while num >= 0:
    if num == 0:
        print(num)
    elif num % 5 == 0:
        print(f"{num} is Multiple of 5")
    elif num % 2 == 0:
        print(f"{num} is an Even number")
    elif num % 2 == 1:
        print(f"{num} is an Odd number")
    num += -1