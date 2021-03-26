#define variable and prompt user for input for person one
client_one_principal = float(input("Principle (amount): "))
client_one_time =      float(input("Time:               "))
client_one_rate =      float(input("Rate:               "))

#calculate the compound interest for person one 
Amount = client_one_principal * (1 + client_one_rate / 100)**client_one_time
CI = Amount - client_one_principal
print('Compound Interest: ', round(CI,2))

print("---")

#define variable and prompt user for input for person two
client_two_principal = float(input("Principle (amount): "))
client_two_time =      float(input("Time:               "))
client_two_rate =      float(input("Rate:               "))

#calculate the compound interest for person two
Amount = client_two_principal * (1 + client_two_rate / 100)**client_two_time
CI = Amount - client_two_principal
print('Compound Interest: ', round(CI,2))

print("---")

#define variable and prompt user for input for person three
client_three_principal = float(input("Principle (amount): "))
client_three_time =      float(input("Time:               "))
client_three_rate =      float(input("Rate:               "))

#calculate the compound interest for person three
Amount = client_three_principal * (1 + client_three_rate / 100)**client_three_time
CI = Amount - client_three_principal
print('Compound Interest: ', round(CI,2))
   