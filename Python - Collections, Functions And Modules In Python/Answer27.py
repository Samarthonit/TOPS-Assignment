Tuple = (1, 2, 3, 4, 2, 5, 6, 3, 2, 7)

Repeated = {item for item in Tuple if Tuple.count(item) > 1}

print("Repeated items:", Repeated)  
