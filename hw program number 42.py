#Duvall pinkney
#4/24/2015
#hw program number 42

##Due Date: 24 April Reading: Chapter 8
####Write a program that asks the user to enter a number between 0 and 1000,
##inclusive (that is, including the end points 0 and 1000). If they enter a
##number out of range, print a message that the number is out of range and prompt them again for a number between 0 and 1000, inclusive. When the user enters a number in range,
##print the number to the screen and end the program.
def main():
    inLst = eval(input("please enter a number between 0 to 1000: "))
    if inLst < 0:
        print(" Number is too low out of range")
    if inLst > 1000:
        print(" Number is too high and out of range")
    else:
        print(inLst)          

    while inLst < 0:
        inLst = eval(input("please enter a number between 0 to 1000: "))
        if inLst < 0:
            print(" Number is too low out of range")
        if inLst > 1000:
            print(" Number is too high and out of range")
        else:
            print(inLst)          

    while inLst > 1000:
        inLst = eval(input("please enter a number between 0 to 1000: "))
        if inLst < 0:
            print(" Number is too low out of range")
        if inLst > 1000:
            print(" Number is too high and out of range")
        else:
            print(inLst)          

    

main()                   
                 
