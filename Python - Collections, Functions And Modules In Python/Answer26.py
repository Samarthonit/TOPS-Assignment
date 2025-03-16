List = [(1, 2, 3, 4, 5)]

New_Value = 7

New_List = [i[:-1] + (New_Value,) for i in List]

print(New_List)