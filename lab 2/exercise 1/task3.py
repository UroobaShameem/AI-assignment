# input username and password
username = input("Enter username: ")
password = input("Enter password: ")

# check password and print message
if(password== "abc$123") or (password== "ABC$123"):
    print("Welcome ", username)

else:
    print("I don't know you")


