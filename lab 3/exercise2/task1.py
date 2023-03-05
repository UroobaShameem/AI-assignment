# Open the file in write mode
with open('cities.txt', 'w') as file:
    # Get the number of cities to input
    num_cities = int(input("Enter the number of cities: "))
    
    # Loop through each city and get its data
    for i in range(num_cities):
        name = input(f"Enter the name of city {i+1}: ")
        population = int(input(f"Enter the population of city {i+1}: "))
        mayor = input(f"Enter the mayor of city {i+1}: ")
        
        # Write the data to the file
        file.write(f"{name},{population},{mayor}\n")