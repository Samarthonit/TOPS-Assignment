String1 = input("Enter Your String 1: ")
String2 = input("Enter Your String 2: ")

if len(String1) >= 2 and len(String2) >= 2:
    New_String1 = String2[:2] + String1[2:]
    New_String2 = String1[:2] + String2[2:]
    Answer = New_String1 + "" + New_String2
    print(Answer)
else:
    New_String1 = String1
    New_String2 = String2
    Answer = New_String1 + "" + New_String2
    print(Answer)
