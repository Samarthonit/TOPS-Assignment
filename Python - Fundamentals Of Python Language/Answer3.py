User_Number = int(input("Enter Your Number: "))

a = 0
b = 1

print("Fibonacci Series")
for i in range(User_Number):
    print(a, end="")
    a,b = b,a+b

# Help from Google