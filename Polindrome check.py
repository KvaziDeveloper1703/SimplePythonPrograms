"""
This program checks, if given sentance is polindrome.
Polindrome is a sentance, that does not change, if we read it backwards.
"""
choice = 1;
while choice == 1:
    textLine = input("Write a string here, to check if it is a polindrome:") #We enter the line
    reversedTextLine = textLine[::-1] #We reverse the line entered
    casefoldTextLine = textLine.casefold() #We get rid of capital letters, so program can also work with capitalized sentences 
    casefoldReversedTextLine = reversedTextLine.casefold()
    if casefoldTextLine == casefoldReversedTextLine:
        print("It is a polindrome")
    else:
        print("It is not a polindrome")
    choice = int(input("Do you want to check other string?[Yes-1/No-0]")) #Here user can choose to continue or stop using this program
