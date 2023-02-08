#program to concatenate dictionaries to create a new one

dict_1 = {'a': 1, 'b': 2}
dict_2 = {'c': 3, 'd': 4}
dict_3 = {'e': 5, 'f': 6}

dict= {**dict_1, **dict_2, **dict_3}
print(dict)