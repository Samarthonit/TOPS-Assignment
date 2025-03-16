String = "Samarth"

Dict = {}

for char in String:
    if char != " ":
        Dict[char] = Dict.get(char, 0) + 1

print(Dict)
