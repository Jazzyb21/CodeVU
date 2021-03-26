quarter = 0.25
dime = 0.10
nickel = 0.05
penney = 0.01

user_input = float(input("Enter monies! "))

quarters = user_input / quarter
dimes = user_input % quarter / dime
nickels = user_input % dime / nickel
pennies = user_input % nickel / penney

print(f"Quarters: {quarters}, Dimes: {dimes}, Nickels: {nickels}, Pennies: {pennies}")