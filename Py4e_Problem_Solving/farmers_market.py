def print_cheese_options(cheeses):
    counter = 0
    for cheese in cheeses:
        counter += 1
        print(f"{counter}) {cheese}")

def print_directions():
    print("All of our bags of cheese curds are $7, but every three bags it will only be $20.\n " +
            "And for every four bags it is $25")
    print("Select the cheeses you would like by selecting the corresponding number. Enter 'done' to complete.")

def calculate_final_price(selections):
    #This range function is exclusive. So, its creates a sequence of numbers from 1 to 5 
    # If I removed adding the 1, then it will only create a sequence from 1 to 4
    total = 0
    for count in range(1, len(selections) + 1):
        total = total + 7
        if count != 1 and count % 3 == 0:
            total = total - 1
        if count != 1 and count % 4 == 0:
            total = total - 2
    return total

def get_cheese_selections():
    selections = list()
    while (True):
        choice = input("What cheese would you like? ")
        if choice.lower() == 'done': break
        int_choice = int(choice)
        if int_choice < 1 or int_choice > 5 : 
            print("Please enter a valid selection.")
        else:
             selections.append(choice)
    return selections



cheeses = ["CHEDDAR CURDS", "GARLIC DILL CHEDDAR CURDS", "CHIVE CHEDDAR CURDS", "SOUR CREAM AND ONION CURDS", "RANCH CURDS"]

print_directions()
print_cheese_options(cheeses)

try: 
    cheese_selections = get_cheese_selections()
except:
    print("Please enter a number that corresponds with the list of cheeses.")
total = calculate_final_price(cheese_selections)
print(f"Final Price: ${total}")


