User_String = input("Enter Your String: ")

if len(User_String) >= 3:
    if User_String.endswith("ing"):
        User_String = User_String + "ly"
        print(User_String)
    else:
        User_String = User_String + "ing"
        print(User_String)