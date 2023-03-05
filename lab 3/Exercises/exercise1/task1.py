numbers = [1, 2, 3, 4, 5]

# Use lambda functions to define square and cube operations
square = lambda x: x ** 2
cube = lambda x: x ** 3

# Use map() function to apply the lambda functions to each element of the list
squared_numbers = list(map(square, numbers))
cubed_numbers = list(map(cube, numbers))

# Print the results
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print("Cubed numbers:", cubed_numbers)
