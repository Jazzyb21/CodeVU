import math
# Will pull this module in when needed
#This is the math module. We must import it to access many mathmatical functions
# The statement aboves creates a module object named math

# We need to write a program that helps Bob The Builder calculate the amount of flooring a house needs.

vinylPlankPrice = 1.58
marbleTitlePrice = 3.58
solidHardwoodPrice = 2.58
try:
    selectedFlooring = int(input("What type of flooring would you like to purchase? Please select a type that corresponds to a number.\n 1) Vinyl Plank 2) Marble Tile 3) Solid Hardwood\n"))
    if selectedFlooring < 1 or selectedFlooring > 3:
        print("That is not a valid selection.\n")
    
    #Build the code out like this--then refactor. Asks students if they have suggestions on what should be moved into a function and why
    if selectedFlooring == 1:
        #Touch on built in functions
        #Touch on type conversion functions
        #Theses are built in functions that convert values from one type to another
        print("Price: " + str(vinylPlankPrice) +"/ sq. ft.")
        width = float(input("What is the width in feet?\n"))
        length = float(input("What is the length in feet?\n"))
        area = width * length
        finalPrice = area * vinylPlankPrice
        print("Total Cost: $" + str(round(finalPrice, 2)))
    elif selectedFlooring == 2:
        print("Price: " + str(marbleTitlePrice) +"/ sq. ft.")
        width = float(input("What is the width in feet?\n"))
        length = float(input("What is the length in feet?\n"))
        area = width * length
        finalPrice = area * marbleTitlePrice
        print("Total Cost: $" + str(round(finalPrice, 2)))
    elif selectedFlooring == 3:
        print("Price: " +  str(solidHardwoodPrice) + "/sq. ft.")
        width = float(input("What is the width in feet?\n"))
        length = float(input("What is the length in feet?\n"))
        area = width * length
        finalPrice = area * solidHardwoodPrice
        print("Total Cost: $" + str(round(finalPrice, 2)))
except:
    print("Please enter a number.")




# #Final Refactor
# #fruitful function/ pure functions
# # if time this is another option
# def calculateFlooringPriceWithWaste(area, priceSelectedFlooring):
#     response = input("Would you like to include 10% waste in your final quote?\n Y or N\n")
#     price = ''
#     if response.upper() == 'Y':
#         withWaste = area * 1.1
#         x = math.ceil(withWaste)  * priceSelectedFlooring
#         price = float(x)
#     elif response.upper() == 'N':
#         #https://realpython.com/lessons/python-none-overview/
#         #define null objects and variables
#         price = None
#     else:
#         print("Not a valid option. We will assume no.")
#         price = None
#     return price   
        

# # #Fruitful function/ pure function
# def calculateFlooringPrice(priceSelectedFlooring):
#     width = float(input("What is the width in feet?\n"))
#     length = float(input("What is the length in feet?\n"))
#     area = width * length
#     # withWastePrice = calculateFlooringPriceWithWaste(area, priceSelectedFlooring)

#     #ternary operator
#     # value_if_true if condition else value_if_false
#     # return float(withWastePrice) if withWastePrice != None else area * priceSelectedFlooring
#     return area * priceSelectedFlooring

# #Void Function
# def printFlooringPrice(priceSelectedFlooring, finalPrice):
#     print("Price: " + str(priceSelectedFlooring) +"/ sq. ft.")
#     # Floats are bad for precision and we will talk about the why soon. 
#     # If you just cant wait: https://smirnov-am.github.io/representing-money-in-python/
#     # This a built in function to round it to two decimal places
#     #After we round the float to 2 decimal places we must convert the value to a string do concatentation
#     print("Total Cost: $" + str(round(finalPrice, 2)))

# try:
#     selectedFlooring = int(input("What type of flooring would you like to purchase? Please select a type that corresponds to a number.\n 1) Vinyl Plank 2) Marble Tile 3) Solid Hardwood\n"))

#     if selectedFlooring < 1 or selectedFlooring > 3:
#         print("That is not a valid selection.\n")

#     if selectedFlooring == 1:
#         vinylPlankPrice = 1.58
#         finalPrice = calculateFlooringPrice(vinylPlankPrice)
#         printFlooringPrice(vinylPlankPrice, finalPrice)
#     elif selectedFlooring == 2:
#         marbleTitlePrice = 3.58
#         finalPrice = calculateFlooringPrice(marbleTitlePrice)
#         printFlooringPrice(marbleTitlePrice, finalPrice)
#     elif selectedFlooring == 3:
#         solidHardwoodPrice = 2.58
#         finalPrice = calculateFlooringPrice(solidHardwoodPrice)
#         printFlooringPrice(solidHardwoodPrice, finalPrice)

# except: 
#     print("Please enter a number.")

        

