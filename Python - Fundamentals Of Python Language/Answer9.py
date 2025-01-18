Number1 = int(input("Enter Your Number 1: "))
Number2 = int(input("Enter Your Number 2: "))
Number3 = int(input("Enter Your Number 3: "))

if Number1 == Number2 or Number2 == Number3 or Number3 == Number1:
    print("The Sum is 0")
else:
    Answer = Number1 + Number2 + Number3
    print("The Sum is", Answer)