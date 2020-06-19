from random import randint as __randint

# Roll method
def roll(dCount, dSides):

    print("\nRolling " + str(dCount) + "d" + str(dSides) + "...")

    # Define list of rolls
    dRolls = list()

    # Roll one die at a time and add it to the dRolls list
    for _ in range(dCount):
        dRolls.append(__randint(1, dSides))

    # Define variable to hold total
    dTotal = 0

    print("Rolls:", end="")

    # Calculate total and print rolls
    for dRoll in dRolls:
        dTotal += dRoll
        print(" " + str(dRoll), end="")

    # Print the total
    print("\n\nTotal: " + str(dTotal))

    # Return total
    return dTotal

# Method to roll multiple different dice types
def multiRoll(dRollOrders):

    print("\nRolling dice...\n")

    # Define variable to hold total
    dTotal = 0

    # Go through and roll all the dice
    for dRollOrder in dRollOrders:
        dTotal += roll(dRollOrder[0], dRollOrder[1])
    
    # Print total
    print("\n\n\nMultiroll Total: " + str(dTotal))

# Method to calculate average roll
def calculateAverage(dCount, dSides):

    # Calculate average
    dAverage = dCount * ((dSides/2) + 0.5)

    # Print average
    print("Average: " + str(dAverage))