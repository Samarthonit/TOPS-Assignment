Dict = {'Microsoft': 1, 'Google': 2, 'Apple': 3, 'Amazon': 4, 'Meta': 5}
Keys = {'Apple', 'Google'}

if Keys.issubset(Dict.keys()):
    print("All Keys Exist")
else:
    print('Keys are missing')