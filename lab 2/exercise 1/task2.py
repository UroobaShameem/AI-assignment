# input time of worker
time = float(input("Enter time in hours: "))

# check time and print efficiency
if(time >= 2) and (time <= 3):
    print("Highly efficient")

elif(time >= 3.01) and (time <= 4):
    print("Improve speed")

elif(time >= 4.01) and (time <= 5):
    print("Needs training")

else:
    print("Terminated")