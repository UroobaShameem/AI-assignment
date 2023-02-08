# program to add, remove or update names in a list
list= ['Sadia', 'Ayesha', 'Hamid', 'Ali', 'Sana']

def addName():
    name= input("Enter name to add: ")
    list.append(name)
    print("Name added successfully")

def removeName():
    name= input("Enter name to remove: ")
    list.remove(name)
    print("Name removed successfully")

def updateName():
    name= input("Enter name to update: ")
    newName= input("Enter new name: ")
    list[list.index(name)]= newName 
    print("Name updated successfully")

def displayList():
    print("List: ", list)

while True:
    print("1. Add name\n2. Remove name\n3. Update name\n4. Exit")
    choice= int(input("Enter your choice: "))
    
    if choice== 1:
        addName()
        displayList()
    elif choice== 2:
        removeName()
        displayList()
    elif choice== 3:
        updateName()
        displayList()
    elif choice== 4:
        break
    else:
        print("Invalid choice")
