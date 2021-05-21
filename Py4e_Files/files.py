# Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
# It doesnâ€™t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.
hand = open("words.txt")

stored_words = dict()
for line in hand:
    line.rstrip()
    words = line.split()
    for word in words:
        stored_words[word] = stored_words.get(word, 0) + 1

word_to_search_for = input("Enter word:")
if word_to_search_for in stored_words.keys():
    print("Word Found")
else:
    print("Word not found")