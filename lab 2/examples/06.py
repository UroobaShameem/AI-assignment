pcount=0
ncount=0
count=int(input("Enter the number of numbers you want: "))
i=1
while(i<=count):
    num=int(input("Enter a number: "))
    if(num>0):
        pcount+=1
    else:
        ncount+=1
    i+=1
print("Positive numbers: ",pcount)
print("Negative numbers: ",ncount)