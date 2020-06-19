from random import randint as __randint

# Roll method
def roll(dCount, dSides, quiet=False):

    if (not quiet): print("\nRolling " + str(dCount) + "d" + str(dSides) + "...")

    # Define list of rolls
    dRolls = list()

    # Roll one die at a time and add it to the dRolls list
    for _ in range(dCount):
        dRolls.append(__randint(1, dSides))

    # Define variable to hold total
    dTotal = 0

    if (not quiet): print("Rolls:", end="")

    # Calculate total and print rolls
    for dRoll in dRolls:
        dTotal += dRoll
        if (not quiet): print(" " + str(dRoll), end="")

    # Print the total
    if (not quiet): print("\n\nTotal: " + str(dTotal))

    # Return total
    return dTotal

# Method to roll multiple different dice types
def multiRoll(dRollOrders, quiet=False):

    if (not quiet): print("Rolling dice...")

    # Define variable to hold total
    dTotal = 0

    # Go through and roll all the dice
    for dRollOrder in dRollOrders:
        dTotal += roll(dRollOrder[0], dRollOrder[1])
    
    # Print total
    if (not quiet): print("Multiroll Total: " + str(dTotal))

    # return total
    return dTotal

# Method to calculate average roll
def calculateAverage(dCount, dSides, quiet=False):

    # Calculate average
    dAverage = dCount * ((dSides/2) + 0.5)

    # Print average
    if (not quiet): print("Average: " + str(dAverage))

    # return Average
    return dAverage

def calculateMultiAverage(dRollOrders, quiet=False):
    
    # Define variable to hold total average
    dTotalAverage = 0

    # Go through and calculate each average
    for dRollOrder in dRollOrders:
        dTotalAverage += calculateAverage(dRollOrder[0], dRollOrder[1], quiet=True)
    
    # Print total average
    if (not quiet): print("Total average: " + str(dTotalAverage))

    # return total average
    return dTotalAverage