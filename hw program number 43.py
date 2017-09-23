#Duvall Pinkney
#4/25/2015
# hw program number 43


##Due Date: 27 April Reading: Chapter 8
##Write a program that asks the user to enter a string. If
##the user enters an empty string, your program should continue
##prompting the user for a new string until they enter a non-empty string.
##Your program should then print out the string entered.
#####
def main():
    
    inString = input("Please enter a string: ")
    print(inString)
    while inString != "":
        inString = input("Please enter a string: ")
        print(inString)

main()        

    
