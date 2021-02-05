# We need to write a program that helps Bob The Builder calculate the amount of flooring customer needs.

def getArea():
    width = float(input("Width in feet: "))
    length = float(input("Length in feet: "))
    return  width * length

def calculateFlooringPrice(area, priceSelectedFlooring):
    return priceSelectedFlooring * area

def printTotal(priceSelectedFlooring, price ):
    print("Price: " + str(priceSelectedFlooring) + "/sq ft.")
    print("Total Cost: $" + str(round(price)))

try:
    selectedFlooring = int(input("What type of flooring would you like to purchase? " +
                            "Please select a type that corresponds to a number.\n" +
                            " 1) Vinyl Plank 2) Marble Tile 3) Solid Hardwood\n"))
    
    if selectedFlooring < 1 or selectedFlooring > 3:
        print("That is not a valid option")

    if selectedFlooring == 1:
        vinylPrice = 1.58
        area = getArea()
        total = calculateFlooringPrice(area, vinylPrice)
        printTotal(vinylPrice, total)
    elif selectedFlooring == 2:
        marblePrice = 3.58
        area = getArea()
        total = calculateFlooringPrice(area, marblePrice)
        printTotal(marblePrice, total)
    elif selectedFlooring == 3:
        hardwoodPrice = 2.58
        area = getArea()
        total = calculateFlooringPrice(area, hardwoodPrice)
        printTotal(hardwoodPrice, total)
except:
    print("Please enter a number.")


# CHALLENGE:
# Per my flooring research, it is common to include an additional 10% to account for waste.
# Create a new function that returns flooring price with waste.
# Hint: 
# def calcualteFlooringPriceWithWaste(area, selectedFlooringPrice):
#     squareFootageWithWaste = area * 1.1
#     // Finish this function

# BONUS:
# Ask the customer if they would like to include 10% waste in their final quote.
# If no, just calulate the flooring price without waste
# If yes, calculate flooring price with waste

    

















