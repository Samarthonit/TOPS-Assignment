Number = 7

Perfect_Number = sum(i for i in range(1, Number) if Number % i == 0) == Number

print(Perfect_Number)
