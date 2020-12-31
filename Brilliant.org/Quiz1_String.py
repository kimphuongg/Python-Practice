# June 27, 2020

## Create a full Pig Latin translator
vowels = "aeiou"

# get_consonant_prefix(word) takes any string (argument word) and returns the consonant letters at its beginning
def get_consonant_prefix(word):
    consonants = "bcdfghjklmnpqrstvwxyz"
    i = 0
    consonant_prefix = ""
    while (consonants.find(word[i]) > -1):
        consonant_prefix += word[i]
        i += 1
    return consonant_prefix

# get_tail(word) gives us all characters in a word aside from the consonants at the beginning.
def get_tail(word):
    consonants = "bcdfghjklmnpqrstvwxyz"
    i = 0
    consonant_prefix = ""
    while (consonants.find(word[i]) > -1):
        consonant_prefix += word[i]
        i += 1
    tail = word[i:]
    return tail

# Enter a sentence here for it to be converted to pig-latin.
# This code doesn't handle upper-case letters or punctuation.
sentence = "all this pig latin is making me hungry"

pig_sentence = ""
for word in sentence.split(" "):
    if(vowels.find(word[0]) > -1):
        pig_sentence = pig_sentence + word + "yay "
    else:
        pig_sentence = pig_sentence + get_tail(word) + get_consonant_prefix(word) + "ay "
print(pig_sentence)
# word = "through"
# consonant_prefix = get_consonant_prefix(word)
# tail = get_tail(word)
#
# # test the 2 get functions
# print(f"prefix: {consonant_prefix}")
# print(f"tail: {tail}")
#
# pig_word = tail + consonant_prefix + "ay"
#
# print(pig_word)