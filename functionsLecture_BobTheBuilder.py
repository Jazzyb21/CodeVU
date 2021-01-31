import math
# Will pull this module in when needed
#This is the math module. We must import it to access many mathmatical functions
# The statement aboves creates a module obeject named math

# We need to write a program that helps Bob The Builder calculate the amount of flooring a house needs.

vinylPlankPrice = 1.58
marbleTitlePrice = 3.58
solidHardwoodPrice = 2.58

selectedFlooring = int(input("What type of flooring would you like to purchase? Please select a type that corresponds to a number.\n 1) Vinyl Plank 2) Marble Tile 3) Solid Hardwood\n"))


#Build the code out like this--then refactor. Asks students if they have suggestions on what should be moved into a function and why

if selectedFlooring == 1:
    #Touch on built in functions
    #Touch on type conversion functions
    print("Price: " + str(vinylPlankPrice) +"/ sq. ft.")
    width = float(input("What is the width in feet?\n"))
    length = float(input("What is the length in feet?\n"))
    area = width * length
    finalPrice = area * vinylPlankPrice
    print("Total Cost: $" + str(finalPrice))
    userInput = input("\nWould you like to include an extra 10% to cover potential waste and breaks? Y or N\n")
    if userInput.upper() == "Y":
        withWaste = area * 1.1
        # Explain why we want to round this floating point number to the nearest integer that is greater than or equal to a given number. (round up)
        # Per my flooring research, generally, you will want to add a 10% waste factor: Just multiply your area by 1.1 and then round upward. 
        # Here we need to specify the name of the module to access the function using dot notation
        finalPrice = math.ceil(withWaste)  * vinylPlankPrice
        print("Price including an extra 10%: $" + str(finalPrice))
    else:
        print("Thank you for choosing Bob The Builder for your flooring needs!")
elif selectedFlooring == 2:
    print("Price: " + str(marbleTitlePrice) +"/ sq. ft.")
    width = float(input("What is the width in feet?\n"))
    length = float(input("What is the length in feet?\n"))
    area = width * length
    finalPrice = area * marbleTitlePrice
    print("Total Cost: $" + str(finalPrice))
    userInput = input("\nWould you like to include an extra 10% to cover potential waste and breaks? Y or N\n")
    if userInput.upper() == "Y":
        withWaste = area * 1.1
        finalPrice = math.ceil(withWaste)  * marbleTitlePrice
        print("Price including an extra 10%: $" + str(finalPrice))
    else:
        print("Thank you for choosing Bob The Builder for your flooring needs!")
elif selectedFlooring == 3:
    print("Price: " +  str(solidHardwoodPrice) + "/sq. ft.")
    width = float(input("What is the width in feet?\n"))
    length = float(input("What is the length in feet?\n"))
    area = width * length
    finalPrice = area * solidHardwoodPrice
    print("Total Cost: $" + str(finalPrice))
    userInput = input("\nWould you like to include an extra 10% to cover potential waste and breaks? Y or N\n")
    if userInput.upper() == "Y":
        withWaste = area * 1.1
        finalPrice = math.ceil(withWaste)  * solidHardwoodPrice
        print("Price including an extra 10%: $" + str(finalPrice))
    else:
        print("Thank you for choosing Bob The Builder for your flooring needs!")
else:
    print("We don't that carry that")




#Final Refactor
# #Note this function is getting large. Can we break this out further
# #Void function
# def calculateFlooringPrice(priceSelectedFlooring):
#     print("Price: " + str(priceSelectedFlooring) +"/ sq. ft.")
#     width = float(input("What is the width in feet?\n"))
#     length = float(input("What is the length in feet?\n"))
#     area = width * length
#     finalPrice = area * priceSelectedFlooring
#     print("Total Cost: $" + str(finalPrice))
#     userInput = input("\nWould you like to include an extra 10% to cover potential waste and breaks? Y or N\n")
#     if userInput.upper() == "Y":
#         finalPrice = calculateFlooringPriceWithWaste(area, priceSelectedFlooring)
#         print("Price including an extra 10%: $" + str(finalPrice))
#     else:
#         print("Thank you for choosing Bob The Builder for your flooring needs!")

# #fruitful function
# def calculateFlooringPriceWithWaste(area, priceSelectedFlooring):
#     withWaste = area * 1.1
#     return math.ceil(withWaste)  * priceSelectedFlooring


# if selectedFlooring == 1:
#     vinylPlankPrice = 1.58
#     calculateFlooringPrice(vinylPlankPrice)
# elif selectedFlooring == 2:
#     marbleTitlePrice = 3.58
#     calculateFlooringPrice(vinylPlankPrice)
# elif selectedFlooring == 3:
#     solidHardwoodPrice = 2.58
#     calculateFlooringPrice(vinylPlankPrice)
# else:
#     print("We don't that carry that")
        



