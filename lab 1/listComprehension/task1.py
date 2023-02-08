# program to generate lowercased version of each string that has
# length greater than five

list= {"PAKISTAN", "CHINA", "UAE", "AFGHANISTAN", "KSA"}

newList = [x.lower() for x in list if len(x) > 5]
print(newList)