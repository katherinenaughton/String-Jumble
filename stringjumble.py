"""
stringjumble.py
Author: Katie Naughton
Credit: I worked with Noah. 

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""

text=input("Please enter a string of text (the bigger the better) : ")
print('You entered "' +text+ '". Now jumble it: ')

#letters in reverse
print(text[::-1])

#words in reverse, letters correct order
wordlist=[]
word=""
for i in text[::-1]:
    if i!=" ":
        word=i+word
    if i==" ":
        wordlist.append(word)
        word=""
wordlist.append(word)
#print(wordlist)
output=""
for i in wordlist:
    output += i + " "
print(output)

#words correct, letters reversed
wordlist=[]
word=""
for i in text:
    if i!=" ":
        word=i+word
    if i==" ":
        wordlist.append(word)
        word=""
wordlist.append(word)

output=""
for i in wordlist:
    output += i + " "
print(output)