# import string
#File Processing
#A text file is a sequence of lines
# a text file has newlines at the end of each line
#To read a file you must call the open(filename, mode)  -mode is optional
#example file_handle = open('strings.py', 'r')

# What is a handle: opening outside to the program, you can talk to the file from the handle. A thing that allows you to get to the file
#\n still one character

#Reading Files in Python
# Example xfile = open('mbox.text)
# for line in xfile:
    #print(cheese)
#Reading the Whole File into a sinlge string Example:
# result = file_hanlde.read()

# file_name = input("Enter a file name: ")

# try:
#     result = file_name.find('na na boo boo')
#     if result == -1:
#         file_handle = open(file_name)
#     else:
#         print("Na na boo to you! You have been punk'd")
#         quit()
        
# except:
#     print("File cannot be opened: ", file_name)
#     file_handle.close()
#     quit()

# count = 0
# for line in file_handle:    
#     line = line.rstrip()
#     count = count + 1
# file_handle.close()
# print(f"There are {count} lines in this {file_name}")


# Write a program to read through a file and 
# Print the contents of the file (line by line) 
# All in upper case. 

file_name = input('Enter the file name. ')
file_name = file_name.lower()
line_count = 0
if file_name == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd! ")
else:
    try:
        f_hand = open(file_name)
    except:
        print('File cannot be opened:', file_name)
        quit()
    for lines in f_hand:
        line_count = line_count + 1
    print('There were', line_count, 'subject lines in', file_name)          


