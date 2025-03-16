# Difference Between append() and extend()
# append() and extend() are used to add elements to a list, but they work differently
# append() is used for single items and extend() used for multiple items


# Example of append()
list1 = [1, 2, 3, 4, 5]
list1.append([6, 7])
print("List of append() -", list1)

# Example of extend()
list2 = [1, 2, 3, 4, 5]
list2.extend([6, 7])
print("List of extend() -", list2)