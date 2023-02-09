# Input height, width and depth of a box
height = float(input("Enter height in cm: "))
width = float(input("Enter width in cm: "))
depth = float(input("Enter depth in cm: "))

# Calculate volume
volume = height * width * depth
print("Volume is: ", volume, "cm3")

# condition to check volume and print size
if(volume >= 1) and (volume <= 10):
    print("Extra Small")

elif(volume >= 11) and (volume <= 25):
    print("Small")

elif(volume >= 26) and (volume <= 75):
    print("Medium")

elif(volume >= 76) and (volume <= 100):
    print("Large")

elif(volume >= 101) and (volume <= 250):
    print("Extra Large")

else:
    print("Extra Extra Large")