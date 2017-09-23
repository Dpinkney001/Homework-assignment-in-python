#Duvall Pinkney
#2/7/2015
#program 3-due 2/10/2015
#Assignment: write a program that implements the pseudocode("informal high-level description
#of the operating principle of a computer program or other algorithm")
#

def apartment():
    print("This program will convert your apartment dimesions in meter and convert the size to ")
    print(" square feet. Please enter the size of your apartment in square meters: ")
    size = eval(input("-> "))
    convertedSize = size * 10.764
    print(convertedSize)

apartment()    
