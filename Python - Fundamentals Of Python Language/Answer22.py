User_String = input("Enter Your String: ")

if len(User_String) < 2:
    print("")
else:
    Answer = User_String[:2] + User_String[-2:]
    print(Answer)

