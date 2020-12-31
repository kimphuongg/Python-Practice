#June 29, 2020

# Earlier quizzes were about the Caesar cipher, a 基本 classic
# encyption method from Roman times. Another method is the
# book cipher (书密码). This code takes the form of a list of numbers,
# each of which represents a single word in the decoded message (短信).

# To translate (翻译) a number (数码) into a word (词 詞),
# 我们需要用一本书，或者 some other large segment of text.
# The word corresponding with a number n is the word at
# index n in your text. In other words, it is the (n+1)th
# word in the book text.

# In the coding environment below is a passage from
# "The Adventures of Huckleberry Finn" by Mark Twain (1884).
# We also included a list of numbers that represents a
# coded message (短信).

# [?]Write a program to decode the secret message represented by
# _numbers_. What does it say?

passage = "Well, the second night a fog begun to come on, and we made for a \
towhead to tie to, for it wouldn't do to try to run in a fog; but when I \
paddled ahead in the canoe, with the line to make fast, there warn't \
anything but little saplings to tie to. I passed the line around one of them \
right on the edge of the cut bank, but there was a stiff current, and the \
raft come booming down so lively she tore it out by the roots and away \
she went. I see the fog closing down, and it make me so sick and scared \
I couldn't budge for most a half a minute it seemed to me."

numbers = [32, 71, 107, 65, 36, 49]
passage_list = passage.split(" ")
message = ""
for i in range(len(numbers)):
    if i == 0:
        message = message + passage_list[numbers[i]]
    else:
        message = message + " " + passage_list[numbers[i]]
print(f"Decoded message is:\n{message}")