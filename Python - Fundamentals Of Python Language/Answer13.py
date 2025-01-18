User_String = input("Enter Your String: ")

for char in set(User_String):
    print(f'"{char}": {User_String.count(char)}')