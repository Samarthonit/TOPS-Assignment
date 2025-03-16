import random

with open('example.txt', 'r') as file:
    lines = file.readlines()

random_line = random.choice(lines)

print(random_line.strip())