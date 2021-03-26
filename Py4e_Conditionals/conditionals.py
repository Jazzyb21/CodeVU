A ='Sweet Banana - The least spicy!'
B ='Jalapeno - Feel the heat'
C ='Habanero - Im sweating just thinking about it!'
D ='Carolina Reaper - Im in pain just thinking about it!'
#Phase ONE: 
#we'll use a try except so if someone uses a letter we can tell them to use a number
try:
    scoville_Score = int(input('Whats SHU score can you handle?'))
    #add SP after if to show we can initialize a variable with an empty value so we can assign it with a different value later
    scoville_pepper = ''
    ##do if, then if else and try to add a condition, then use elif
    ##we compare the score the that was given to us to the score of the pepper by using comparison operators
    #explain how if this evaluates to true then it will set the pepper in the body and print that
    if (scoville_Score <= 1000):
        scoville_pepper = A
        ##mistake don't indent
        ##print("you think you can handle this pepper? THE " + scoville_pepper)
        ##we add more branches to our statement so the execution has many different routes to take
        ##we start chaining them together so we have more options
    elif (scoville_Score <= 8000):
        scoville_pepper = B
    elif (scoville_Score <= 2200000):
        scoville_pepper = C
    else:
        scoville_pepper = D
    print("you think you can handle this pepper? THE " + scoville_pepper)
except:
    print('Please, use a number for the SHU.')
#Phase TWO:
try:
    print('We have these peppers: A.) sweet banana,, B.) jalapeno, C.)  Habanero, D.) Carolina Reaper.')
    print('  ')
    favorite_Pepper = input('What pepper is your favorite? Put in their coressponding letter ')
    if (favorite_Pepper == 'a' or favorite_Pepper == 'A'):
        #we can use logical operators to help us short-circuit the condition
        #if our user uses lower case first, perfect! we don't have to worry 
        #But we can also be prepared if the use uppercase this guards us against errors
        ##because it is getting a little hard to read I'm going to add parenthesis
        ##Mistake use one = instead of two
            favorite_Pepper = A
    elif (favorite_Pepper == 'b' or favorite_Pepper == 'B'):
            favorite_Pepper = B
    elif (favorite_Pepper == 'c' or favorite_Pepper == 'C'):
            favorite_Pepper = C
    elif (favorite_Pepper == 'd' or favorite_Pepper == 'D'):
            favorite_Pepper = D
    else:
        print("pick a letter A-F, please.")
    print('your favorite pepper is the ', favorite_Pepper)
except:
    print("pick a letter A-F, please.")
#Phase THREE
try:
   scoville_Score = int(input('Whats SHU score can you handle?'))
    scoville_pepper = ''
    if (scoville_Score <= 1000):
        scoville_pepper = A
    elif (scoville_Score <= 8000):
        scoville_pepper = B
    elif (scoville_Score <= 2200000):
        scoville_pepper = C
    else:
        scoville_pepper = D
    print("you think you can handle this pepper? THE " + scoville_pepper)
    print('We have these peppers: A.) sweet banana,, B.) jalapeno, C.)  Habanero, D.) Carolina Reaper.')
    print('  ')
    favorite_Pepper = input('What pepper is your favorite? Put in their coressponding letter ')
    print('  ')
    more_message = 'You can handle more than your favorite pepper the '
    less_message = 'What! You cant handle the heat of your favorite pepper the '
    your_message = ''
    if (favorite_Pepper == 'a' or favorite_Pepper == 'A'):
            favorite_Pepper = A
            #Banana Pepper
            #we start to add in some functionality of the scoville score chain to determine if our user can in fact handle that pepper
            if (scoville_Score >= 1000):
                your_message = more_message
    elif (favorite_Pepper == 'b' or favorite_Pepper == 'B'):
            favorite_Pepper = B
            #Jalapeno
            if (scoville_Score <= 2000):
                your_message = less_message
            else: 
                your_message = more_message
                #As you can see it starts to become very difficult to read 
    elif (favorite_Pepper == 'c' or favorite_Pepper == 'C'):
            favorite_Pepper = C
            #Habenaro
            if (scoville_Score <= 50000):
               your_message = less_message
            else: 
                your_message = more_message
    elif (favorite_Pepper == 'd' or favorite_Pepper == 'D'):
            favorite_Pepper = D
            #carolina reaper
            if (scoville_Score <= 2200000):
                your_message = less_message
            else: 
                your_message = more_message
    else:
        print("pick a letter A-F, please.")
    print("Based on your SHU score a spicy pepper for you is the " + scoville_pepper)
    print('your favorite pepper is the ', favorite_Pepper)
    print(your_message + favorite_Pepper)
    if (scoville_pepper == favorite_Pepper):
        print('You know what heat level you can handle!')
except:
    print('Please, use a number for the SHU or pick a letter A-F, please for your favorite pepper.')