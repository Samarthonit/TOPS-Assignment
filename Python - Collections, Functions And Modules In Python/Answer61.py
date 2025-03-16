Num = int(input("Enter a number: "))

Divisors = 0

for i in range(1, Num + 1):
    if Num % i == 0:
        Divisors += i

print(f"The sum of divisors of {Num} is: {Divisors}")
