jalapeno = 'Jalopeno'
habenaro = 'Habernero'
sweet_banana = 'Sweet Banana'
carolina_reaper = 'Carolina Reaper'
# try:
#     scoville_score = int(input('What SHU score can you handle?'))

#     #what are some other comparison operators?

    #what are other logical operators
#   #maybe have students shout out or tyupe out what to do next
    # give the sudents more control
    # may be too long
    
    
#     pepper = ''

#     if scoville_score <= 1000:
#         pepper = sweet_banana
#     elif scoville_score <= 8000:
#         pepper = jalapeno
#     elif scoville_score <= 2200000:
#         pepper = habenaro  
#     else: 
#         pepper = carolina_reaper 

#     print('You think you can handle this pepper? The ' + pepper)
# except:
#     print('Please enter a number.')
try:
    print('We have these peppers. A) Sweet B B) Jalo B) Habo D) reaper')
    favorite_Pepper = input('What is your favorite pepper? Please pick the corresponding pepper. ')
    if favorite_Pepper == 'a' or favorite_Pepper == 'A':
        favorite_Pepper = sweet_banana
    elif favorite_Pepper == 'b' or favorite_Pepper == 'B':
        favorite_Pepper == jalapeno
    elif favorite_Pepper == 'c' or favorite_Pepper == 'C':
        favorite_Pepper = carolina_reaper
    elif favorite_Pepper == 'd'  or favorite_Pepper == 'D':
        favorite_Pepper == habenaro
    else:
        print('Please enter a valid character.')
    print('Favorite Pepper: ', favorite_Pepper)
except:
    print('Please enter a string.')


