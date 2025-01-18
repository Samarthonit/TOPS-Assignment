User_Number = int(input("Enter Your Number: "))

Factorial_Number = 1

if User_Number < 0:
    print(User_Number, "is Negative Number")
elif User_Number == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, User_Number + 1):
        Factorial_Number *= i
    print("Factorial of", User_Number, "is", Factorial_Number)