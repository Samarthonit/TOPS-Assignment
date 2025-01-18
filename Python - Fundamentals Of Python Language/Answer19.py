User_String = input("Enter Your String: ")

Not_String = User_String.find("not")
Poor_String = User_String.find("poor")

if Not_String != -1 and Poor_String != -1 and Not_String < Poor_String:
    New_String = User_String[:Not_String] + "Good" + User_String[Poor_String + 4:]
    print(New_String)

else:
    print(User_String)

# Help From Google