# program to remove 0th, 4th, and 5th elements in a list

list= ['Apple', 'Mango', 'Orange', 'Grapes', 'Pineapple', 'Banana', 'Watermelon']
list= [x for (i,x) in enumerate(list) if i not in (0,4,5)]
print(list)