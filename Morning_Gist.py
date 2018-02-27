#pylint: disable = E0001
#pyling: disable = C0304
'''Write a program to ask the user to enter a string of characters and find its length.
Then provide the following information about this string:
a.
Print the uppercase letters (if any) in the string
b.
Print every 2nd character in the string
c.
    Print the string with all vowels replaced by an underscore and'''
#count/print the number of vowels''''

QUESTION = raw_input("Enter a string of whatever you want \n")
STR_LENGTH = len(QUESTION)
COUNT = 0
print "upper case letters\n",
for x in range(0, STR_LENGTH):
    for i in range(65, 91):
        if STR_LENGTH[x] is chr(i):
            print chr(i),
            COUNT += 1
print "every 2nd character\n",
STR_TWO = 0
while STR_TWO <= STR_LENGTH:
    print STR_LENGTH[STR_TWO],
    STR_TWO += 2
print "all vowels",
VOWELS = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
for i in range(0, STR_LENGTH):
    if VOWELS.__contains__(STR_LENGTH[i]):
        STR_LENGTH.replace(VOWELS, "_")
