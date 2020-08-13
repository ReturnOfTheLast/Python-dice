from random import randint as __randint

# Roll method
def roll(dCount, dSides, modifier=0, quiet=False, dropLow=0, dropHigh=0):

    if (not quiet): print("Rolling " + str(dCount) + "d" + str(dSides) + "...")

    # Define list of rolls
    dRolls = list()

    # Roll one die at a time and add it to the dRolls list
    for _ in range(dCount):
        dRolls.append(__randint(1, dSides))

    #sort list
    dRolls.sort()

    # drop lowest
    if (dropLow > 0):
        if (not quiet): print("Dropped: " + str(dRolls[:dropLow]))
        dRolls = dRolls[dropLow:]

    # drop highest
    if (dropHigh > 0):
        if (not quiet): print("Dropped: " + str(dRolls[-dropHigh:]))
        dRolls = dRolls[:-dropHigh]

    # Define variable to hold total
    dTotal = 0

    if (not quiet): print("Rolls:", end="")

    # Calculate total and print rolls
    for dRoll in dRolls:
        dTotal += dRoll
        if (not quiet): print(" " + str(dRoll), end="")

    # Adding modifier, if any
    if (modifier != 0):
        dTotal += modifier
        if (not quiet): print("\nAdding modifier: " + str(modifier))

    # Print the total
    if (not quiet): print("\nTotal: " + str(dTotal))

    # Return total
    if (quiet): return dTotal

# Method to roll multiple different dice types
def multiRoll(dRollOrders, modifier=0, quiet=False):

    if (not quiet): print("Rolling dice...")

    # Define variable to hold total
    dTotal = 0

    # Go through and roll all the dice
    for dRollOrder in dRollOrders:
        dTotal += roll(dRollOrder[0], dRollOrder[1])

    # Adding modifier, if any
    if (modifier != 0):
        dTotal += modifier
        if (not quiet): print("\nAdding modifier: " + str(modifier))

    # Print total
    if (not quiet): print("\nMultiroll Total: " + str(dTotal))

    # return total
    if (quiet): return dTotal

# Method to calculate average roll
def calculateAverage(dCount, dSides, modifier=0, quiet=False):

    # Calculate average
    dAverage = dCount * ((dSides/2) + 0.5)

    # Adding modifier, if any
    if (modifier != 0):
        dAverage += modifier
        if (not quiet): print("\nAdding modifier: " + str(modifier))

    # Print average
    if (not quiet): print("\nAverage: " + str(dAverage))

    # return Average
    if (quiet): return dAverage

def calculateMultiAverage(dRollOrders, modifier=0, quiet=False):

    # Define variable to hold total average
    dTotalAverage = 0

    # Go through and calculate each average
    for dRollOrder in dRollOrders:
        dTotalAverage += calculateAverage(dRollOrder[0], dRollOrder[1], quiet=True)

    # Adding modifier, if any
    if (modifier != 0):
        dTotalAverage += modifier
        if (not quiet): print("\nAdding modifier: " + str(modifier))

    # Print total average
    if (not quiet): print("\nTotal average: " + str(dTotalAverage))

    # return total average
    if (quiet): return dTotalAverage

def rollAbilityScore(amount=6):
    scores = list()
    for _ in range(amount):
        scores.append(roll(4, 6, dropLow=1, quiet=True))
    scores.sort()
    print(scores)
