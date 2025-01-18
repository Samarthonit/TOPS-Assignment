User_Number = int(input("Enter Your Positive Number: "))

if User_Number <= 0:
    print("Enter Positive Number Not Negative Number")
else:
    Answer = User_Number * (User_Number + 1) // 2
    print("The Sum of First",User_Number, "Positive Integers is", Answer)