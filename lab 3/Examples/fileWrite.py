#example 1
f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

#example 2
f = open("demofile.txt", "r")
print(f.read())

#example 3
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")

f=open("demofile.txt", "r")
print(f.read())