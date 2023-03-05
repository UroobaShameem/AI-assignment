# Open the file in append mode, which will create the file if it doesn't exist
with open('student.txt', 'a') as file:
    # Write the message to the file
    file.write("Now we are AI students\n")