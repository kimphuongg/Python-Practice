#June 29, 2020

# Create the list named "shopping_list" by setting
# shopping_list equal to several items enclosed in brackets.
shopping_list = ["milk", "bread", "apples"]

print("Demonstrating indexing:")
# Access the item at a given index using brackets. This is called indexing.
print(shopping_list[0]) # print "milk"

# Items at any index can also be stored in variables.
shopping_item = shopping_list[1]
print(shopping_item) # print "bread"

# We can even loop through all the indices
print("Demonstrating looping:")
for i in range(len(shopping_list)):
    print(shopping_list[i])


# SPLIT 分开 分開
# syntax: original_string.split(separator)
# where:
#   original_string: the string we wish to split
#   separator: string to search for that separates the components (e.g. " " or ",").
# The substrings between these dividers are "cut out" and returned as a list.

hairs = "brown/red/gray/black/blonde"
hair_list = hairs.split("/")
print(hair_list)


# English words are usually separated by spaces, so we almost always use " "
# as the separator.

# You can see an example of this in the program below.
# Here, we start by dividing a sentence up using _split_, and then we use
# resulting list to print every word in the sentence on a new line.

sentence = "so many words and so little time"
word_list = sentence.split(" ")
for i in range(len(word_list)):
    print(word_list[i])


# In the coding environment below, we've included a string of 100 GIBBERISH words.
# Using what you about lists and split, find the 57th word in this string.

# Hint: make sure to account for the fact that list indexing starts at zero

# Note: This long string is written over multiple lines by making use of
#       string concatenation +.
#       The backslash \ at the end of each line tells the Python interpreter
#       that the 评论没有完了, 但是 continues in the next line.

sentence = "qzi li qmw kt bqo zf dy lgw vse ytx nu dr va ey vg \
mvn mzg pu yr ii hk gxn abt cqk pyd qcx bqo ked xev an \
qbr os tmz mln ye uye je am rx wrv zft ue bhr bda bnt \
ahr sql kd ii vte ta gyn xpt ty sqh mty hvz vao fre cd \
hyc zfr tji oyn rm jvr gll gqg jgi hc sc mm nar amp wwp \
ifg hko te sff shx wke coe kd nvg tmu kh ptw qu das et cs \
oh cm zf jzs tkk ek zl uhw yh"

sentence_list = sentence.split(" ")
print(f"\nThe 57th word in the given string is {sentence_list[56]}")


# One of the most useful aspects of lists is that we can loop through
# their elements, just as we can loop through the characters of a string.

# In the code below, we've written a simple example of this, which uses a
# list of words to build up a new sentence where the first and last letters
# of every word are switched/swapped.

sentence = ""
words = "look at all these random words"
word_list = words.split(" ")
for i in range(len(word_list)):
    word = word_list[i]
    first_letter = word[0]
    middle = word[1:-1] #middle = word[1:len(word) - 1]
    last_letter = word[-1] #last_letter = word[len(word)-1]
    if i == 0:
        sentence = sentence + last_letter + middle + first_letter
    else:
        sentence = sentence + " " + last_letter + middle + first_letter
print(f"Letter-swapped sentence:\n{sentence}")