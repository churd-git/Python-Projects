print("Welcome to the tip calculator!") # Welcome message
bill = float(input("What was the total bill? $")) # Takes the input of the bill total. Input is converted to float and saved as a variable called "bill".
tip = int(input("What percentage tip would you like to give? 10, 12, 15, or another amount: ")) # Takes the input of the desired tip % total. Input is converted to an integer and saved as a variable called "tip".
tip += 100 #Adds 100 to the tip input for later calculations.
people = int(input("How many people to split the bill? ")) # Takes the input of the amount of people splitting the bill. Input is converted to an integer and saved as a variable called "people".
print("Each person should pay:" + str(round((bill/people)*(tip/100),2))) # Print the results of the calculation. BEDMASS for equation.
