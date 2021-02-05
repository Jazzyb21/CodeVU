import math
# We need to write a program that helps Bob The Builder calculate the amount of flooring a house needs.

# vinylPrice = 1.58
# marblePrice = 3.58
# hardwoodPrice = 2.58

def calcualteFlooringPriceWithWaste(area, selectedFlooringPrice):
    response = input("Would you like to include 10% waste in your final quote?\n Y or N\n")
    finalPrice = ''
    if response.upper() == 'Y':
        withWaste = area * 1.1
        total = math.ceil(withWaste) * selectedFlooringPrice
        finalPrice = float(total)
    elif response.upper() == 'N':
        finalPrice = None
    else:
        print("Not a valid option. We will assume no.")
        finalPrice = None
    return finalPrice
          
def calculateFlooringPrice(selectedFlooringPrice):
    width = float(input("Width in feet: "))
    length = float(input("Length in feet: "))
    area = width * length
    withWastePrice = calcualteFlooringPriceWithWaste(area, selectedFlooringPrice)
    return float(withWastePrice) if withWastePrice != None else area * selectedFlooringPrice

def printFlooringPrice(finalPrice, selectedFlooringPrice):
    print("Price: " + str(selectedFlooringPrice) + " / sq ft.")
    print("Total Cost: $" + str(round(price)))

try:
    selectedFlooring = int(input("What type of flooring would you like to buy? Select a type that corresponds to a number." +
    "\n 1) Vinyl Plank 2) Marble Tile 3) Solid Hardwood\n"))

    if selectedFlooring < 1 or selectedFlooring > 3:
        print("That is not a valid selection.")
        

    if selectedFlooring == 1:
        vinylPrice = 1.58
        price = calculateFlooringPrice(vinylPrice)
        printFlooringPrice(price, vinylPrice)
    elif selectedFlooring == 2:
        marblePrice = 3.58
        price = calculateFlooringPrice(marblePrice)
        printFlooringPrice(price, marblePrice)
    elif selectedFlooring == 3:
        hardwoodPrice = 2.58
        price = calculateFlooringPrice(hardwoodPrice)
        printFlooringPrice(price, hardwoodPrice)
except:
    print("Please enter a number.")

